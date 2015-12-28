#!/usr/bin/env python
#-*- coding:utf-8 -*-


import json
from itertools import count


class Column(object):
    
    'Base Column object to keep track of Metric and Dimension ordering.'

    _ids = count(0)

    def __init__(self, name = None):
        self.idx = next(self._ids)
        self.is_dim = False

    @property
    def key(self):
        return self.name.lower().replace(' ', '_')

    @classmethod
    def reset(cls):
        'needed if more than 1 report in same thread.'
        cls._ids = count(0)

        
class Metric(Column):
    def __init__(self, name, label=None):
        super(Metric, self).__init__()
        self.name = name


class Dimension(Column):
    def __init__(self, name):
        super(Dimension, self).__init__()
        self.name = name
        self.is_dim = True

        
class MorrisGraph(object):

    'Given a report and a configuration produces Morris report as Json.'

    data_limit = 365
    conf_query = '''SELECT reference, 
                           report_plot_type,
                           report_dom_location,
                           report_dimensions,
                           report_metrics,
                           report_additional_options
                    FROM {config_table}
                    WHERE reference = '{config_ref}'
                    LIMIT 1;'''
    data_query = 'SELECT {columns} FROM {table} LIMIT {data_limit}'
    json_template = 'Morris.{report_plot_type}({data_dict})'
    json_indent = 2
    
    def __init__(self, conn, report_table, config_table, config_ref):
        self.conn = conn
        self.report_table = report_table
        self.config_table = config_table
        self.config_ref = config_ref

    def _load_config(self):    
        cur = self.conn.cursor()
        cur.execute(self.conf_query.format(
            config_table = self.config_table,
            config_ref = self.config_ref))
        res = cur.fetchone()
        if res == None:
            err_mess = 'No configuration found for ref. {}\n'.format(self.config_ref)
            err_mess += 'Please verify {}'.format(self.config_table)
            raise Exception(err_mess)
        reference = res[0]
        report_plot_type = res[1]
        report_dom_location = res[2]
        report_dimensions = res[3].split(",") if res[3] else []
        report_metrics = res[4].split(",") if res[4] else []
        report_additional_options = res[5]
        # additionnal cleaning
        report_dimensions = [d.strip() for d in report_dimensions]
        report_metrics = [m.strip() for m in report_metrics]
        return dict(
            reference = reference,
            report_plot_type = report_plot_type.lower().capitalize(),
            report_dom_location = report_dom_location,
            report_dimensions = report_dimensions,
            report_metrics = report_metrics,
            report_additional_options = report_additional_options)

    def _get_data_dict(self, conf):   #conn, table, dimensions, metrics):
        cur = self.conn.cursor()
        column_objects = []
        # needed if more than 1 report in same thread
        Column.reset()
        for d in conf['report_dimensions']:
            column_objects.append(Dimension(name=d))
        for m in conf['report_metrics']:
            column_objects.append(Metric(name=m))
        cur.execute(
            self.data_query.format(
                table = self.report_table,
                columns = ','.join(['"{}"'.format(col.name) for col in column_objects]),
                data_limit = self.data_limit))
        data = []
        for r in cur:
            d = {}
            for m in column_objects:
                d[m.key] = r[m.idx]
            data.append(d)
        return dict(
            data = data,
            xkey = [col.key for col in column_objects if col.is_dim],
            ykeys = [col.key for col in column_objects if not col.is_dim],
            labels = [col.name for col in column_objects if not col.is_dim])

    def to_json(self):
        conf = self._load_config()
        data_dict = self._get_data_dict(conf)
        data_dict['element'] = conf['report_dom_location']
        return self.json_template.format(
            report_plot_type = conf['report_plot_type'],
            data_dict = json.dumps(data_dict, indent=self.json_indent))
