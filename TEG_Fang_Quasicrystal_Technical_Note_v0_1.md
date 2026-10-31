> **Preliminary draft v0.1 — work in progress; content subject to substantial revision**

# Tetrahedral Emergent Gravity: A Candidate Topological Realization from an Icosahedral Tetrahedral Quasicrystal

**Miguel Ángel Franco León**
Independent Researcher · ORCID: [0009-0003-9492-385X](https://orcid.org/0009-0003-9492-385X)

31 October 2026

---

## Abstract

This preliminary technical note examines whether the icosahedral packing of regular tetrahedra constructed by Fang et al. ([arXiv:1311.3994](https://arxiv.org/abs/1311.3994)) can serve as a candidate topological realization of the tetrahedral coordination axiom ($z = 4$) of Tetrahedral Emergent Gravity (TEG). The network of tetrahedron centers is four-connected, with published packing density $\varphi \approx 0.59783$ and bond lengths ranging from 0.437 to 0.749 (ratio 1.714). The authors themselves state that the structure cannot be considered physically as 4-coordinated because of this broad bond-length distribution. We record the packing deficit relative to denser known packings, note the existence of phason flips on prolate faces, and list the open questions that separate this geometric candidate from a derived contribution to galactic dynamics. A possible saturating multiplicative factor is mentioned only as an illustration of scale issues; it is not advanced as a prediction. The note is a candidate topological observation plus an explicit list of gaps.

---

## 1. Introduction

Tetrahedral Emergent Gravity (TEG) selects tetrahedral coordination $z_{\text{fund}} = 4$ by maximising holographic entropy density among the Platonic solids. From this single axiom it derives algebraically $D_{\text{eff}} = \ln 8$, $\sigma_{\text{eff}} \approx 0.1088$, and a vacuum profile that has been tested on the SPARC sample (Franco León, Zenodo DOIs [10.5281/zenodo.18729743](https://doi.org/10.5281/zenodo.18729743) and subsequent versions). The present draft asks only whether a published quasicrystalline packing supplies a four-connected geometric substrate for that coordination number. No improvement of the SPARC fit is claimed.

---

## 2. The Fang et al. packing

Fang, Kovacs, Sadler & Irwin ([arXiv:1311.3994](https://arxiv.org/abs/1311.3994)) construct an icosahedral quasicrystal of regular tetrahedra. The network of tetrahedron centers is four-connected. The authors state explicitly:

> "the structure cannot be considered physically as 4-coordinated, due to the excessively high ratio between the longest and shortest bonds stemming from each tetrahedron center."

Bond lengths range from 0.437 to 0.749 (units of the tetrahedron edge length), ratio 1.714. A golden twist reduces the number of distinct plane classes from 190 to 10. Phason degrees of freedom exist in the form of flips of three tetrahedra on faces of the prolate rhombohedra. The relative frequency of prolate to oblate rhombohedra is the golden ratio.

The realization of the TEG axiom is therefore topological (four-connectedness of the center network) and not metrically uniform. In TEG the quantities $D_{\text{eff}} = \ln 8$ and $\sigma_{\text{eff}}$ are derived from the coordination number $z = 4$ under the assumption of a homogeneous network; they do not automatically inherit metric uniformity of bond lengths. Whether the broad length distribution of the Fang network modifies those algebraic results is an open question.

Haji-Akbari et al. (*Nature* 2009) obtained a dodecagonal quasicrystal of hard tetrahedra at packing fraction $\approx 0.83$ by Monte Carlo simulation. The Fang structure is a geometric construction of different symmetry and lower density; it has not been shown to be selected by entropy.

---

## 3. Packing deficit

Relative to the densest known tetrahedral packing of Chen, Engel & Glotzer ($\approx 0.856$), the absolute packing difference is $0.856 - 0.59783 \approx 0.258$. Relative to a reference value of 0.85 the absolute difference is $\approx 0.252$. These figures characterise geometric frustration. They do not by themselves determine a correction to any macroscopic roughness parameter of TEG.

---

## 4. On a possible multiplicative factor (illustrative only)

A saturating factor of the form

$$
1 + \varepsilon \cdot \frac{x}{1 + x}, \qquad x = \frac{r}{R_C},
$$

with $R_C$ identified with the Jeans radius of TEG ($\approx 0.62$ kpc), may be contemplated. With $\varepsilon$ of order 0.03 the maximum correction is $\approx 3\,\%$ in acceleration ($\approx 1.5\,\%$ in velocity). For $R_C = 0.62$ kpc the factor $x/(1+x)$ itself rises from $\approx 0.3$ at $r = 0.3$ kpc to $\approx 0.9$ at $r = 5$ kpc, so it is not fully saturated on the inner SPARC points; the total effect remains $\leq 3\,\%$, below typical observational scatter, and is degenerate with $a_0$ and with stellar mass-to-light ratios. No quantitative rule is given that maps the packing deficit $\approx 0.25$–$0.30$ onto $\varepsilon \approx 0.03$; the latter is simply a small assumed value. Because the factor produces no observationally distinguishable signature under these choices, it is recorded only as an illustration of the scale-separation problem and is not advanced as a prediction.

---

## 5. Effective stress-energy (conjecture)

The phonon elasticity of icosahedral quasicrystals is isotropic at long wavelengths (Lubensky, Ramaswamy & Toner, *Phys. Rev. B* 32, 7444, 1985; see also Levine et al., *Phys. Rev. Lett.* 54, 1520, 1985). This is a necessary condition for a macroscopic isotropic limit. In principle the packing deficit and prolate phason flips could source a geometric contribution to the effective stress-energy. Writing $T_{\mu\nu} = \delta F / \delta g^{\mu\nu}$, however, requires that the free energy be a functional of the spacetime metric. A material elastic energy is not automatically of that form. The conventional factor $-2/\sqrt{-g}$, an equation of state, and covariant conservation would all need to be established. At present the tensor remains a conjecture.

---

## 6. Open questions

The positive content of this draft is a single literature-based observation: a published four-connected quasiperiodic network of tetrahedron centers exists. The gaps that remain are:

1. whether the algebraic quantities of TEG ($D_{\text{eff}}$, $\sigma_{\text{eff}}$) depend only on topological coordination $z = 4$ or also on metric uniformity of bond lengths;
2. a controlled coarse-graining argument linking the microscopic network to any macroscopic galactic scale;
3. a quantitative relation, if any, between packing deficit and a correction to acceleration or roughness;
4. a properly defined geometric stress-energy contribution satisfying the Einstein equations and conservation; and
5. quantitative re-evaluation on the public SPARC sample (Lelli, McGaugh & Schombert, *Astron. J.* 152, 157, 2016), which under present choices is expected to show only a small, degenerate rescaling.

---

## Status of claims

| Item | Status |
|---|---|
| Four-connected center network (Fang et al.) | Taken from literature |
| Packing density $\varphi \approx 0.59783$ and bond range | Taken from literature |
| Identification with TEG $z = 4$ axiom | Conjectural (topological only) |
| $\varepsilon \approx 0.03$ multiplicative factor | Heuristic illustration only |
| Effective stress-energy tensor | Open problem / conjecture |
| Coarse-graining to galactic scales | Open problem |

---

## References

1. Fang, F., Kovacs, J., Sadler, G. & Irwin, K. (2014). An Icosahedral Quasicrystal as a Packing of Regular Tetrahedra. *Acta Phys. Pol. A* **126**, 458. [arXiv:1311.3994](https://arxiv.org/abs/1311.3994).
2. Franco León, M. Á. Tetrahedral Emergent Gravity series. Zenodo DOIs [10.5281/zenodo.18729743](https://doi.org/10.5281/zenodo.18729743) and subsequent versions.
3. Haji-Akbari, A. et al. (2009). Disordered, quasicrystalline and crystalline phases of densely packed tetrahedra. *Nature* **462**, 773.
4. Chen, E. R., Engel, M. & Glotzer, S. C. (2010). Dense crystalline dimer packings of regular tetrahedra. *Discrete Comput. Geom.* **44**, 253.
5. Lubensky, T. C., Ramaswamy, S. & Toner, J. (1985). Hydrodynamics of icosahedral quasicrystals. *Phys. Rev. B* **32**, 7444.
6. Levine, D. et al. (1985). Elasticity and Dislocations in Pentagonal and Icosahedral Quasicrystals. *Phys. Rev. Lett.* **54**, 1520.
7. Lelli, F., McGaugh, S. S. & Schombert, J. M. (2016). SPARC: Mass models for 175 disk galaxies with Spitzer photometry and accurate rotation curves. *Astron. J.* **152**, 157.
8. Newman, M. E. J. & Henley, C. L. (1995). Phason elasticity of a three-dimensional quasicrystal. *Phys. Rev. B* **52**, 6386.
