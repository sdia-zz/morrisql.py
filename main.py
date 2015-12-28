#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sqlite3
from tqdm import tqdm
from itertools import count



class Column(object):
    _ids = count(0)

    def __init__(self, name = None):
        self.idx = self._ids.next()
        self.name = name
        
    def key(self):
        return self.name.lower().replace(' ', '_')


class Metric(Column):
    def __init__(self, name, label=None):
        super(Metric, self).__init__()
        self.name = name
        self.label = label


class Dimension(Column):
    def __init__(self, name):
        super(Dimension, self).__init__()
        self.name = name
        self.is_dim = True


def load_config(conn, config_table, config_ref):
    
    # move this to settings
    query = '''SELECT reference, 
                      report_plot_type,
                      report_dom_location,
                      report_dimensions,
                      report_metrics,
                      report_additional_options
               FROM {config_table}
               WHERE reference = {config_ref}
               LIMIT 1;
    '''

    cur = conn.cursor()
    cur.execute(query.format(
        config_table = config_table,
        config_ref = config_ref
    ))
    res = cur.fetchone()

    return dict(
        reference = res[0],
        report_plot_type = res[1],
        report_dom_location = res[2],
        report_dimensions = res[3].split("'"),
        report_metrics = res[4].split("'"),
        report_additional_options = res[5].split("'")
    )




def build_data_element(conn, table, dimensions, metrics):

    cur = conn.cursor()
    query = 'select {columns} from {table} LIMIT {limit}'
    LIMIT = 365
    column_objects = []

    for d in dimensions:
        column_objects.append(Dimension(name=d))

    for m in metrics:
        column_objects.append(Metric(name=m))
        
    query = query.format(
        table = table,
        columns = ','.join(['"{}"'.format(co.name) for co in column_objects]),
        limit = LIMIT
    )

    data = []
    cur.execute(query)
    for r in cur:
        d = {}
        for m in column_objects:
            d[m.key()] = r[m.idx]

        data.append(d)

    return data


    

def main():
    conn = sqlite3.connect('tests/test.db')
    table = 'morrisql_report_data'
    dimensions = ['report_date']
    metrics = ['metric_1', 'metric_2', 'Custom metric']
    for l in build_data_element(conn, table, dimensions, metrics):
        print l
    



if __name__ == '__main__':
    main()
