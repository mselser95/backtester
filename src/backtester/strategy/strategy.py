#!/usr/bin/env python
# coding:utf-8
"""
Name    : __init__.py
Author  : Matias Selser
Time    : 8/23/21 1:28 PM
Desc    :
"""


class Strategy:

    def __init__(self):
        pass

    def step(self):
        raise NotImplemented

    def get_assets(self):
        raise NotImplemented

    def reset_strategy(self):
        raise NotImplemented
