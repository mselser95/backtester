# backtester

Modular Python backtesting framework for trading strategies.

## Components

- **Asset** — holds price series and statistical parameters (mu, sigma)
- **Strategy** — abstract base for trading strategies. Includes a `Long` implementation for weighted long-only returns
- **Portfolio** — combines multiple strategies with configurable weights
- **Generator** — simulated price generation using random walk with drift
- **Simulation** — Monte Carlo engine that runs N simulations of M steps each

## Quick start

```python
from backtester.asset import Asset
from backtester.strategy import Long
from backtester.portfolio import Portfolio
from backtester.simulation import MontecarloSimulation

assets = [Asset("BTC", prices, mu=0.001, sigma=0.02)]
strategy = Long(assets, weights=[1.0])
portfolio = Portfolio([strategy], weights=[1.0])
sim = MontecarloSimulation(portfolio, n_simulations=1000, n_steps=252)
sim.run()
```

## Development

```bash
pip install -r requirements.txt
tox
```

## License

MIT
