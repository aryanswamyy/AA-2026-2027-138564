# AA-2026-2027-138564 — P06: k-Vertex Cover Decision

**Student:** Aryan Swami  
**Student number / benchmark seed:** 138564  
**Course:** Advanced Algorithms, 2026/2027  
**Project:** 1 — Exhaustive Search & Greedy Heuristics

## Problem

Given an undirected graph `G = (V, E)` and an integer `k`, decide whether there is a vertex cover `C` with `|C| <= k`. A vertex cover touches every edge: each edge has at least one endpoint in `C`.

## Repository layout

- `src/` — problem definition, exact solver, greedy heuristic, graph I/O, and utilities.
- `experiments/` — reproducible benchmark runner.
- `data/graphs/handmade/` — small hand-crafted graphs with manually verified answers.
- `data/graphs/synthetic/` — generated benchmark graphs.
- `data/results.csv` — benchmark results using the project schema.
- `notebooks/` — analysis and plots.
- `tests/` — correctness checks against handmade instances.
- `docs/p1/` — report, slides, and live demo notes.

## Planned implementation

1. Implement an exact decision solver that returns as soon as it finds a cover of size at most `k`.
2. Implement a deterministic greedy cover heuristic and use its result to answer the decision question.
3. Create 1–2 handmade graphs with at most 8 vertices, solve them by hand, and record the ground truth.
4. Generate undirected graphs at densities 12.5%, 25%, 50%, and 75%, using seed `138564` and storing distinct integer 2D coordinates as node attributes.
5. Measure runtime with `time.perf_counter()`, count basic operations, apply a per-run timeout, and log results in `data/results.csv`.
6. Analyze runtime and decision results; prepare the report (maximum 8 pages), presentation, and demo notes.

For this decision problem, report whether the greedy cover has at most `k` vertices, its cover size, and its runtime. The exact solver provides the correctness reference.

## Status

Repository structure is set up. Solver code, handmade instances, experiments, and final deliverables will be added next.
