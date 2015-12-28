#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sqlite3
from morrisql import MorrisGraph


def main():
    print('Line example ....')
    mg = MorrisGraph(
        conn = sqlite3.connect('sql/test.db'),        
        report_table = 'morrisql_report_line',
        config_table = 'morrisql_report_config',
        config_ref = 'lineplot01')
    print(mg.to_json())

    print('Area example ....')
    mg = MorrisGraph(
        conn = sqlite3.connect('sql/test.db'),        
        report_table = 'morrisql_report_line',
        config_table = 'morrisql_report_config',
        config_ref = 'areaplot01')
    print(mg.to_json())

    print('Bar example ....')
    mg = MorrisGraph(
        conn = sqlite3.connect('sql/test.db'),        
        report_table = 'morrisql_report_bar',
        config_table = 'morrisql_report_config',
        config_ref = 'barplot01')
    print(mg.to_json())

    print('Donut example ....')
    mg = MorrisGraph(
        conn = sqlite3.connect('sql/test.db'),        
        report_table = 'morrisql_report_donut',
        config_table = 'morrisql_report_config',
        config_ref = 'donutplot01')
    print(mg.to_json())
    

if __name__ == '__main__':
    main()
