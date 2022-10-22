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
        returns = np.array([asset.get_px() / self.pxs[i] - 1 for i, asset in enumerate(self.assets)])
        self.pxs = [asset.get_px() for asset in self.assets]
        return returns
