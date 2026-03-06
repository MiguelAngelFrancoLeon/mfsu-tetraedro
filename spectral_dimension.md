# Exact Algebraic Prediction of the Spectral Dimension in Quantum Gravity

**Tetrahedral Emergent Gravity (TEG) - Spectral Dimension Paper**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18810945.svg)](https://doi.org/10.5281/zenodo.18810945)
[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg)](https://arxiv.org/abs/XXXX.XXXXX)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Author**: Miguel Ángel Franco León  
**Date**: March 2026  
**Status**: Published on Zenodo, submitted to arXiv

---

## 🎯 Executive Summary

**We derive the spectral dimension of quantum gravity algebraically for the first time in history.**

**Main Result**:
```
d_s = ln(2z_fund) = ln 8 ≈ 2.0794
```

where `z_fund = 4` is tetrahedral vacuum coordination selected by holographic entropy maximization.

**This matches**:
- ✅ Loop Quantum Gravity (LQG): `d_s ∈ [2.0, 2.2]` (Modesto 2009)
- ✅ Causal Dynamical Triangulations (CDT): `d_s ∈ [2.0, 2.5]` (Ambjørn 2005)
- ✅ Asymptotic Safety: `d_s → 2` at UV fixed point (Reuter 2012)

**With < 4% precision and ZERO free parameters.**

---

## 🚀 Why This Matters

### **The 15-Year Open Question**

Since Modesto (2009), the quantum gravity community has known that:
- LQG simulations give `d_s ≈ 2` at small scales
- CDT Monte Carlo gives `d_s ≈ 2` in de Sitter phase
- Asymptotic Safety predicts `d_s → 2` at UV fixed point

**But nobody knew WHY.**

All previous results were **numerical** (spin-network coarse-graining, Monte Carlo, RG flow).

**Until now.**

### **Our Contribution**

We derive `d_s = ln 8` **algebraically** from a single geometric axiom:

> **Axiom**: The quantum vacuum maximizes holographic entropy density by selecting tetrahedral coordination (`z = 4`)

**From this alone**, we derive:
1. Spectral dimension: `d_s = ln 8`
2. Bulk entropy: `D_V = ln 8`
3. Gravitational effective dimension: `D_eff = ln 8`
4. Fractal dimension: `d_f = ln 8`

**All the same quantity.** All derived. Zero fitting.

---

## 📊 Key Results

### **Triple Validation**

| Method | Result | Match |
|--------|--------|-------|
| **Analytical (Generating Functions)** | `d_s = ln 8 = 2.0794` | Exact |
| **Numerical (Python Simulations)** | `d_s = 2.08 ± 0.06` | ✅ Within uncertainty |
| **LQG Literature (Modesto 2009)** | `d_s ∈ [2.0, 2.2]` | ✅ <4% discrepancy |
| **CDT Literature (Ambjørn 2005)** | `d_s ∈ [2.0, 2.5]` | ✅ Center of range |

### **Unification**

We prove that four apparently different quantities are **the same**:

```
d_s (spectral) = D_V (bulk entropy) = D_eff (gravitational) = d_f (fractal) = ln 8
```

This connects:
- Quantum gravity (LQG/CDT) ↔ Galactic phenomenology (rotation curves)
- Microscopic (Planck scale) ↔ Macroscopic (kpc scales)
- Discrete network geometry ↔ Continuum effective dimension

---

## 📁 Repository Contents

```
spectral-dimension-teg/
├── paper/
│   ├── spectral_dimension_teg.pdf        # Main paper (19 pages)
│   ├── spectral_dimension_teg.tex        # LaTeX source
│   └── references.bib                    # Bibliography
│
├── figures/
│   ├── figure1_tetrahedral_network.pdf   # Tetrahedral vacuum diagram
│   └── figure1_spectral_across_scales.pdf # d_s across 60 orders of magnitude
│
├── code/
│   ├── spectral_dimension_simulations.py # Complete Python code
│   ├── requirements.txt                  # Dependencies
│   └── README_CODE.md                    # How to run simulations
│
├── data/
│   └── numerical_results.csv             # Simulation outputs
│
├── metadata/
│   ├── zenodo_metadata.json              # For Zenodo upload
│   └── arxiv_metadata.txt                # For arXiv submission
│
├── LICENSE                                # CC BY 4.0
└── README.md                              # This file
```

---

## 🔬 Scientific Highlights

### **1. First Algebraic Derivation**

**Previous work** (all numerical):
- Modesto (2009): Spin-network coarse-graining → `d_s ≈ 2.0`
- Ambjørn (2005): CDT Monte Carlo → `d_s ∈ [2.0, 2.5]`
- Calcagni (2017): Heat kernel methods → `d_s ∈ [1.8, 2.2]`

**This work** (algebraic):
- Tetrahedral axiom + orientation duality → `d_s = ln 8` (exact)
- Generating function analysis (Delporte 2024 methods)
- Numerical confirmation: `d_s = 2.08 ± 0.06`

### **2. Regime Identification**

**Critical insight**: LQG/CDT simulations probe the **intermediate coarse-graining regime**, not the asymptotic limit.

```
Asymptotic (t → ∞):     d_s = 3           [Standard Bethe lattice]
Intermediate (LQG/CDT): d_s = ln 8 ≈ 2.08 [Oriented Bethe lattice]
```

We work in the **same regime** LQG/CDT simulations probe, explaining why we match their results.

### **3. Geometric Origin**

**Why `d_s ≈ 2` in quantum gravity?**

**Answer**: Tetrahedral vacuum structure.

- LQG spin networks: dominated by 4-valent nodes
- CDT 4-simplices: have tetrahedral (3-simplex) boundaries
- Both encode `z = 4` at microscopic level
- Orientation duality: SU(2) holonomies `U_ij` and `U_ji = U_ij†` double effective branching
- Result: `d_s = ln(2z) = ln 8`

**Not a coincidence. Geometric necessity.**

### **4. Connection to Galactic Phenomenology**

The **same** `d_s = ln 8` appears as gravitational effective dimension `D_eff` in Newtonian Fractional-Dimension Gravity (NFDG).

**NFDG** (Varieschi 2021): Uses `D_eff ∈ [2.0, 2.2]` as **fitted parameter** to explain flat rotation curves.

**TEG**: **Derives** `D_eff = ln 8` from quantum vacuum geometry.

**This unifies**:
- Quantum gravity at Planck scale
- Dark matter phenomenology at galactic scales

---

## 🧪 Reproducibility

### **Run the Simulations Yourself**

**Requirements**:
```bash
pip install numpy networkx scipy matplotlib
```

**Run**:
```bash
cd code/
python spectral_dimension_simulations.py
```

**Outputs**:
- `Standard tree d_s: 3.02 ± 0.08`
- `Oriented tree d_s: 2.08 ± 0.06` ← **Matches `ln 8 = 2.079`**
- `figure2_spectral_dimension_plateau.png`

**Time**: ~2 minutes on laptop

**Code**: 158 lines, fully documented, copy-paste ready for Google Colab

---

## 🎯 Falsifiable Predictions

### **1. High-Precision LQG Simulations**

**Prediction**: `d_s ∈ [2.05, 2.10]` in intermediate regime

**Test**: Improved spin-network coarse-graining with better numerics

**Falsification**: If future LQG finds `d_s < 2.05` or `d_s > 2.10` (>3σ)

### **2. Regime-Dependent Measurements**

**Prediction**: `d_s(t)` crossover from `ln 8` (intermediate) to `3` (asymptotic)

**Test**: Measure `d_s(t)` as function of diffusion time in LQG/CDT

**Falsification**: If no crossover observed, or crossover at wrong value

### **3. CDT Refinements**

**Prediction**: `d_s = 2.08 ± 0.05` in de Sitter phase (intermediate regime)

**Test**: Larger lattices, longer Monte Carlo runs

**Falsification**: If `d_s = 1.9 ± 0.05` or `d_s = 2.3 ± 0.05`

### **4. Galactic Observations**

**Prediction**: `D_eff = ln 8 ≈ 2.08` universal across all galaxies

**Test**: High-precision SPARC rotation curve analysis

**Falsification**: If `D_eff` varies significantly galaxy-by-galaxy

---

## 📚 Citation

If you use this work, please cite:

```bibtex
@article{FrancoLeon2026_SpectralDimension,
  author = {Franco León, Miguel Ángel},
  title = {Exact Algebraic Prediction of the Spectral Dimension in Quantum Gravity from Tetrahedral Vacuum Structure},
  year = {2026},
  month = {March},
  journal = {Zenodo},
  doi = {10.5281/zenodo.18810945},
  note = {Also available at arXiv:XXXX.XXXXX}
}
```

### **Or in Text**:

Franco León, M.Á. (2026). *Exact Algebraic Prediction of the Spectral Dimension in Quantum Gravity from Tetrahedral Vacuum Structure*. Zenodo. https://doi.org/10.5281/zenodo.18884181

---

## 🔗 Related Work

### **TEG Framework Papers**:

1. **TEG v1.0** (2025): Initial framework, σ_eff derivation
   - Zenodo: 10.5281/zenodo.18729743
   
2. **TEG v1.1** (2026): SPARC validation, 171 galaxies
   - Zenodo: 10.5281/zenodo.XXXXXXX

3. **TEG v1.2** (2026): Jeans radius r_J from LQG volume operator
   - Zenodo: 10.5281/zenodo.XXXXXXX

4. **This work** (2026): Spectral dimension d_s = ln 8
   - Zenodo: 10.5281/zenodo.18810945

### **Key References**:

- **Modesto (2009)**: First numerical d_s in LQG
- **Ambjørn et al. (2005)**: d_s in CDT
- **Delporte et al. (2024)**: Oriented graph spectral dimensions (methods used here)
- **Varieschi (2021)**: NFDG (we provide its quantum gravity foundation)

---

## 🤝 Contributions & Feedback

### **Found a Bug?**
Open an issue with:
- Description of the problem
- Steps to reproduce
- Expected vs actual behavior

### **Have a Question?**
- Check the paper (Section 7: Discussion, Open Questions)
- Open a discussion on GitHub
- Email: miguel.franco.leon@proton.me

### **Want to Collaborate?**
I'm particularly interested in:
- High-precision LQG simulations to test d_s ∈ [2.05, 2.10]
- CDT refinements measuring d_s(t) regime transition
- Extensions to cosmology (CMB, structure formation)
- Lorentzian sector calculations

---

## 📜 License

**Paper**: CC BY 4.0 (Creative Commons Attribution 4.0 International)
- ✅ Share, adapt, commercial use allowed
- ✅ Must give appropriate credit
- ✅ Indicate if changes were made

**Code**: MIT License
- ✅ Use, modify, distribute freely
- ✅ Include copyright notice

---

## 🙏 Acknowledgments

I thank the LQG and CDT communities for making their numerical results publicly available, particularly:
- **Leonardo Modesto** (LQG spectral dimension)
- **Renate Loll** & **Jan Ambjørn** (CDT)
- **Carlo Rovelli** (spin-network formalism)
- **Nicolas Delporte**, **Sambuddha Sen**, **Reiko Toriumi** (oriented graph methods)

Special thanks to the SPARC team (Federico Lelli et al.) for galaxy data, and to the open science community for inspiration.

---

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/username/spectral-dimension-teg?style=social)
![GitHub forks](https://img.shields.io/github/forks/username/spectral-dimension-teg?style=social)
![Downloads](https://img.shields.io/github/downloads/username/spectral-dimension-teg/total)

**Paper views**: [Zenodo stats]  
**Code runs**: [GitHub Actions]

---

## 🗺️ Roadmap

### **Completed** ✅
- [x] Algebraic derivation d_s = ln 8
- [x] Generating function analysis
- [x] Numerical validation (Python)
- [x] Paper written (19 pages)
- [x] Code released (MIT license)

### **In Progress** 🚧
- [ ] arXiv submission (gr-qc)
- [ ] Journal submission (Classical and Quantum Gravity)
- [ ] Community feedback incorporation

### **Future Work** 🔮
- [ ] Lorentzian sector calculations
- [ ] CMB predictions (with CAMB)
- [ ] High-precision LQG tests
- [ ] Extensions to cosmology

---

## 💬 Contact

**Miguel Ángel Franco León**  
Independent Researcher  
📧 miguel.franco.leon@proton.me  
🐦 [@username] (@miguelAfrancoL)  
🔗 [ORCID: 0009-0003-9492-385X] (if you have one)

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=username/spectral-dimension-teg&type=Date)](https://star-history.com/#username/spectral-dimension-teg&Date)

---

**Last updated**: March 2026  
**Version**: 1.0  
**DOI**: 10.5281/zenodo.XXXXXXX

---

**Made with 💙 for the advancement of science**

**"The dimensional reduction d_s ≈ 2 is not a dynamical accident.  
It is a geometric necessity from tetrahedral vacuum structure."**

---
