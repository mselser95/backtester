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
        print(self.weights)
        ret = np.dot(returns, self.weights)

        # update last px
        self.pxs = [asset.get_px() for asset in self.assets]

        return ret

    def get_assets(self):
        return self.assets

    def reset_strategy(self):
        self.pxs = [asset.get_px() for asset in self.assets]