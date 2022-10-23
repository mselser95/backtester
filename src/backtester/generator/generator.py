#!/usr/bin/env python
# coding:utf-8
"""
Name    : __init__.py
Author  : Matias Selser
Time    : 8/23/21 1:28 PM
Desc    :
"""

import numpy as np


class SimulatedPriceGenerator:

    def __init__(self, assets):
        self.assets = assets
        self.starting_px = [asset.get_px() for asset in assets]

    def update_prices(self):
        for asset in self.assets:
            px = asset.get_px()
            asset.set_px(px * asset.parameters["mu"] + asset.parameters["sigma"] * np.random.normal())

    def reset_prices(self):
        for asset, starting_px in zip(self.assets, self.starting_px):
            asset.set_px(starting_px)