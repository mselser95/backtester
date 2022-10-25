#!/usr/bin/env python
# coding:utf-8
"""
Name    : __init__.py
Author  : Matias Selser
Time    : 8/23/21 1:28 PM
Desc    :
"""

import simulation


class RealSimulation(simulation.Simulation):

    def __init__(self, start_time, end_time, portfolio):
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time
        self.portfolio = portfolio

    def run(self):
        pass
