#!/usr/bin/env python
# coding:utf-8
"""
Name    : __init__.py
Author  : Matias Selser
Time    : 8/23/21 1:28 PM
Desc    :
"""
import time

import numpy as np

import backtester.simulation.simulation as simulation
import backtester.generator.generator as g
from tqdm import tqdm_notebook


class MontecarloSimulation(simulation.Simulation):

    def __init__(self, steps, times, portfolio):
        super().__init__()
        self.steps = steps
        self.times = times
        self.initial_portfolio = portfolio

        asset_list = set()
        for strategy in self.initial_portfolio:
            asset_list.union(strategy.get_assets())

        self.price_generator = g.SimulatedPriceGenerator(asset_list)

    def run(self):
        returns = np.array((self.times, self.steps))
        for run in tqdm_notebook(range(self.times), total=self.times):  # run n simulations
            portfolio = self.initial_portfolio.copy()
            for step in range(self.steps):  # of m steps
                returns[run][step] = portfolio.get_returns()

        return {
            "Returns": returns,
        }
