/*
This sqlite3 compliant, only for testing purpose,
*/

DROP TABLE IF EXISTS morrisql_report_data;
CREATE TABLE morrisql_report_data (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       report_date DATE, -- NON-UNIQUE FOR TESTING PURPOSE
       metric_1 NUMERIC,
       metric_2 NUMERIC,
       "Custom metric" NUMERIC
);

DROP TABLE IF EXISTS morrisql_report_config;
CREATE TABLE morrisql_report_config (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       reference VARYING CHARACTER(255),
       report_plot_type VARYING CHARACTER(255),
       report_dom_location VARYING CHARACTER(255),
       report_dimension VARYING CHARACTER(255),
       report_metrics VARYING CHARACTER(255),
       report_labels VARYING CHARACTER(255),
       report_additional_options TEXT
);

INSERT INTO morrisql_report_config (reference, report_plot_type, report_dom_location, report_dimension, report_metrics, report_labels, report_additional_options)
VALUES
('lineplot01', 'line', 'morris-example', 'report_date', 'metric_1, metric_2, Custom metric', 'Sales 2014, Sales 2015, Projection 2016', NULL),
('lineplot02', 'line', 'morris-example', 'report_date', 'metric_1, metric_2, Custom metric', NULL, NULL),
('lineplot03', 'line', 'morris-example', 'report_date', 'metric_1, metric_2, Custom metric', 'Sales 2014, Sales 2015, Projection 2016', NULL)
;

INSERT INTO morrisql_report_data (report_date, metric_1, metric_2, "Custom metric")
VALUES
('2015-05-31', 5, 16, 27),
('2015-05-30', 5, 20, 25),
('2015-05-29', 3, 18, 28),
('2015-05-28', 2, 19, 25),
('2015-05-27', 9, 15, 28),
('2015-05-26', 10, 18, 27),
('2015-05-25', 6, 20, 30),
('2015-05-24', 1, 18, 30),
('2015-05-23', 3, 16, 29),
('2015-05-22', 5, 16, 25),
('2015-05-21', 4, 17, 29),
('2015-05-20', 3, 17, 25),
('2015-05-19', 8, 19, 26),
('2015-05-18', 9, 17, 28),
('2015-05-17', 4, 16, 27),
('2015-05-16', 9, 17, 29),
('2015-05-15', 9, 20, 28),
('2015-05-14', 7, 16, 27),
('2015-05-13', 10, 19, 30),
('2015-05-12', 7, 20, 30),
('2015-05-11', 8, 15, 25),
('2015-05-10', 10, 17, 28),
('2015-05-9', 5, 16, 28),
('2015-05-8', 10, 17, 26),
('2015-05-7', 10, 18, 26),
('2015-05-6', 1, 18, 26),
('2015-05-5', 6, 18, 27),
('2015-05-4', 9, 20, 30),
('2015-05-3', 3, 18, 30),
('2015-05-2', 3, 17, 25),
('2015-05-1', 3, 19, 26);
