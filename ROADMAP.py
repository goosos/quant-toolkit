"""
Placeholder modules — one per upcoming tutorial.

Each file documents what the module WILL do and which tutorial
will build it. This is the roadmap, in code form.
"""

# validation.py — Part 2: Walk-Forward Analysis
#   walk_forward_split(price, n_splits, train_size, test_size)
#   Expanding/rolling windows. Never test on data you optimized on.

# overfitting.py — Part 4: PBO & Deflated Sharpe
#   deflated_sharpe(returns, n_trials)
#   probability_of_backtest_overfitting(returns_splits)
#   Penalize results for the number of configurations you tried.

# costs.py — Part 6: Slippage & Commissions
#   CostModel(fees, slippage, market_impact)
#   Realistic cost modeling beyond flat percentages.

# sizing.py — Part 7: Kelly Criterion
#   kelly_fraction(win_rate, win_loss_ratio)
#   Position sizing: how much to bet, not just when.

# data.py — Part 9: Lookahead & Survivorship Bias
#   check_lookahead(signals, price)
#   Data validation guards: the biases that silently inflate results.

# metrics.py — Part 10: Sharpe vs Sortino
#   sortino(returns), calmar(returns), omega(returns)
#   Beyond Sharpe: the full performance metric toolkit.
