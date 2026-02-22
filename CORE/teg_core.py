"""
TEG — Tetrahedral Emergent Gravity
Core implementation matching paper TEG v1.1
Zenodo: https://zenodo.org/records/18729743

Author: Miguel Ángel Franco León
License: MIT
"""

import numpy as np

# ── Derived constants (zero free parameters) ──────────────────
PHI      = np.log(4)                        # ln 4 ≈ 1.3863  holographic amplification
D_EFF    = np.log(8)                        # ln 8 ≈ 2.0794  effective Hausdorff dimension
LN2      = np.log(2)                        # ln 2 ≈ 0.6931  universal holographic bit
SIGMA_UV = 2 * np.log(1.5) / np.log(12)    # ≈ 0.3263       geometric frustration bound
N_BITS   = np.log(8) / np.log(2)           # = 3 exact      spatial dimensions
SIGMA_EFF = SIGMA_UV / N_BITS              # ≈ 0.1088       derived-and-confirmed parameter

# ── Physical scales ───────────────────────────────────────────
G     = 4.302e-6   # kpc (km/s)² / M_sun
M_J   = 1e6        # M_sun  — Jeans mass reference
N0    = 1.5        # roughness saturation scale
R_REF = 1.0        # kpc   — unit-fixing convention

# ── Verification (run once at import) ─────────────────────────
assert abs(np.log(8) - np.log(4) - np.log(2)) < 1e-12, "Holographic bit identity failed"
assert abs(N_BITS - 3.0) < 1e-12, "N_bits must be exactly 3"


def sigma_eff_z(z, z_pack=12):
    """
    Fully derived sigma_eff for coordination number z.
    sigma_eff(z) = sigma_UV(z) / N_bits(z)

    Parameters
    ----------
    z : int or float
        Vacuum coordination number to test.
    z_pack : int
        Kissing number upper bound (default 12).

    Returns
    -------
    float
        Derived roughness parameter for this z.
    """
    sigma_uv = 2 * np.log(z_pack / (z_pack - z)) / np.log(z_pack)
    n_bits   = np.log(2 * z) / np.log(2)
    return sigma_uv / n_bits


def F(N):
    """
    Roughness saturation function.
    F(N) = 1 - exp(-N / N0),  N = log10(M_b / M_J)
    """
    return 1.0 - np.exp(-N / N0)


def v_bar(r, Mb, sig=SIGMA_EFF):
    """
    Baryonic rotation velocity from TEG baseline equation (Eq. 15).

    V²_bar(r) = G·M_b(r)/r · Phi · (1 - sig·F(N)/(1+sig·F(N))) · (r/r_ref)^((D_eff-2)/2)

    Parameters
    ----------
    r  : array_like  — radii in kpc
    Mb : array_like  — enclosed baryonic mass in M_sun (same length as r)
    sig: float       — roughness parameter (default: derived SIGMA_EFF)

    Returns
    -------
    ndarray  — circular velocity in km/s
    """
    N    = np.log10(max(Mb[-1], 1.0) / M_J)
    fN   = F(N)
    ampl = PHI * (1 - sig * fN / (1 + sig * fN)) * (r / R_REF) ** ((D_EFF - 2) / 2)
    return np.sqrt(np.maximum(G * Mb / r * ampl, 0.0))


def v_vac(r, Mb_tot, r_max):
    """
    Vacuum entropy contribution (Eq. 17).

    V²_vac(r) = G · ln2 · M_b,tot · r² / r_max³

    Physical origin: bulk entropy D_V = ln8 acting on the free
    tetrahedral network in the galaxy exterior. Coefficient ln2
    is the universal holographic bit (D_V - D_A), derived not fitted.

    Parameters
    ----------
    r      : array_like — radii in kpc
    Mb_tot : float      — total baryonic mass in M_sun
    r_max  : float      — outermost observed radius in kpc

    Returns
    -------
    ndarray — vacuum velocity contribution in km/s
    """
    return np.sqrt(np.maximum(G * LN2 * Mb_tot * r**2 / r_max**3, 0.0))


def v_total(r, Mb, sig=SIGMA_EFF):
    """
    Total predicted rotation velocity (Eq. 18).

    V²_total = V²_bar + V²_vac

    Parameters
    ----------
    r  : array_like — radii in kpc
    Mb : array_like — enclosed baryonic mass profile in M_sun
    sig: float      — roughness parameter (default: derived)

    Returns
    -------
    ndarray — total circular velocity in km/s
    """
    Vb = v_bar(r, Mb, sig)
    Vv = v_vac(r, Mb[-1], r[-1])
    return np.sqrt(Vb**2 + Vv**2)


def rmse_dex(V_obs, V_pred):
    """
    Root mean square error in logarithmic units (dex).

    RMSE = sqrt(mean(log10(V_obs/V_pred)²))

    Parameters
    ----------
    V_obs  : array_like — observed velocities
    V_pred : array_like — predicted velocities

    Returns
    -------
    float — RMSE in dex
    """
    mask = V_pred > 0
    if mask.sum() < 3:
        return 999.0
    return np.sqrt(np.mean(np.log10(V_obs[mask] / V_pred[mask])**2))


def load_sparc(filepath):
    """
    Load a SPARC rotation curve file (*_rotmod.dat).

    Returns
    -------
    tuple (r, V_obs, errV, Mb, V_bar) or None if file is invalid.
    Columns: r[kpc], Vobs[km/s], errV[km/s], Vgas, Vdisk, Vbul
    Mb = enclosed baryonic mass computed from quadrature sum.
    """
    try:
        d = np.loadtxt(filepath, comments='#')
        if d.ndim < 2 or len(d) < 5:
            return None
        r   = d[:, 0]
        Vo  = d[:, 1]
        eV  = d[:, 2]
        Vg  = d[:, 3]
        Vd  = d[:, 4]
        Vb_ = d[:, 5]
        Mb  = np.maximum(Vg**2 + Vd**2 + Vb_**2, 0.0) * r / G
        Vbar = np.sqrt(np.maximum(Vg**2 + Vd**2 + Vb_**2, 0.0))
        mask = (r > 0) & (Vo > 0) & (Mb > 0)
        if mask.sum() < 5:
            return None
        return r[mask], Vo[mask], eV[mask], Mb[mask], Vbar[mask]
    except Exception:
        return None
