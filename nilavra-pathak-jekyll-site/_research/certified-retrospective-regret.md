---
layout: page
title: "Certified Retrospective Regret"
summary: "Auditing marketing allocation decisions using constraint-faithful hindsight oracles."
---

This project develops a framework for measuring how much value may have been left on the table by a realized allocation policy.

The core idea is to compare a historical allocation against a model-based hindsight oracle that respects the same practical constraints: budget, stability, support, and operational feasibility. Instead of asking what an unconstrained optimizer would have done, the framework asks what better allocation was feasible under the same regime.

Key themes include:

- Response-surface estimation.
- Stability-constrained oracle construction.
- Monte Carlo uncertainty propagation.
- Retrospective policy scoreboarding.
- Regret distributions and probability-of-improvement summaries.

The goal is to provide a practical audit layer for allocation systems when live experimentation is limited, expensive, or infeasible.
