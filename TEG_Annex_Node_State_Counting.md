> **Preliminary draft — work in progress; content subject to substantial revision**

# Annex: Node state counting and a geometric reading of the 8 labels

*Companion to the TEG framework. All results below are algebraic or geometric checks reproduced by `teg_node_state_counting.py` (16/16 checks pass). No parameter is fitted, and no statement about rotation curves is made.*

## A.1 Status

This annex does three things: (i) it separates the *label entropies* $D_A$, $D_V$ of TEG from the state counting of loop quantum gravity (LQG); (ii) it records a geometric reading of the $2z = 8$ labels at a tetrahedral node; (iii) it states, explicitly, the single hypothesis under which the step $\sigma_{\text{eff}} = \sigma_{UV}/N_{\text{bits}}$ follows from symmetry. It does **not** derive $\sigma_{UV}$, the amplification $\Phi$, the vacuum term $M_{\text{vac}}$, or any galactic result.

## A.2 Label entropy is not LQG state counting

In TEG, $D_A = \ln z$ and $D_V = \ln 2z$ are logarithms of the number of (face, orientation) labels available to one excitation at a node. In LQG, a $z$-valent node whose legs carry spin $1/2$ has an $SU(2)$-invariant (intertwiner) space of dimension $C_{z/2}$ (the Catalan number) for even $z$ and zero for odd $z$. For four legs of equal spin $j$ the dimension is $2j+1$ (verified numerically for $j = 1/2, 1, 3/2, 2$).

| $z$ | intertwiners | $S_{\text{LQG}}=\ln(\text{dim})$ | TEG $D_V=\ln 2z$ |
|---|---|---|---|
| 3 | 0 | none | 1.792 |
| 4 | 2 | 0.693 | 2.079 |
| 5 | 0 | none | 2.303 |
| 6 | 5 | 1.609 | 2.485 |
| 8 | 14 | 2.639 | 2.773 |
| 10 | 42 | 3.738 | 2.996 |

The LQG entropy grows as $z\ln 2$, while $\ln 2z$ grows logarithmically; the two differ at $z=4$ ($\ln 2$ versus $\ln 8$). The values $\ln 4$ and $\ln 8$ are recovered only for $j = 3/2$ and $j = 7/2$, which is not a prediction, since any integer $N$ equals $2j+1$ for some $j$. The consistency with LQG claimed in the main text refers to the spectral dimension only, not to state counting. (Equal spins were used; configurations with unequal spins are not covered.)

## A.3 Geometric reading of the 8 labels

Place a regular tetrahedron with vertices $v_i = (\pm1,\pm1,\pm1)$ of positive sign-product. The outward normal of the face opposite $v_i$ is $-v_i$ and the inward normal is $+v_i$ (checked numerically; the four normals close, $\sum n_i = 0$). Hence the 8 labels (face $i$, in/out) correspond to the 8 vectors $\pm n_i$, which are exactly the **8 vertices of a cube**, i.e. three sign bits $(s_x, s_y, s_z)$. The orientation (in/out) is the **parity** $s_xs_ys_z$, which the tetrahedral group $T_d$ preserves. Therefore:

- $D_V = \ln 8$: three bits, the signs of the Cartesian components of a face normal (so $N_{\text{bits}}=3$ reflects $\dim\mathbb{R}^3$ geometrically);
- $D_A = \ln 4$: the single-orientation subspace (4 states, 2 independent bits);
- $D_V - D_A = \ln 2$: one bit, the parity (the "orientation duality").

## A.4 Candidate state spaces

Criteria fixed before comparison: (P1) $\ln 4$, $\ln 8$, $\ln 2$ arise without insertion; (P2) the number 3 arises from structure; (P3) symmetry fixes how entropy is shared among the three channels.

| Candidate | P1 | P2 | P3 |
|---|---|---|---|
| A: 8 modes, $T_d$ irreps ($2A_1\oplus 2T_2$) | yes (by definition) | **no**: directions live in $T_2$ (6 states, $\ln 6\neq\ln 8$) | no |
| B: labels $\pm n_i$ = cube vertices (3 sign bits) | yes | **yes** | yes, conditional (A.5) |
| C: LQG node, spin $1/2$ | no (gives $\ln 2$) | no | no |

## A.5 Symmetry and the $1/N_{\text{bits}}$ step

$T_d$ preserves the factorisation into the three axis-sign bits, but does **not** preserve the factorisation "face (2 bits) + orientation (1 bit)" (which would give a 2:1 split). $S_3$ acts transitively on the three axis bits, so any allocation that is additive over them gives equal weights $1/3$.

**Hypothesis H.** The roughness $\sigma_{UV}$ is allocated additively over the three axis-sign bits.

Under H, equipartition follows from $T_d$ symmetry; H itself is not derived. Note that for the single-orientation state the per-axis marginal entropies are $\ln 2$ each (sum $3\ln 2$) while the joint entropy is $\ln 4$ (mutual information $\ln 2$), so "entropy per direction" is ambiguous between marginal and joint readings, although the fraction $1/3$ holds in both.

## A.6 What this does not establish

| Item | Status |
|---|---|
| Intertwiner counting for $z$-valent spin-$1/2$ nodes | Standard result, verified numerically |
| 8 labels $=$ cube vertices; parity $=$ orientation | Computed here (geometric identity) |
| Identification of TEG's label space with $\pm n_i$ | Conjectural (a reading of "flux in/out per face") |
| Hypothesis H (additive allocation per axis bit) | Assumed, not derived |
| $\sigma_{UV}$, $\Phi=\ln 4$, $M_{\text{vac}}$, rotation curves | Not addressed |
| Survival of local $T_d$ symmetry in an icosahedral quasicrystalline vacuum | Open |

## A.7 Reproducibility

```
python teg_node_state_counting.py
```

Requires only `numpy`. Output: 16/16 `PASS`.

## References

1. Barbieri, A. (1998). Quantum tetrahedra and simplicial spin networks. *Nucl. Phys. B* **518**, 714.
2. Baez, J. C. & Barrett, J. W. (1999). The quantum tetrahedron in 3 and 4 dimensions. *Adv. Theor. Math. Phys.* **3**, 815.
