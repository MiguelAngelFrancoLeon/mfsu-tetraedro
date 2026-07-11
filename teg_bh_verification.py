#!/usr/bin/env python3
"""
teg_bulge_chameleon_limit.py

TEG vH2 — Appendix (Bulge Chameleon Limit)
Verification of Proposition A.1: GR recovery in the high-density limit
rho/rho_c >> 15.9, applied to the Galactic bulge.

This script performs a THEORETICAL / NUMERICAL verification only.
It does NOT process any Euclid Q2 (EGBS) catalog data. The EGBS survey
(Beaulieu et al. 2026, arXiv:2606.25883) is cited only as motivation for
why the Galactic bulge is a relevant high-density regime to check; no
EGBS photometry is loaded, fit, or compared against here.

The Einasto bulge density profile is taken from Portail et al. 2017
(pre-Euclid, independently published). This script verifies that the
TEG chameleon field Phi_TEG(rho) satisfies Phi_TEG -> 1 (GR exact) at
every radius in that profile, closing a previously undocumented
coverage gap in the low-density-only verification suite (SPARC, App. F).

Author: Miguel Angel Franco Leon
Repository: mfsu-tetraedro
License: same as parent repository
"""

import numpy as np


# ──────────────────────────────────────────────────────────────────────────
# 1. TEG constants (zero free parameters)
# ──────────────────────────────────────────────────────────────────────────

DA = np.log(4)          # surface entropy = ln4
DV = np.log(8)          # volume entropy  = ln8
PARTIAL = 3 - DV         # holographic codimension = 3 - ln8
N0 = 1.5                 # saturation scale (Proposition 7.1)
RHO_TRANSITION = 15.9    # threshold rho/rho_c above which Phi_TEG -> 1

# TEG critical density (from paper, Sec. 4)
RHO_C_SI = 6.78e-26      # g/cm^3
_G_SI = 6.674e-11        # m^3 kg^-1 s^-2
_M_SUN_KG = 1.989e30     # kg
_PC_M = 3.086e16         # m
RHO_C_MSUN_PC3 = RHO_C_SI * 1e3 / _M_SUN_KG * _PC_M ** 3  # Msun/pc^3


def _sanity_check_constants() -> None:
    """Algebraic identities that must hold to machine precision."""
    assert abs(DV / DA - 1.5) < 1e-14, "DV/DA must equal 3/2"
    assert abs(DV / np.log(2) - 3.0) < 1e-14, "DV/ln2 must equal 3"
    assert abs(PARTIAL - (3 - 4 * DV / 4)) < 1e-14, "codimension identity failed"


# ──────────────────────────────────────────────────────────────────────────
# 2. Chameleon field (Proposition 7.1 / Proposition A.1)
# ──────────────────────────────────────────────────────────────────────────

def phi_teg(rho_msun_pc3: np.ndarray, rho_c: float = RHO_C_MSUN_PC3,
            n0: float = N0) -> np.ndarray:
    """
    TEG chameleon amplification factor Phi_TEG(rho).

    Phi_TEG -> ln4  as rho/rho_c -> 0   (diffuse regime, e.g. dwarf galaxies)
    Phi_TEG -> 1    as rho/rho_c -> inf (screened regime, e.g. galactic bulge)

    Parameters
    ----------
    rho_msun_pc3 : array_like
        Local density in Msun/pc^3.
    rho_c : float
        TEG critical density in Msun/pc^3.
    n0 : float
        Saturation scale of Proposition 7.1.

    Returns
    -------
    ndarray
        Phi_TEG evaluated at each input density.
    """
    x = np.asarray(rho_msun_pc3, dtype=float) / rho_c
    f_local = 1.0 - np.exp(-x / n0)
    return 1.0 + (DA - 1.0) * (1.0 - f_local)


# ──────────────────────────────────────────────────────────────────────────
# 3. Bulge density profile (Portail et al. 2017, Einasto form)
#    Independent, pre-Euclid, published parametrization.
# ──────────────────────────────────────────────────────────────────────────

def rho_bulge_einasto(r_kpc: np.ndarray, rho0: float = 100.0,
                       r_s: float = 0.5, n: float = 3.5) -> np.ndarray:
    """
    Einasto density profile for the Milky Way bulge (Portail et al. 2017).

    Parameters
    ----------
    r_kpc : array_like
        Galactocentric radius in kpc.
    rho0 : float
        Central density in Msun/pc^3.
    r_s : float
        Scale radius in kpc.
    n : float
        Einasto index.

    Returns
    -------
    ndarray
        Density in Msun/pc^3.
    """
    r_pc = np.asarray(r_kpc, dtype=float) * 1000.0
    rs_pc = r_s * 1000.0
    d_n = 3 * n - 1 / 3 + 0.0079 / n  # Retana-Montenegro et al. 2012 approx.
    return rho0 * np.exp(-d_n * ((r_pc / rs_pc) ** (1 / n) - 1))


# ──────────────────────────────────────────────────────────────────────────
# 4. Verification routine
# ──────────────────────────────────────────────────────────────────────────

def verify_bulge_chameleon_limit(r_min_kpc: float = 0.05,
                                  r_max_kpc: float = 3.0,
                                  n_points: int = 500,
                                  tol: float = 1e-5) -> dict:
    """
    Verify Proposition A.1 across the radial extent of the Galactic bulge.

    Checks that:
      (a) rho/rho_c exceeds RHO_TRANSITION at every sampled radius, and
      (b) Phi_TEG deviates from 1 by less than `tol` at every sampled radius.

    Returns a dict with the arrays and pass/fail flags, and raises
    AssertionError if either condition fails anywhere in the profile.
    """
    r_arr = np.linspace(r_min_kpc, r_max_kpc, n_points)
    rho_arr = rho_bulge_einasto(r_arr)
    ratio_arr = rho_arr / RHO_C_MSUN_PC3
    phi_arr = phi_teg(rho_arr)
    deviation = np.abs(phi_arr - 1.0)

    threshold_ok = bool(np.all(ratio_arr > RHO_TRANSITION))
    screening_ok = bool(np.all(deviation < tol))

    assert threshold_ok, (
        f"rho/rho_c fails to exceed {RHO_TRANSITION} at some radius in "
        f"[{r_min_kpc}, {r_max_kpc}] kpc -- bulge profile assumption invalid."
    )
    assert screening_ok, (
        f"Phi_TEG deviates from 1 by more than {tol} at some radius -- "
        f"Proposition A.1 not satisfied numerically."
    )

    return {
        "r_kpc": r_arr,
        "rho_msun_pc3": rho_arr,
        "ratio_rho_rhoc": ratio_arr,
        "phi_teg": phi_arr,
        "max_deviation_from_GR": float(deviation.max()),
        "min_ratio_rho_rhoc": float(ratio_arr.min()),
        "threshold_satisfied_everywhere": threshold_ok,
        "screening_satisfied_everywhere": screening_ok,
    }


# ──────────────────────────────────────────────────────────────────────────
# 5. Main
# ──────────────────────────────────────────────────────────────────────────

def main() -> None:
    _sanity_check_constants()
    result = verify_bulge_chameleon_limit()

    print("=" * 62)
    print("TEG vH2 -- Appendix: Bulge Chameleon Limit (Proposition A.1)")
    print("=" * 62)
    print(f"rho_c (TEG)              = {RHO_C_MSUN_PC3:.6f} Msun/pc^3")
    print(f"Threshold rho/rho_c      > {RHO_TRANSITION}")
    print(f"Radial range checked     = 0.05 - 3.0 kpc (Einasto, Portail+2017)")
    print("-" * 62)
    print(f"Min rho/rho_c in profile = {result['min_ratio_rho_rhoc']:.1f}")
    print(f"Max |Phi_TEG - 1|        = {result['max_deviation_from_GR']:.2e}")
    print(f"Threshold satisfied      : {result['threshold_satisfied_everywhere']}")
    print(f"GR recovery satisfied    : {result['screening_satisfied_everywhere']}")
    print("-" * 62)
    print("Sample points:")
    print(f"{'r [kpc]':<10}{'rho [Msun/pc3]':<18}{'rho/rho_c':<14}{'Phi_TEG':<12}")
    for r_target in (0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0):
        idx = int(np.argmin(np.abs(result["r_kpc"] - r_target)))
        print(
            f"{result['r_kpc'][idx]:<10.2f}"
            f"{result['rho_msun_pc3'][idx]:<18.2f}"
            f"{result['ratio_rho_rhoc'][idx]:<14.1f}"
            f"{result['phi_teg'][idx]:<12.8f}"
        )
    print("=" * 62)
    print("STATUS: theoretical/numerical verification only.")
    print("No Euclid Q2 (EGBS) catalog data were used in this script.")
    print("EGBS (Beaulieu et al. 2026, arXiv:2606.25883) is cited in the")
    print("appendix text as motivation for the high-density regime only.")
    print("=" * 62)


if __name__ == "__main__":
    main()
