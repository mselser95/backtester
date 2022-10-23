#!/usr/bin/env python
# coding:utf-8
"""
Name    : __init__.py
Author  : Matias Selser
Time    : 8/23/21 1:28 PM
Desc    :
"""
import numpy as np


class Portfolio:

    def __init__(self, strategies, weights):
        self.strategy_to_weight = {}
        self.strategies = strategies
        self.weights = weights

        for strategy, weight in zip(strategies, weights):
            self.strategy_to_weight[strategy] = weight

    def get_returns(self):
        ret = 0
        for strategy, weights in self.strategy_to_weight.items():
            ret += np.dot(strategy.step(), weights)

        return ret
