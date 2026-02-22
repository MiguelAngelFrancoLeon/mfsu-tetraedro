"""
TEG — Z-sweep reproducibility script
Reproduces Table 2 and Figure 3 from TEG v1.1 paper.
Zenodo: https://zenodo.org/records/18729743

Runtime: < 5 minutes on full SPARC (171 galaxies).

Usage:
    python zsweep.py --sparc_dir /path/to/sparc/

Download SPARC data from: http://astroweb.cwru.edu/SPARC/
"""

import numpy as np
import glob
import os
import argparse
from teg_core import load_sparc, v_total, rmse_dex, sigma_eff_z

def run_zsweep(sparc_dir, z_values=None):
    """
    Run z-sweep on all SPARC galaxies with sigma_eff fully derived per z.

    Parameters
    ----------
    sparc_dir : str   — path to folder containing *_rotmod.dat files
    z_values  : list  — coordination numbers to test (default [3,4,5,6,8])

    Returns
    -------
    dict: {z: (sigma_eff, rmse)}
    """
    if z_values is None:
        z_values = [3, 4, 5, 6, 8]

    # Load galaxies
    files = sorted(glob.glob(os.path.join(sparc_dir, '*_rotmod.dat')))
    galaxies = []
    for fp in files:
        data = load_sparc(fp)
        if data is not None:
            galaxies.append(data)
    print(f"Loaded {len(galaxies)} galaxies from {sparc_dir}")

    if len(galaxies) == 0:
        raise ValueError("No galaxies loaded. Check sparc_dir path.")

    results = {}
    print(f"\n{'z':>4}  {'sigma_eff':>10}  {'N_bits':>8}  {'RMSE':>8}  {'Delta':>8}")
    print("  " + "-" * 44)

    best_rmse = np.inf
    for z in z_values:
        sig  = sigma_eff_z(z)
        Ph   = np.log(z)
        De   = np.log(2 * z)
        residuals = []

        for r, Vo, eV, Mb, Vbar in galaxies:
            Vp = v_total(r, Mb, sig)
            m  = Vp > 0
            if m.sum() < 3:
                continue
            residuals.extend(np.log10(Vo[m] / Vp[m]).tolist())

        rmse = np.sqrt(np.mean(np.array(residuals)**2)) if residuals else 999.
        results[z] = (sig, rmse)
        if rmse < best_rmse:
            best_rmse = rmse

    # Print table
    for z in z_values:
        sig, rmse = results[z]
        n_bits = np.log(2 * z) / np.log(2)
        delta  = rmse - best_rmse
        best_marker = " ← BEST" if delta < 1e-9 else ""
        print(f"  {z:>2}  {sig:>10.4f}  {n_bits:>8.3f}  {rmse:>8.4f}  {delta:>+8.4f}{best_marker}")

    best_z = min(results, key=lambda z: results[z][1])
    print(f"\nConclusion: z = {best_z} achieves lowest RMSE.")
    if best_z == 4:
        print("✓ Confirms TEG prediction: z_fund = 4 (tetrahedral vacuum).")
    else:
        print(f"✗ z = {best_z} wins — TEG model must be revised.")

    return results


def main():
    parser = argparse.ArgumentParser(
        description='TEG z-sweep: reproduce Table 2 of TEG v1.1 paper.')
    parser.add_argument('--sparc_dir', type=str, required=True,
                        help='Path to SPARC *_rotmod.dat files.')
    parser.add_argument('--z_values', type=int, nargs='+',
                        default=[3, 4, 5, 6, 8],
                        help='Coordination numbers to test (default: 3 4 5 6 8).')
    args = parser.parse_args()
    run_zsweep(args.sparc_dir, args.z_values)


if __name__ == '__main__':
    main()
