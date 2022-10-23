#!/usr/bin/env python
# coding:utf-8
"""
Name    : __init__.py
Author  : Matias Selser
Time    : 8/23/21 1:28 PM
Desc    :
"""


class Asset:

    def __init__(self, name, px, mu, sigma):
        self.name = name
        self.px = px
        self.parameters = {
            "mu": mu,
            "sigma": sigma
        }

    def get_px(self):
        return self.px

    def set_px(self, px):
        self.px = px
