#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sqlite3
from tqdm import tqdm
from itertools import count



class Column(object):
      _ids = count(0)

      def __init__(self):
          self.id = self._ids.next()


class Metric(Column):
    def __init__(name, label=None):
        super(Metric, self).__init__()
        self.name = name
        self.label = label


class Dimension(Column):
    def __init__(name):
        super(Dimension, self).__init__()
        self.name = name
        self.is_dim = True


def build_data_element():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    query = 'select {columns} from {table} LIMIT {limit}'
    table = 'morrisql_report_data'
    dimensions = ['report_date']
    metrics = ['metric_1', 'metric_2', 'Custom metric']
    LIMIT = 365
    labels = None

    column_objects = []

    for d in dimensions:
        column_objects.append(Dimension(name=d))

    for m in metrics:
        column_objects.append(Metric(name=m))
    
    #clean and join col
    columns = ','.join(['"{}"'.format(co.name) for co in column_objects])
    # whoiswho ?
    # dimensions :: 0 -> len(dimensions) - 1
    # metrics    :: len(dimensions) -> len(dimensions) - 1
    
    query = query.format(
        table = table,
        columns = columns,
        limit = LIMIT
    )
    cur.execute(query)
    for l in cur:
        print l




    

def main():
    build_data_element()




if __name__ == '__main__':
    main()
