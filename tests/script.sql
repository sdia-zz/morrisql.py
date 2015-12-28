/*
This sqlite3 compliant, only for testing purpose,
*/

DROP TABLE IF EXISTS morrisql_report_line;
CREATE TABLE morrisql_report_line (
       report_date DATE,
       metric_1 NUMERIC,
       metric_2 NUMERIC,
       "Custom metric" NUMERIC
);

DROP TABLE IF EXISTS morrisql_report_bar;
CREATE TABLE morrisql_report_bar (
       report_date DATE,
       Variable_A  NUMERIC,
       "Variable B" NUMERIC
);

DROP TABLE IF EXISTS morrisql_report_donut;
CREATE TABLE morrisql_report_donut (
       "Download Sales" NUMERIC,
       "In-Store Sales" NUMERIC,
       "Mail-Order Sales" NUMERIC
);

DROP TABLE IF EXISTS morrisql_report_config;
CREATE TABLE morrisql_report_config (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       reference VARYING CHARACTER(255),
       report_plot_type VARYING CHARACTER(255),
       report_dom_location VARYING CHARACTER(255),
       report_dimensions VARYING CHARACTER(255),
       report_metrics VARYING CHARACTER(255),
       report_additional_options TEXT
);

INSERT INTO morrisql_report_config (reference, report_plot_type, report_dom_location, report_dimensions, report_metrics, report_additional_options)
VALUES
('lineplot01', 'line', 'line-example', 'report_date', 'metric_1, metric_2, Custom metric', NULL),
('barplot01', 'bar', 'bar-example', 'report_date', 'Variable_A, Variable B', NULL),
('donutplot01', 'donut', 'donut-example', NULL, 'Download Sales, In-Store Sales, Mail-Order Sales', NULL);

INSERT INTO morrisql_report_donut
VALUES (12, 30, 20);

INSERT INTO morrisql_report_bar (report_date, "Variable_A", "Variable B")
VALUES
('2015-05-31', 5, 16),
('2015-05-30', 5, 20),
('2015-05-29', 3, 18),
('2015-05-28', 2, 19),
('2015-05-27', 9, 15);



INSERT INTO morrisql_report_line (report_date, metric_1, metric_2, "Custom metric")
VALUES
('2015-05-31', 5, 16, 27),
('2015-05-30', 5, 20, 25),
('2015-05-29', 3, 18, 28),
('2015-05-28', 2, 19, 25),
('2015-05-1', 3, 19, 26);
