#!/usr/bin/env python
#-*- coding:utf-8 -*-


from setuptools import setup
from morrisql import __version__


setup(
    name = 'morrisql.py',
    version = __version__,
    author = 'Seydou Dia',
    author_email = 'sdia.pyc@gmail.com',
    description = 'MorriSQL.py produce Json data from SQL table for input to Morris.JS graph framework.',
    license = 'MIT',
    keywords = 'morris.js, sql, json',
    py_modules = ['morrisql'],
    long_description = open('README.md').read())
