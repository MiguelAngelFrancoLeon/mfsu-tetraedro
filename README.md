# MFSU-Tetraedro / Tetrahedral Emergent Gravity (TEG)

**Framework:** Unified Fractal-Stochastic Model (MFSU) + Tetrahedral Emergent Gravity (TEG)

**Core axiom:** The quantum vacuum in ℝ³ selects tetrahedral network coordination `z_fund = 4` by maximising holographic entropy density among all Platonic solids.

---

## Algebraic derivation chain (zero fitted parameters)
z_fund = 4 → D_eff = ln 8 ≈ 2.079 → σ_UV = 0.3263 → N_bits = 3 (exact) → σ_eff = 0.1088
plain
Copy

**Empirical confirmation:** 171 SPARC galaxies, RMSE = 0.152 dex, σ_eff confirmed to 0.72% with zero fitting.

---

## Z-sweep validation (175 SPARC galaxies)

![TEG z-sweep](fig_zsweep.png)

**Result:** `z = 4` (tetrahedron) achieves minimum RMSE with σ_eff fully derived at each z — zero fitting anywhere.

| z | Geometry | σ_eff | RMSE (dex) | Δ vs z=4 |
|---|----------|-------|------------|----------|
| 3 | Triangle | 0.090 | 0.183 | +20.4% |
| **4** | **Tetrahedron** | **0.109** | **0.152** | **baseline** |
| 5 | Trigonal bipyramid | 0.131 | 0.159 | +4.6% |
| 6 | Octahedron | 0.156 | 0.181 | +19.1% |
| 8 | Cube | 0.221 | 0.229 | +50.7% |

**Interpretation:** Only z = 4 yields N_bits = 3 = dim(ℝ³) as exact integer. The empirical minimum coincides with the geometric first-principles selection.

---

## Key documents

| Document | DOI | Description |
|---|---|---|
| **TEG Vol. 7** (full derivation) | [10.5281/zenodo.19479542](https://doi.org/10.5281/zenodo.19479542) | Axiom, algebraic chain, SPARC validation, 8 open problems |
| **TEG Predictions** (accessible summary) | [10.5281/zenodo.20320039](https://doi.org/10.5281/zenodo.20320039) | Euclid/DESI falsifiable predictions with thresholds |
| **MFSU Vol. 5** (TEG-MFSU unification) | [10.5281/zenodo.16316882](https://doi.org/10.5281/zenodo.16316882) | Central dynamical equation, γ = σ_eff², CMB predictions |

---

## Quick start — reproduce in 5 minutes

```bash
# Clone repository
git clone https://github.com/MiguelAngelFrancoLeon/mfsu-tetraedro.git
cd mfsu-tetraedro

# Download SPARC data from http://astroweb.cwru.edu/SPARC/
# Place in ./SPARC/ directory

# Run z-sweep validation
python sparc_zsweep.py ./SPARC/
Expected output: z = 4 achieves minimum RMSE with σ_eff(z) fully derived at each z — zero fitting at any step.
Falsifiable predictions
Table
Prediction	Value	Test	Timeline
Weak-lensing shear excess	+5% at ℓ > 10⁴	Euclid	2027
Central void density deficit	−8% at r < 0.3 r_void	DESI	2025–2027
Anomalous diffusion exponent	t^0.962	NIST TN 2279	Now
CMB spectral slope	−ln 8 ≈ −2.079	Planck ℓ < 30	Now
Algebraic conjecture (Open Problem 5)
Holographic codimension ∂ = 3 − ln 8 ≈ 0.921 suggests:
plain
Copy
H₀^TEG ≈ H₀^CMB / √∂ ≈ 67.4 / √0.92056 ≈ 70.3 km/s/Mpc
Numerically consistent with CCHP 2025 (70.39 ± 1.22 km/s/Mpc, Freedman et al.). Not claimed as prediction — requires derivation of full TEG cosmological action.
Framework status
Table
Element	Status	Origin
z_fund = 4	Derived from holographic entropy maximisation	Tetrahedral axiom
D_eff = ln 8	Algebraic identity	Orientation duality
σ_eff = 0.1088	Theorem (S₃-symmetry + max entropy)	Confirmed: SPARC 0.72%
d_s = ln 8	Derived from EPRL intertwiner structure	dim(H_int^(4)) = 2, causal rigidity
γ = σ_eff²	Strong conjecture (3 independent arguments)	Pending: OP.9 verification
H₀ ≈ 70.3	Algebraic conjecture	Pending: OP.5 cosmological action
Open problems: 8 documented with full transparency (see TEG Vol. 7, Section 10).
What TEG is / is not
TEG is: A phenomenological framework for galactic dynamics with geometric derivation chain and falsifiable predictions.
TEG is not: A complete theory of everything. Not validated at galaxy cluster or full cosmological scales. Eight open problems explicitly documented.
Contact
Miguel Angel Franco Leon
Independent researcher
ORCID: 0009-0003-9492-385X
Zenodo: https://zenodo.org/communities/mfsu-teg
Citation
bibtex
Copy
@misc{francoleon2026teg,
  author = {Franco Leon, Miguel Angel},
  title = {Tetrahedral Emergent Gravity (TEG): Algebraic Derivation of the Effective Vacuum Dimension, Jeans Radius, and Holographic Codimension from a Single Geometric Axiom},
  year = {2026},
  doi = {10.5281/zenodo.19479542},
  url = {https://doi.org/10.5281/zenodo.19479542}
}
License
CC BY 4.0 — Free use with attribution.
Reproducibility code runs in < 5 minutes on public SPARC dataset.
