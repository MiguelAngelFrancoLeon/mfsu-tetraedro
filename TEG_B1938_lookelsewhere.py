#!/usr/bin/env python3
"""Look-elsewhere probability for TEG length scales vs B1938+666.

Companion to Franco León, "The dark perturber in JVAS B1938+666 as a
test of Tetrahedral Emergent Gravity: a consistency check and a 5-cell
geometric note" (29 September 2026).

A target radius T is drawn log-uniformly from [Tmin, Tmax]. A candidate
length c is a match if |c/T - 1| < window. Default window = 0.12 is the
relative offset of r_J/4 = 155 pc from the Vegetti disk radius 139 pc.

The reported table uses r_J = 0.619 kpc (TEG v8 Appendix L, H0 = 70,
sigma_eff = 0.1088).
"""
from __future__ import annotations
import argparse
import numpy as np

SIGMA_EFF = 0.1088
D_EFF = float(np.log(8))
PARTIAL = 3.0 - D_EFF
LN2 = float(np.log(2))
Z_FUND = 4
L_PL = 1.616e-35
C = 2.99792458e8
MPC = 3.085677581e22
H0 = 70.0
R_H = C / (H0 * 1e3 / MPC)
R_J_KPC = (L_PL**SIGMA_EFF * R_H ** (1 - SIGMA_EFF)) / (PARTIAL * np.sqrt(np.pi)) / 3.085677581e19
R_J = R_J_KPC * 1000.0  # pc


def families(r_j: float) -> dict[str, np.ndarray]:
    five = np.array([
        r_j,
        r_j * np.sqrt(15) / 4,
        r_j / 4,
        r_j / np.sqrt(15),
        r_j / 3,
    ])
    seven = np.array([
        r_j,
        2 * r_j,
        r_j / Z_FUND,
        r_j * SIGMA_EFF,
        r_j * PARTIAL,
        r_j * (D_EFF - 2),
        r_j * LN2 / Z_FUND,
    ])
    ten = np.unique(np.concatenate([seven, five]))
    rn = r_j / np.arange(1, 11)
    return {"5-cell": five, "all-10": ten, "rJ/n n<=10": rn}


def p_at_least_one(cands, tmin, tmax, window=0.12, n=200_000, seed=0):
    rng = np.random.default_rng(seed)
    T = np.exp(rng.uniform(np.log(tmin), np.log(tmax), n))
    hit = np.zeros(n, dtype=bool)
    for c in cands:
        hit |= np.abs(c / T - 1.0) < window
    return float(hit.mean())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--window", type=float, default=0.12)
    p.add_argument("--n", type=int, default=200_000)
    args = p.parse_args()
    print(f"r_J = {R_J:.4f} pc")
    print(f"window = {args.window}")
    fam = families(R_J)
    ranges = [(10, 1000), (30, 1000), (50, 700)]
    hdr = f"{'range':<16}" + "".join(f"{k:>16}" for k in fam)
    print(hdr)
    for a, b in ranges:
        row = f"{a}-{b} pc".ljust(16)
        for arr in fam.values():
            row += f"{p_at_least_one(arr, a, b, args.window, args.n):16.2f}"
        print(row)


if __name__ == "__main__":
    main()
