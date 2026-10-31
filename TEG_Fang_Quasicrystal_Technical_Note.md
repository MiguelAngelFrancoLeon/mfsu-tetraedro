# Tetrahedral Emergent Gravity with Quasicrystalline Realization: A Technical Note

**Miguel Ángel Franco León**
Independent Researcher
ORCID: [0009-0003-9492-385X](https://orcid.org/0009-0003-9492-385X)

October 31, 2026

---

## Abstract

This technical note extends Tetrahedral Emergent Gravity (TEG) by providing an explicit quasicrystalline realization of its foundational axiom—the selection of tetrahedral coordination ($z = 4$) by the quantum vacuum. Drawing on the icosahedral packing of regular tetrahedra constructed by Fang et al. (2013/2014), we identify a 4-connected network whose packing density and phason degrees of freedom supply a geometric origin for the residual cohesion observed at galactic scales. A saturating correction, derived from the packing deficit and phason density of this network, is proposed that preserves the Newtonian and flat-rotation-curve limits of TEG while anchoring the framework in existing quasicrystal and holographic literature. No new free parameters fitted to rotation-curve data are introduced. The construction is offered as a geometric strengthening of TEG rather than a phenomenological improvement.

---

## 1. Introduction

Tetrahedral Emergent Gravity (TEG) posits that the quantum vacuum in three-dimensional space selects tetrahedral coordination ($z_{\text{fund}} = 4$) because this geometry maximises holographic entropy density among the Platonic solids. From this single axiom, TEG derives algebraically an effective vacuum dimension $D_{\text{eff}} = \ln 8$, an effective roughness $\sigma_{\text{eff}} \approx 0.1088$, and a vacuum mass profile that reproduces observed galactic rotation curves on the SPARC sample with zero parameters fitted to the data. The framework is consistent with the 4-valent nodes of Loop Quantum Gravity and with the effective dimensions reported by Causal Dynamical Triangulations.

The present note supplies a concrete geometric realisation of the $z = 4$ network by embedding it in a quasicrystalline packing already constructed in the literature. The goal is not to improve the numerical fit to rotation curves, but to place the tetrahedral axiom on a firmer microscopic foundation and to connect TEG with the quasicrystal and discrete-holography literature.

---

## 2. Quasicrystalline Realisation of the Tetrahedral Network

Fang, Kovacs, Sadler & Irwin ([arXiv:1311.3994](https://arxiv.org/abs/1311.3994)) construct an icosahedral quasicrystal composed entirely of regular tetrahedra. Two independent decoration procedures—one guided by a three-dimensional slice of the Elser–Sloane four-dimensional quasicrystal and another based on the three-dimensional Ammann tiling—yield the same structure. The network of tetrahedron centres is four-connected, thereby realising the coordination number $z = 4$ of the TEG axiom in a quasiperiodic setting.

The packing density of this network is

$$
\varphi = \frac{65}{16464}\left(208800\sqrt{2} + 64215\sqrt{5} - 45499\sqrt{10} - 294845\right) \approx 0.59783.
$$

Bond lengths between centres range from 0.437 to 0.749 (in units of the tetrahedron edge length), giving a maximum-to-minimum ratio of 1.714. A distinctive phason mechanism is present: on the faces of each prolate rhombohedron, groups of three tetrahedra may flip. The relative frequency of prolate to oblate rhombohedra in the underlying Ammann tiling is the golden ratio $\varphi = (1+\sqrt{5})/2$. A golden twist reduces the number of distinct plane classes from 190 to 10.

This construction is compatible with the entropy-driven formation of quasicrystalline order by hard tetrahedra (Haji-Akbari et al., *Nature* 2009) and with the conformal quasicrystals and holographic foliations studied by Boyle and collaborators. It therefore supplies an explicit microscopic carrier for the tetrahedral vacuum of TEG.

---

## 3. Saturating Geometric Correction

The packing deficit relative to denser known tetrahedral packings ($\approx 0.85$) is $\delta\varphi \approx 0.297$. Combined with the phason density associated with the prolate flips (order $\varphi^{-1} \approx 0.618$), this geometric frustration suggests a small additive correction to the effective roughness of TEG:

$$
\delta\sigma_{QC} \sim 0.03 \quad (\text{range } 0.02\text{–}0.05).
$$

The modified acceleration is written

$$
a(r) = a_N \cdot \nu\!\left(\frac{a_N}{a_0}\right) \cdot \left[1 + \delta\sigma_{QC} \, \frac{r/R_C}{1 + r/R_C}\right],
$$

where $a_N = G M_{\text{bar}}(r)/r^2$, $\nu$ is the interpolating function already employed in TEG, and $R_C$ is identified with the Jeans radius $r_J \approx 0.62$ kpc derived in TEG. Equivalently, the vacuum mass profile of TEG may be rescaled by the same saturating factor.

The functional form guarantees the correct limits: for $r \ll R_C$ the correction vanishes and pure TEG is recovered; for $r \gg R_C$ the correction approaches a constant, preserving asymptotically flat rotation curves. No parameter is adjusted to rotation-curve data.

---

## 4. Geometric Stress-Energy Tensor

In the standard elasticity theory of icosahedral quasicrystals the free-energy density contains phonon, phason and phonon–phason coupling terms. Applied to the four-connected network of Fang et al., the packing deficit and the prolate phason flips generate a purely geometric effective stress-energy tensor

$$
T_{\mu\nu}^{QC} = \frac{\delta F_{\text{Fang}}}{\delta g^{\mu\nu}},
$$

where $F_{\text{Fang}}$ is the elastic free energy of the quasicrystalline tetrahedral packing. This tensor supplies the residual cohesion at low baryonic density without the introduction of particle dark matter.

---

## 5. Discussion and Epistemic Status

The construction presented here does not alter the numerical performance of TEG on the SPARC sample; it supplies a geometric substrate for the tetrahedral axiom and links the framework to existing quasicrystal and holographic results. Quantitative re-evaluation of the modified profile on the public SPARC data remains to be performed and is left for future work. The note is therefore offered strictly as a technical clarification of the microscopic realisation of TEG, not as a claim of improved phenomenological accuracy.

Open questions include the precise derivation of the numerical prefactor $\delta\sigma_{QC}$ from holographic entropy maximisation under the packing constraint of Fang et al., the extension of the same network to cluster and cosmological scales, and the embedding of the construction into the discrete holographic foliations of Boyle & Kulp.

---

## References

1. Fang, F., Kovacs, J., Sadler, G. & Irwin, K. (2014). An Icosahedral Quasicrystal as a Packing of Regular Tetrahedra. *Acta Phys. Pol. A* **126**, 458. [arXiv:1311.3994](https://arxiv.org/abs/1311.3994).
2. Franco León, M. Á. Tetrahedral Emergent Gravity series (Zenodo DOIs [10.5281/zenodo.18729743](https://doi.org/10.5281/zenodo.18729743) and subsequent versions).
3. Haji-Akbari, A. et al. (2009). Disordered, quasicrystalline and crystalline phases of densely packed tetrahedra. *Nature* **462**, 773.
4. Boyle, L., Dickens, M. & Flicker, F. (2020). Conformal Quasicrystals and Holography. *Phys. Rev. X* **10**, 011009.
5. Boyle, L. & Kulp, J. (2025). Holographic Foliations: Self-Similar Quasicrystals from Hyperbolic Honeycombs. [arXiv:2408.15316](https://arxiv.org/abs/2408.15316).
6. Newman, M. E. J. & Henley, C. L. (1995). Phason elasticity of a three-dimensional quasicrystal. *Phys. Rev. B* **52**, 6386.
7. Lelli, F., McGaugh, S. S. & Schombert, J. M. (2016). SPARC: Mass models for 175 disk galaxies. *Astron. J.* **152**, 157.
