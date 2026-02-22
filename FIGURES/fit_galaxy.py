"""
TEG — Single galaxy rotation curve fitting and plotting
Reproduces Figure 1 of TEG v1.1 paper.
Zenodo: https://zenodo.org/records/18729743

Usage:
    python fit_galaxy.py NGC3198_rotmod.dat
    python fit_galaxy.py NGC3198_rotmod.dat --plot
"""

import numpy as np
import argparse
import os
from teg_core import (load_sparc, v_bar, v_vac, v_total,
                      rmse_dex, SIGMA_EFF)


def fit_galaxy(filepath, plot=False):
    """
    Fit TEG v1.1 to a single SPARC galaxy.
    sigma_eff = 0.1088 (derived, not fitted).

    Parameters
    ----------
    filepath : str  — path to *_rotmod.dat file
    plot     : bool — show rotation curve plot

    Returns
    -------
    dict with RMSE baseline and v1.1 results
    """
    data = load_sparc(filepath)
    if data is None:
        raise ValueError(f"Could not load {filepath}")

    r, Vo, eV, Mb, Vbar = data
    name = os.path.basename(filepath).replace('_rotmod.dat', '')

    # TEG predictions (zero fitting — sigma_eff fully derived)
    Vb_pred = v_bar(r, Mb)
    Vv_pred = v_vac(r, Mb[-1], r[-1])
    Vt_pred = np.sqrt(Vb_pred**2 + Vv_pred**2)

    rm_base = rmse_dex(Vo, Vb_pred)
    rm_v11  = rmse_dex(Vo, Vt_pred)
    impr    = (rm_base - rm_v11) / rm_base * 100

    print(f"\n{'─'*50}")
    print(f"Galaxy:       {name}")
    print(f"log10(Mb):    {np.log10(Mb[-1]):.2f}  M_sun")
    print(f"r_max:        {r[-1]:.1f}  kpc")
    print(f"N points:     {len(r)}")
    print(f"sigma_eff:    {SIGMA_EFF:.4f}  (derived, not fitted)")
    print(f"{'─'*50}")
    print(f"RMSE baseline:  {rm_base:.4f} dex")
    print(f"RMSE + M_vac:   {rm_v11:.4f} dex")
    print(f"Improvement:    {impr:+.1f}%")
    print(f"{'─'*50}")

    if plot:
        try:
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt

            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9),
                                            gridspec_kw={'height_ratios': [2, 1]})

            ax1.errorbar(r, Vo, yerr=eV, fmt='ko', ms=4, capsize=2.5,
                         label='Observed (SPARC)', zorder=6)
            ax1.plot(r, Vbar, 'b:', lw=1.5, label='Baryons only', alpha=0.6)
            ax1.plot(r, Vb_pred, 'r--', lw=2,
                     label=f'TEG baseline  RMSE={rm_base:.3f} dex')
            ax1.plot(r, Vt_pred, color='darkorange', lw=2.5,
                     label=f'TEG + Mvac  RMSE={rm_v11:.3f} dex')
            ax1.fill_between(r, Vb_pred, Vt_pred, alpha=0.18,
                             color='orange', label='Mvac contribution')
            ax1.set_ylabel('V (km/s)', fontsize=12)
            ax1.set_title(f'{name}  |  log Mb = {np.log10(Mb[-1]):.1f} M_sun\n'
                          f'sigma_eff = {SIGMA_EFF:.4f} (derived)',
                          fontsize=11, fontweight='bold')
            ax1.legend(fontsize=8.5)
            ax1.grid(True, alpha=0.2)
            ax1.set_xlim(left=0)

            res_base = np.where(Vb_pred > 0,
                                np.log10(Vo / np.where(Vb_pred > 0, Vb_pred, 1)),
                                np.nan)
            res_v11  = np.where(Vt_pred > 0,
                                np.log10(Vo / np.where(Vt_pred > 0, Vt_pred, 1)),
                                np.nan)
            ax2.axhline(0, color='k', lw=0.8, ls='--')
            ax2.fill_between([r.min(), r.max()], -0.1, 0.1,
                             alpha=0.1, color='green')
            ax2.scatter(r, res_base, c='red', s=28, label='Baseline', alpha=0.8)
            ax2.scatter(r, res_v11, c='darkorange', s=28, label='+Mvac', alpha=0.9)
            ax2.set_xlabel('Radius (kpc)', fontsize=12)
            ax2.set_ylabel('log10(Vobs/Vpred)', fontsize=11)
            ax2.set_title('Residuals  (green band = ±0.1 dex)', fontsize=10)
            ax2.legend(fontsize=9)
            ax2.set_xlim(left=0)
            ax2.set_ylim(-0.55, 0.55)
            ax2.grid(True, alpha=0.2)

            plt.tight_layout()
            outfile = f'{name}_TEG_fit.png'
            plt.savefig(outfile, dpi=150, bbox_inches='tight')
            print(f"Plot saved: {outfile}")
        except ImportError:
            print("matplotlib not available — skipping plot.")

    return {'name': name, 'rmse_base': rm_base, 'rmse_v11': rm_v11,
            'improvement_pct': impr}


def main():
    parser = argparse.ArgumentParser(
        description='Fit TEG v1.1 to a single SPARC galaxy.')
    parser.add_argument('filepath', type=str,
                        help='Path to *_rotmod.dat file.')
    parser.add_argument('--plot', action='store_true',
                        help='Generate rotation curve plot.')
    args = parser.parse_args()
    fit_galaxy(args.filepath, plot=args.plot)


if __name__ == '__main__':
    main()
