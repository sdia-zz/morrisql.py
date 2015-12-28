# morrisql.py

MorriSQL.py produce Json data from SQL table for input to Morris.JS graph framework.


## How it works ?

The main API of this library requires :

    * connection to a database,
    * table containing the report,
    * a config table,
    * a configuration reference

### Database connection

    >>> conn = psycopg2.connect('localhost, port ...')


### The report table


| report_date | metric_1 | metric_2 | Custom metric |
|---|---|---|---
'2015-05-31'| 5| 16| 27|
'2015-05-30'| 5| 20| 25|
'2015-05-29'| 3| 18| 28|
'2015-05-28'| 2| 19| 25|
'2015-05-1' | 3| 19| 26|


### The config table

This is the central component of this library, please follow the ddl :

    CREATE TABLE morrisql_report_config (
           reference VARYING CHARACTER(255) PRIMARY KEY, -- or unique
           report_plot_type VARYING CHARACTER(255),
           report_dom_location VARYING CHARACTER(255),
           report_dimensions VARYING CHARACTER(255),
           report_metrics VARYING CHARACTER(255),
           report_additional_options TEXT
    );


| reference | report_plot_type | report_dom_location | report_dimensions | report_metrics | report_additional_options |
|---|---|---|---|---|---|
|'lineplot01'| 'line' | 'line-example' | 'report_date' | 'metric_1, metric_2, Custom metric' | NULL |
|'areaplot01'| 'area' | 'area-example' | 'report_date' | 'metric_1, metric_2, Custom metric' | NULL |
|'barplot01' | 'bar'  | 'bar-example'  | 'report_date' | 'Variable_A, Variable B'            | NULL |


### Putting all together ...

    >>> from MorriSQL.py import MorrisGraph
    >>> mg = MorrisGraph(
                 conn = sqlite3.connect('tests/test.db'),        
                 report_table = 'morrisql_report_line',
                 config_table = 'morrisql_report_config',
                 config_ref = 'lineplot01')
    >>> mg.to_json()
Morris.Line({
  "xkey": [
    "report_date"
  ], 
  "element": "line-example", 
  "labels": [
    "metric_1", 
    "metric_2", 
    "Custom metric"
  ], 
  "ykeys": [
    "metric_1", 
    "metric_2", 
    "custom_metric"
  ], 
  "data": [
    {
      "metric_1": 5, 
      "report_date": "2015-05-31", 
      "metric_2": 16, 
      "custom_metric": 27
    }, 
    {
      "metric_1": 5, 
      "report_date": "2015-05-30", 
      "metric_2": 20, 
      "custom_metric": 25
    }, 
    {
      "metric_1": 3, 
      "report_date": "2015-05-29", 
      "metric_2": 18, 
      "custom_metric": 28
    }, 
    {
      "metric_1": 2, 
      "report_date": "2015-05-28", 
      "metric_2": 19, 
      "custom_metric": 25
    }, 
    {
      "metric_1": 3, 
      "report_date": "2015-05-1", 
      "metric_2": 19, 
      "custom_metric": 26
    }
  ]
})