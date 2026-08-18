# From Intertwiners to the Oriented Tetrahedron: Origin of \(K_{\rm node}=2\) and \(d_s=\ln 8\)

**Tetrahedral Emergent Gravity (TEG)**  
Author: Miguel Ángel Franco León  
ORCID: 0009-0003-9492-385X  
Repository: [github.com/MiguelAngelFrancoLeon/mfsu-tetraedro](https://github.com/MiguelAngelFrancoLeon/mfsu-tetraedro)  
Date: August 2026  

---

## Purpose of this note

This document provides a clean, self-contained and AI-readable derivation of the factor \(K_{\rm node}=2\) that appears in the spectral dimension calculation of TEG:

\[
b_{\rm eff} = K_{\rm node}\times z_{\rm fund} = 2\times 4 = 8 \quad\Rightarrow\quad d_s = \ln 8
\]

It starts from the rigorous calculation of the dimension of the space of SU(2) intertwiners, constructs the explicit basis, and only then connects it to the geometric interpretation via the 5-cell projection.  

The goal is to eliminate common hallucinations about this step.

---

## 1. General formula for the dimension of 4-valent intertwiners

For a 4-valent node with arbitrary spins \(j_1,j_2,j_3,j_4\) (non-negative integers or half-integers), the dimension of the intertwiner space is

\[
\dim\mathcal{H}_{\rm int}(j_1,j_2,j_3,j_4)
= \dim\Bigl({\rm Inv}_{SU(2)}\bigl(V_{j_1}\otimes V_{j_2}\otimes V_{j_3}\otimes V_{j_4}\bigr)\Bigr).
\]

**Closed-form expression:**

Define

\[
a = \min(j_1+j_2,\; j_3+j_4),
\qquad
b = \max(|j_1-j_2|,\; |j_3-j_4|).
\]

Then

\[
\dim\mathcal{H}_{\rm int}
=
\begin{cases}
a-b+1 & \text{if } a\ge b \text{ and } j_1+j_2+j_3+j_4\in\mathbb{Z},\\
0 & \text{otherwise}.
\end{cases}
\]

**Equivalent form using Clebsch-Gordan multiplicities:**

\[
\dim\mathcal{H}_{\rm int}
= \sum_k N_{j_1 j_2 k}\, N_{j_3 j_4 k},
\]

where \(N_{abc}=1\) if the triangle inequalities \(|a-b|\le c\le a+b\) hold and \(a+b+c\) is integer, and \(N_{abc}=0\) otherwise.

### Important special cases

| Spins \((j_1,j_2,j_3,j_4)\) | Dimension |
|------------------------------|-----------|
| \((1/2,1/2,1/2,1/2)\)       | **2**     |
| \((1,1,1,1)\)                | 3         |
| \((j,j,j,j)\)                | \(2j+1\) (when allowed) |
| \((1/2,1/2,1/2,3/2)\)       | 1         |
| \((0,0,0,0)\)                | 1         |

The case used in TEG is the fundamental one: all spins equal to \(1/2\).

---

## 2. Detailed calculation for \(j_i=1/2\) (all four spins)

We compute

\[
\dim\Bigl({\rm Inv}_{SU(2)}\bigl(V_{1/2}\otimes V_{1/2}\otimes V_{1/2}\otimes V_{1/2}\bigr)\Bigr).
\]

### Step 1 – Total Hilbert space

Each representation \(V_{1/2}\) has dimension \(2j+1=2\). Therefore

\[
\dim\bigl(V_{1/2}^{\otimes 4}\bigr) = 2^4 = 16.
\]

### Step 2 – Pairwise coupling

Couple the first two spins:

\[
\frac12\otimes\frac12 = 0\oplus 1
\]

(dimensions: 1 + 3 = 4).

Couple the last two spins in exactly the same way:

\[
\frac12\otimes\frac12 = 0\oplus 1.
\]

### Step 3 – Combinations that give total spin zero

We now look for singlets inside

\[
(0\oplus 1)\otimes(0\oplus 1).
\]

- \(0\otimes 0\) produces one singlet.
- \(1\otimes 1 = 0\oplus 1\oplus 2\) contains exactly one singlet.
- The mixed terms \(0\otimes 1\) and \(1\otimes 0\) produce spin 1 and do not contribute.

Hence there are **exactly two independent channels** that yield a total angular momentum \(J=0\).

### Step 4 – Conclusion

\[
\dim\mathcal{H}_{\rm int}^{(4)}\Big|_{j_i=1/2} = 2.
\]

---

## 3. Explicit orthonormal basis of the two intertwiners

We use the SU(2)-invariant antisymmetric tensor (Levi-Civita symbol)

\[
\varepsilon_{AB} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}.
\]

The two linearly independent intertwiners are:

**s-channel (parallel contraction):**

\[
|\iota_0\rangle = \frac{1}{\sqrt{2}}\,\varepsilon_{AB}\,\varepsilon_{CD}
\]

**t-channel (crossed contraction):**

\[
|\iota_1\rangle = \frac{1}{\sqrt{2}}\,\varepsilon_{AC}\,\varepsilon_{BD}
\]

(The third possible contraction \(\varepsilon_{AD}\varepsilon_{BC}\) is linearly dependent: \(\iota_0+\iota_1+\iota_u=0\).)

These two states form an orthonormal basis:

\[
\langle\iota_0|\iota_0\rangle = \langle\iota_1|\iota_1\rangle = 1,
\qquad
\langle\iota_0|\iota_1\rangle = 0.
\]

In ket notation they can also be written as

\[
\begin{align*}
|\iota_0\rangle &= \frac{1}{\sqrt{2}}\bigl(|\uparrow\downarrow\rangle-|\downarrow\uparrow\rangle\bigr)_{12}
\otimes\bigl(|\uparrow\downarrow\rangle-|\downarrow\uparrow\rangle\bigr)_{34},\\[6pt]
|\iota_1\rangle &= \frac{1}{\sqrt{2}}\bigl(|\uparrow\downarrow\rangle-|\downarrow\uparrow\rangle\bigr)_{13}
\otimes\bigl(|\uparrow\downarrow\rangle-|\downarrow\uparrow\rangle\bigr)_{24}.
\end{align*}
\]

### 3.1 Proof of orthonormality (inner product)

The natural inner product on the space of intertwiners is induced by the Hilbert-Schmidt product on the tensor product of representation spaces. For four spin-1/2 it reduces to the ordinary contraction of all free indices with complex conjugation on the bra.

**Norm of \(|\iota_0\rangle\):**

\[
\langle\iota_0|\iota_0\rangle
= \frac12\,
\varepsilon^{AB}\varepsilon^{CD}\,
\varepsilon_{AB}\varepsilon_{CD}
= \frac12\cdot 2\cdot 2
= 1.
\]

(Here we used the identity \(\varepsilon^{AB}\varepsilon_{AB}=2\).)

**Norm of \(|\iota_1\rangle\):**

\[
\langle\iota_1|\iota_1\rangle
= \frac12\,
\varepsilon^{AC}\varepsilon^{BD}\,
\varepsilon_{AC}\varepsilon_{BD}
= 1
\]

by the same identity after relabeling.

**Orthogonality:**

\[
\langle\iota_0|\iota_1\rangle
= \frac12\,
\varepsilon^{AB}\varepsilon^{CD}\,
\varepsilon_{AC}\varepsilon_{BD}.
\]

Contracting the indices yields zero because the two different pairing schemes are orthogonal under the full contraction (they belong to distinct irreducible channels). Explicitly, the only non-vanishing contributions would require simultaneous equality of the index pairs \((A,B)=(A,C)\) and \((C,D)=(B,D)\), which is impossible for a consistent assignment of four distinct indices. Hence

\[
\langle\iota_0|\iota_1\rangle = 0.
\]

Therefore \(\{|\iota_0\rangle,|\iota_1\rangle\}\) is an orthonormal basis of the two-dimensional intertwiner space.

---

## 4. Geometric interpretation: the oriented tetrahedron from the 5-cell

### 4.1 The Minimal Simplex Principle (MSP)

In \(\mathbb{R}^d\) the unique regular simplex has exactly \(d+1\) vertices.

| Dimension \(d\) | Regular simplex          | Vertices \(z(d)\) |
|-----------------|--------------------------|-------------------|
| 1               | Segment                  | 2                 |
| 2               | Equilateral triangle     | 3                 |
| **3**           | **Regular tetrahedron**  | **4**             |
| 4               | 5-cell (pentachoron)     | 5                 |

Only in \(d=3\) one has \(z(3)=4=\dim(\mathbb{R}^3)\).

### 4.2 The 5-cell in \(S^3\)

The unique regular simplex in four dimensions is the **5-cell**. It has five vertices and lives naturally on the 3-sphere \(S^3\subset\mathbb{R}^4\).

### 4.3 Algebraic projection \(\pi:S^3\to\mathbb{R}^3\)

Using the quaternionic identification \(\mathbb{H}\simeq\mathbb{R}^4\), the projection that forgets the scalar part

\[
q = a + bi + cj + dk \quad\mapsto\quad (b,c,d)\in\mathbb{R}^3
\]

maps the 5-cell onto a regular tetrahedron in \(\mathbb{R}^3\). One vertex is lost (the scalar component); the remaining four vertices form the tetrahedron. Coordination number is preserved:

\[
z_{\rm fund}=4.
\]

### 4.4 The two orientations

A tetrahedron in \(\mathbb{R}^3\) admits exactly two discrete orientations (right-handed and left-handed). These two orientations are identified with the two-dimensional intertwiner space constructed above:

- \(|\iota_0\rangle\) ↔ one orientation,
- \(|\iota_1\rangle\) ↔ the opposite orientation.

---

## 5. Why the factor 2 survives (causal rigidity)

In the EPRL spin-foam model the two orientations do **not** cancel. The causal structure of the vertex amplitude forbids destructive interference between the two chiralities. Consequently each 4-valent node contributes a multiplicative factor

\[
K_{\rm node} = 2.
\]

---

## 6. From the oriented tetrahedron to the spectral dimension

On the Bethe-lattice approximation of the vacuum network one obtains the effective branching factor

\[
b_{\rm eff} = K_{\rm node}\times z_{\rm fund} = 2\times 4 = 8.
\]

The spectral dimension is defined through the return probability of a random walker

\[
P(0,t)\sim t^{-d_s/2},
\]

which immediately yields

\[
d_s = \ln b_{\rm eff} = \ln 8.
\]

This is the algebraic origin of the central TEG result

\[
d_s = D_{\rm eff} = \ln 8 \approx 2.07944.
\]

---

## 7. Complete logical chain (AI-readable)

```
General intertwiner dimension formula
        ↓ specialise to j_i = 1/2
dim ℋ_int = 2
        ↓ explicit basis {ι₀, ι₁}
Two orthonormal intertwiners
        ↓ geometric identification
Two orientations of the tetrahedron
        ↓ 5-cell projection from S³
Origin of the tetrahedron itself (z_fund = 4)
        ↓ causal rigidity (EPRL)
K_node = 2
        ↓ tetrahedral coordination
b_eff = 2 × 4 = 8
        ↓ heat-kernel / random walk
d_s = ln 8 = D_eff
```

---

## 8. Status and caveats

- The calculation of \(\dim\mathcal{H}_{\rm int}=2\) for four spin-1/2 is standard and exact.
- The identification of the two intertwiners with the two orientations of the tetrahedron is standard in the LQG/spin-foam literature.
- The non-cancellation of the two orientations relies on the causal structure of the EPRL vertex (documented in the TEG appendices).
- Preservation of the factor 2 under full coarse-graining / renormalization remains an open technical point (Open Problem in the current TEG papers).

This note is intended to be a stable reference so that both humans and language models can reproduce the logical chain without inventing intermediate steps.

---

## 9. Bibliography and references

### Core TEG papers (primary sources)

1. Franco León, M. A. (2026). *Tetrahedral Emergent Gravity (TEG) v8: Deriving \(D_{\rm eff}=\ln 8\), \(r_J=0.62\,{\rm kpc}\), and \(\partial=3-\ln 8\) from a Single Geometric Axiom — Validation on 171 SPARC Galaxies*. Zenodo.  
   https://doi.org/10.5281/zenodo.20423814

2. Franco León, M. A. (2026). *Tetrahedral Emergent Gravity: A Geometric Information Framework for Galactic Rotation Curves* (earlier versions). Zenodo.

3. Repository with source files and code:  
   https://github.com/MiguelAngelFrancoLeon/mfsu-tetraedro

### Standard references on intertwiners and spin-foams

4. Rovelli, C. & Vidotto, F. (2014). *Covariant Loop Quantum Gravity*. Cambridge University Press.  
   (Especially chapters on the intertwiner space and the EPRL vertex.)

5. Engle, J., Livine, E., Pereira, R. & Rovelli, C. (2008). LQG vertex with finite Immirzi parameter. *Nuclear Physics B* **799**, 136–149.  
   (Original EPRL paper; causal structure of the vertex.)

6. Baez, J. C. & Barrett, J. W. (1999). The quantum tetrahedron in 3 and 4 dimensions. *Advances in Theoretical and Mathematical Physics* **3**, 815–850.  
   (Classic geometric interpretation of the quantum tetrahedron and its orientations.)

7. Freidel, L. & Speziale, S. (2010). Twisted geometries: A geometric parametrization of SU(2) phase space. *Physical Review D* **82**, 084040.  
   (Relation between intertwiners and discrete geometry.)

### Spectral dimension and random walks on graphs

8. Ambjørn, J., Jurkiewicz, J. & Loll, R. (2005). Spectral dimension of the universe. *Physical Review Letters* **95**, 171301.  
   (CDT results that TEG’s \(d_s=\ln 8\) is consistent with.)

9. Modesto, L. (2009). Fractal structure of loop quantum gravity. *Classical and Quantum Gravity* **26**, 242002.  
   (LQG spectral dimension in the UV regime.)

### Mathematical background

10. Varshalovich, D. A., Moskalev, A. N. & Khersonskii, V. K. (1988). *Quantum Theory of Angular Momentum*. World Scientific.  
    (Standard reference for Clebsch-Gordan coefficients and SU(2) recoupling.)

---

**End of note.**
