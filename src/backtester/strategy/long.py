#!/usr/bin/env python
# coding:utf-8
"""
Name    : __init__.py
Author  : Matias Selser
Time    : 8/23/21 1:28 PM
Desc    :
"""

import backtester.strategy.strategy as strategy

import numpy as np


class Long(strategy.Strategy):

    def __init__(self, assets, weights):
        super().__init__()
        self.assets = assets
        self.weights = weights
        self.pxs = [asset.get_px() for asset in self.assets]

    def step(self):
        # calculate returns for every asset
        returns = np.array([asset.get_px() / self.pxs[i] - 1 for i, asset in enumerate(self.assets)])

        # calculate total return as the sum of all the returns times the weights of each asset
        ret = np.dot(returns, self.weights)

        # update last px
        self.pxs = [asset.get_px() for asset in self.assets]

        return ret

    def get_assets(self):
        return self.assets

    def reset_strategy(self):
        self.pxs = [asset.get_px() for asset in self.assets]

