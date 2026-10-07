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
| `data.py` | [Part 3: Data Cleaning & Alignment](https://github.com/goosos/data-cleaning-tutorial) | ✅ |
| `overfitting.py` | [Part 4: Backtest Overfitting](https://github.com/goosos/overfitting-tutorial) | ✅ |
| `metrics.py` | Part 5: Performance Metrics Deep Dive | 🔲 |
| `costs.py` | Part 6: Slippage & Commissions | 🔲 |
| `sizing.py` | Part 7: Position Sizing | 🔲 |

Parts 8–10 are capstone tutorials (multi-strategy portfolios, parameter robustness,
assembling the full system) — they integrate the modules rather than adding new ones.

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
