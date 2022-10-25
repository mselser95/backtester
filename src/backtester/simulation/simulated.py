#!/usr/bin/env python
# coding:utf-8
"""
Name    : __init__.py
Author  : Matias Selser
Time    : 8/23/21 1:28 PM
Desc    :
"""
import time
from copy import copy

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
        for strategy in self.initial_portfolio.strategies:
            asset_list.update(strategy.get_assets())

        self.price_generator = g.SimulatedPriceGenerator(asset_list)

    def run(self):

        returns = np.zeros((self.times, self.steps)) # define returns array

        for run in tqdm_notebook(range(self.times), total=self.times):  # run n simulations
            portfolio = copy(self.initial_portfolio)  # save copy of initial portfolio

            for step in range(self.steps):  # of m steps
                self.price_generator.update_prices()  # update prices of assets
                returns[run, step] = portfolio.get_returns()  # calculate returns with new prices

            self.price_generator.reset_prices()  # reset prices for new run
            for strategy in self.initial_portfolio.strategies:
                strategy.reset_strategy()

        return {
            "Returns": returns,
        }
