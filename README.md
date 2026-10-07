# Quant Toolkit

**Build your own quant research system from scratch — one module at a time.**

This is the companion codebase for the Goosos tutorial series
[*Build Your Own Quant Research System*](https://goosos.com).
Each tutorial adds one module. Follow the series, and you'll understand
every line of your own research toolkit.

> **Scope:** research & backtesting only — data → backtest → validation.
> Live trading (brokers, execution, risk) is a separate series.

## Modules

| Module | Tutorial | Status |
|---|---|---|
| `backtest.py` | [Part 1: VectorBT Tutorial](https://github.com/goosos/vectorbt-tutorial) | ✅ |
| `validation.py` | [Part 2: Walk-Forward Analysis](https://github.com/goosos/walkforward-tutorial) | ✅ |
| `overfitting.py` | Part 4: PBO & Deflated Sharpe | 🔲 |
| `costs.py` | Part 6: Slippage & Commissions | 🔲 |
| `sizing.py` | Part 7: Kelly Criterion | 🔲 |
| `data.py` | Part 9: Lookahead & Survivorship Bias | 🔲 |
| `metrics.py` | Part 10: Sharpe vs Sortino | 🔲 |

Parts 3 (VectorBT vs Backtrader), 5 (Backtesting.py), and 8 (NautilusTrader)
are engine comparisons — they don't add modules, they teach you when to
swap the engine underneath `backtest.py`.

## Design principles

1. **One module, one job.** Each file does a single thing and does it well.
2. **No hidden state.** Functions take data in, return results out. No globals, no singletons.
3. **Beginner-readable.** If a line needs a comment to be understood, it gets one.
4. **Tested.** Every module ships with tests in `tests/`.

## Quickstart

```bash
pip install -r requirements.txt
python examples/ma_crossover.py
```

## Layout

```
quant_toolkit/      # the library — one module per tutorial
tests/              # pytest, one file per module
examples/           # runnable scripts tying modules together
```

## License

MIT. Built in the open, one tutorial at a time.

---

Part of the [Goosos Quantitative Trading Lab](https://goosos.com).
