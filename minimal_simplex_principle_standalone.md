# The Minimal Simplex Principle: Tetrahedral Coordination as a Combinatorial Necessity in R³

### A proof that *z*<sub>min</sub> = 4 is not a hypothesis but a consequence of the definition of volume

**Miguel Angel Franco León**
Independent researcher, Argentina — July 2026

---

## Scope of this paper

Sections 1–3 (the Category Error, Lemma 1, and Theorem 1) are self-contained: they depend on nothing beyond the standard definition of volume in ℝ³ and elementary linear algebra. Section 4.1 relates this result to an existing, independent finding in loop quantum gravity. Section 4.2 is a numerical observation, explicitly flagged as non-derivational. Section 4.3 is explicitly marked as an application of this principle within the author's separate Tetrahedral Emergent Gravity (TEG) framework, and is **not required for, nor implied by, the core result**. A reader interested only in the combinatorial claim can stop after Section 3.

---

## Abstract

Several independent approaches to quantum gravity employ tetrahedral or 4-valent building blocks — loop quantum gravity uses 4-valent spin-network nodes, causal dynamical triangulations sum over 4-simplices — but in each case the tetrahedron is introduced as a convenient discretization, not derived as necessary. This paper proves that no derivation is needed, because none is possible: in Euclidean ℝ³, the minimal number of points required to enclose non-zero volume is exactly four (Lemma 1), and hence the minimal coordination number of any discrete structure supporting volume is *z* = 4 (Theorem 1, the Minimal Simplex Principle). This is a statement about the definition of volume itself, not a physical postulate. It has no free parameters and admits no weaker or stronger version: any structure with *z* < 4 cannot support volume by construction, and *z* = 4 saturates the bound.

**Keywords:** minimal simplex, tetrahedral coordination, discrete geometry, quantum gravity, simplicial complexes, loop quantum gravity

---

## Figure 1 — Dimensional ascent in ℝ³

| Points | Dimension | Object | Measure | Volume |
|---|---|---|---|---|
| 2 | 1D | Line segment | Length $L > 0$ | $V = 0$ |
| 3 | 2D | Triangle (coplanar) | Area $A > 0$ | $V = 0$ |
| **4** | **3D** | **Tetrahedron (non-coplanar)** | — | $V > 0$ — first volume, inevitable |

*Dimensional ascent in ℝ³. One point defines location (0D), two points define length (1D), three points define area (2D) but remain coplanar with identically zero volume. Four non-coplanar points define the 3-simplex — the tetrahedron — the first enclosure of volume. It cannot be reduced.*

---

## 1. The Category Error

A recurring question in discrete approaches to quantum gravity is: *what dynamics select the tetrahedron as the fundamental building block?* This question is a category error. It is equivalent to asking what dynamics define volume before volume exists, or why a triangle has three sides.

Volume is not an emergent property of a pre-geometric tetrahedron. The tetrahedron *is* the definition of volume in three dimensions. Any theory that presupposes space — even to quantize it, discretize it, or sum over it — has already presupposed the tetrahedron. Demanding a dynamical derivation of the tetrahedron from within a volume-bearing theory is self-contradictory.

> To derive the tetrahedron dynamically is to attempt to define volume without volume. The request is ill-posed. The minimal must be postulated only in the sense that logic itself must be postulated.

---

## 2. Lemma 1 — Minimal Volume in ℝ³

> **Lemma 1.** In Euclidean space ℝ³, any set of *k* < 4 points encloses zero 3-volume. The minimal number of points required to enclose *V* > 0 is *k* = 4, realized uniquely (up to deformation) as the tetrahedron.

**Proof.** Trivial by dimension count, but stated explicitly because its consequences are not trivial.

- **k=1** — point: 0-dimensional manifold. *V* = 0.
- **k=2** — segment: 1-dimensional. Defines length $L = |x_2 - x_1|$, volume zero.
- **k=3** — triangle: At most 2-dimensional affine span. If non-collinear, encloses area $A = \tfrac{1}{2}|(x_2-x_1)\times(x_3-x_1)| > 0$, but lies in a plane. Its 3-volume is identically zero.
- **k=4** — **tetrahedron**: Four points $x_1..x_4$ non-coplanar. Volume $V = \tfrac{1}{6}|(x_2-x_1)\cdot((x_3-x_1)\times(x_4-x_1))| > 0$ iff $\det \neq 0$. This is the 3-simplex, the first polytope with interior.

No configuration with fewer than four points can have $\det \neq 0$. ∎

$$
V_{k<4} = 0 \qquad\Big|\qquad V_{k=4} = \tfrac{1}{6}|\det| > 0
$$

---

## 3. Theorem 1 — The Minimal Simplex Principle

> **Theorem 1 (Minimal Simplex Principle).** Let *z(d)* be the minimal number of facets meeting at a vertex required to define a non-degenerate volume element in ℝ^d. Then *z(d) = d+1*. In particular, in ℝ³, *z*<sub>min</sub> = 4. Any discrete structure supporting volume must have coordination *z* ≥ 4, identifying graph valence with simplex vertex count via the standard polytope-normal (Minkowski) correspondence. The minimal case saturates the bound.

The proof follows directly from Lemma 1. A convex polytope in ℝ^d requires at least *d+1* facets to close. This is the definition of a *d*-simplex. In ℝ² the simplex is the triangle (3 edges). In ℝ³ the simplex is the tetrahedron (4 faces). Coordination number *z* corresponds to valence — number of links meeting at a node, or faces meeting at a vertex.

Therefore any graph, spin-network, or triangulation that claims to support 3-volume must be at least 4-valent. A 3-valent node can only support area. This is not a dynamical result; it is combinatorial, and it holds independently of any physical theory built on top of it.

$$
z(d) = d + 1
$$

$$
z_{\min}(\mathbb{R}^3) = 4
$$

*This theorem requires only the definition of volume in ℝ^d and elementary linear algebra (non-vanishing determinant ⇔ non-coplanarity). It does not depend on any specific quantum-gravity framework, and holds regardless of which (if any) physical theory adopts it.*

---

## 4. Consequences and Applications

### 4.1 — Consistency with Loop Quantum Gravity

In LQG, the volume operator $\hat V$ vanishes identically on gauge-invariant nodes of valence < 4; the first non-zero eigenvalues appear for 4-valent nodes. This is habitually presented as a consequence of SU(2) recoupling theory. Theorem 1 offers a combinatorial reading of the same fact: a <4-valent node cannot support volume by construction, independently of the group-theoretic machinery that produces the vanishing operator in LQG. This is not a re-derivation of the LQG result — it predates Theorem 1 and stands on its own — but a combinatorial account of *why* it must be true.

### 4.2 — Numerical observation: kissing number and holographic bits (speculative)

Let $z_{\mathrm{pack}}(\mathbb{R}^3) = 12$ be the kissing number — the maximal number of unit spheres that can touch a central sphere in optimal packing. $z_{\mathrm{pack}}$ and $z_{\min}$ are quantities of different mathematical origin (packing density vs. minimal enclosure), and no derivation in this paper forces a relation between them. The following is recorded as a numerical observation only:

$$
z_{\mathrm{pack}} - z_{\min} = 12 - 4 = 8 = 2^3
$$

Hence $N_{\mathrm{bits}} = \log_2(8) = 3 = \dim(\mathbb{R}^3)$. This is a suggestive numerical coincidence, not a derivation: no argument here shows why the difference $z_{\mathrm{pack}} - z_{\min}$ must carry physical meaning.

> ### ⚠️ External application — depends on the TEG framework, not on Theorem 1 alone
>
> **4.3 — Effective dimension and entropy in TEG.** Within the author's separate Tetrahedral Emergent Gravity (TEG) framework, the number of oriented tetrahedral faces is taken to be $2 \cdot z_{\min}$, and an effective thermal dimension is *constructed* (not derived from Theorem 1 alone) as
>
> $$
> D_{\mathrm{eff}} = \ln(2\, z_{\min}) = \ln 8 = 3\ln 2 .
> $$
>
> This identification — and its proposed match to Bekenstein–Hawking entropy density under holographic projection — is a modeling choice specific to TEG, detailed in Franco León, *TEG v7*, §4.3 (Zenodo, DOI [10.5281/zenodo.19479542](https://doi.org/10.5281/zenodo.19479542)). It is reported here only to show one possible use of Theorem 1; readers evaluating the core mathematical claim of this paper do not need to accept or evaluate this application.

---

## 5. Why No Further Derivation Is Possible — Logical Closure

A natural objection: *"You assumed Euclidean ℝ³ to prove tetrahedral minimality; but ℝ³ itself should emerge from a deeper theory."*

The objection inverts logic. The statement *"space is three-dimensional"* is operationally equivalent to *"volume requires four non-coplanar points."* Dimension is defined by the minimal simplex. To ask for a theory of space that does not presuppose the minimal simplex is to ask for a theory of counting that does not presuppose the integer 1.

Any theory that:

1. Uses the word "volume", "area", "node", "link", "simplex", or "holographic screen", or
2. Writes an action $\int d^3x\,\sqrt{g}$, a sum over triangulations, or a Hilbert space of spin-networks,

has already assumed Lemma 1.

Therefore the search for a dynamical principle *before* the tetrahedron is self-contradictory. The tetrahedron is the floor. There is no basement.

> **Logical chain:**
> **Space** ⇒ presupposes **Volume** ⇒ presupposes **Tetrahedron (z=4)** ⇒ is consistent with the independently established LQG volume-operator result (§4.1).
> Any attempt to reverse the arrow must define volume without tetrahedron — impossible by Lemma 1.

---

## Conclusion

We have proven that $z_{\min} = 4$ in ℝ³ is not a hypothesis, not a model choice, and not derivable from deeper dynamics — it is the absolute combinatorial minimum for volume. It is therefore the necessary coordination of any discrete structure that supports volume, independently of which physical theory, if any, is built on top of it.

This result is deliberately minimal in scope. It does not depend on, and is not weakened by, the success or failure of any specific physical model that uses it — including the author's own TEG framework, whose cosmological predictions remain under active development and are documented separately with open problems clearly marked.

---

## Note added (July 2026) — Related mathematical context: high-dimensional sphere packing

Recent results by OpenAI (*Ten Advances in Mathematics and Theoretical Computer Science*, 249pp, 2026) determine the exact exponential decay rate of the Cohn–Elkies linear program and improve the classical Kabatianskii–Levenshtein (1978) bounds for binary and spherical codes [8]. In particular, they prove the minimal uncertainty radius is $(1/\pi + o(1))\sqrt{d}$ and the optimal LP exponent is $\sqrt{e/2\pi}$. These results, together with the classical kissing number problem (solved in ℝ³ since 1953), illustrate that minimal combinatorial structures in packing geometry remain the subject of deep, active mathematical results — a domain conceptually adjacent to, but distinct from, the minimal-enclosure argument in this paper ($z_{\min}=4$). This work does not establish or imply the Minimal Simplex Principle; it is cited here only as related mathematical context, not as independent confirmation.

---

## References

1. Rovelli, C., Smolin, L. — Discreteness of area and volume in quantum gravity. *Nucl. Phys. B* 442, 593–626 (1995). Volume operator vanishes for valence < 4.
2. Ambjørn, J., Jurkiewicz, J., Loll, R. — Emergence of a 4D world from causal quantum gravity. *Phys. Rev. Lett.* 93, 131301 (2004).
3. Varieschi, G. — Newtonian Fractional-Dimension Gravity and tetrahedral symmetry. *Universe* 7, 387 (2021).
4. Coxeter, H.S.M. — *Regular Polytopes*. On minimal facets: the simplex has *d+1* facets in ℝ^d.
5. Kabatianskii, G.A., Levenshtein, V.I. — Bounds for packings on a sphere and in space. *Probl. Peredachi Inf.* 14, 3–25 (1978).
6. Cohn, H., Elkies, N. — New upper bounds on sphere packings I. *Ann. Math.* 157, 689–714 (2003).
7. Cohn, H., et al. — The sphere packing problem in dimension 8 and 24. *Ann. Math.* (2017).
8. OpenAI — *Ten Advances in Mathematics and Theoretical Computer Science*. 249pp, 2026. On exact Cohn–Elkies LP decay rate $\sqrt{e/2\pi}$, minimal uncertainty radius $(1/\pi + o(1))\sqrt{d}$, and improved Kabatianskii–Levenshtein bounds.
9. Franco León, M.A. — *Tetrahedral Emergent Gravity v7: Entropic Cosmology from Minimal Vacuum*. Zenodo, April 9 2026. DOI: [10.5281/zenodo.19479542](https://doi.org/10.5281/zenodo.19479542). (Cited only in §4.3 as the source of an external application; not required for Sections 1–3.)
10. Franco León, M.A. — *TEG vH3.1 / v8: Holographic Closure and Minimal Simplex Principle*. Zenodo, July 2 2026. DOI: [10.5281/zenodo.21129061](https://doi.org/10.5281/zenodo.21129061). (Cited only in §4.3.)

---

*"The tetrahedron is not in space. Space is in the tetrahedron."*
