# From Simplicial Minimality to Spectral Dimension: Why \(4\times 2=8\) Does Not Yield \(d_s=\ln 8\)

Miguel Ángel Franco León  
Independent Researcher  
ORCID: 0009-0003-9492-385X  
GitHub: [MiguelAngelFrancoLeon/mfsu-tetraedro](https://github.com/MiguelAngelFrancoLeon/mfsu-tetraedro)

**Status.** Working note. Tetrahedral Emergent Gravity (TEG) is the *framework under examination*, not a validated theory.  
**Claim of this note.** \(d_s=\ln 8\) is a hypothesis. It is not derived from tetrahedral minimality plus intertwiner multiplicity.

---

## Abstract

A non-degenerate simplex in three dimensions has four vertices. Separately, the SU(2)-invariant intertwiner space of a four-valent \(j=1/2\) node is two-dimensional. Their product is eight. It is tempting to set \(b_{\mathrm{eff}}=8\) and \(d_s=\ln 8\).

That identification is not a theorem. This note separates three quantities — geometric coordination \(z\), internal multiplicity \(M\), and dynamical branching \(b_{\mathrm{dyn}}\) — and shows that finite internal multiplicity plus local finite-range dynamics does not change the leading spectral exponent. On a three-dimensional Hausdorff geometry one still has \(d_w=2\) and \(d_s=3\).

If one *assumes* \(d_H=3\) and *requires* \(d_s=\ln 8\), the walk dimension must be \(d_w=6/\ln 8\simeq 2.885\). That is an anomalous-transport target, not a derivation. An alternative programme (reduced Hausdorff dimension \(d_H\simeq\ln 8\) with ordinary diffusion) is a different hypothesis and is not treated as proved here.

The missing object is an explicit tetrahedral coarse-graining that couples the intertwiner sector to spatial transport. Until that object exists, \(4\times 2=8\not\Rightarrow d_s=\ln 8\).

---

## 1. Purpose

The purpose is modest: list what follows from two standard facts, and what does not.

TEG, as previously documented by the author, used the chain
\[
z=4 \;\longrightarrow\; b_{\mathrm{eff}}=2z=8 \;\longrightarrow\; d_s=\ln 8
\]
and identified \(d_s=D_{\mathrm{eff}}=d_f=\ln 8\). That last identification is an ansatz. This note replaces it with a testable question.

---

## 2. What is established

### 2.1 Simplicial minimality

A non-degenerate \(d\)-simplex has \(d+1\) vertices. For \(d=3\),
\[
N_{\min}=4.
\]
The unique regular simplex is the tetrahedron.

This is combinatorial geometry. It is **not** yet a law for the vacuum, and it does not by itself fix the degree of a physical graph:

| Object | Count |
|---|---|
| Vertices of one 3-simplex | 4 |
| Edges incident on one vertex *of that simplex* | 3 |
| Neighbours of a centre whose neighbours form a tetrahedron | 4 |

The third row is a 4-valent *network* picture (centre + tetrahedron of neighbours). It is a further modelling choice, here written
\[
z_{\min}=4
\]
only as a **minimality condition**, not as a derived microscopic Hamiltonian.

### 2.2 Intertwiner multiplicity

For four spin-\(1/2\) representations,
\[
\tfrac12\otimes\tfrac12=0\oplus 1,
\]
and a total singlet can be built through two independent channels \((0\otimes 0)\to 0\) and \((1\otimes 1)\to 0\). Hence
\[
\dim\operatorname{Inv}\bigl[(\tfrac12)^{\otimes 4}\bigr]=2.
\]
This is representation theory. It does not depend on a gravitational reading.

A convenient recoupling matrix (phase conventions aside) is
\[
F=\begin{pmatrix}-1/2 & \sqrt{3}/2 \\ \sqrt{3}/2 & 1/2\end{pmatrix},
\]
which is real orthogonal, \(F^\top F=I\), \(\det F=-1\), \(\mathrm{spec}(F)=\{-1,+1\}\). Recoupling itself supplies no attenuation.

The tensors \(\varepsilon_{AB}\varepsilon_{CD}\) and \(\varepsilon_{AC}\varepsilon_{BD}\) are linearly independent but not, with identical prefactors, orthonormal. An orthonormal pair is obtained by Gram–Schmidt. The invariant statement is only \(\dim\mathcal H_{\mathrm{int}}=2\).

---

## 3. The tempting step, and why it fails

Write \(M=\dim\mathcal H_{\mathrm{int}}=2\). Then
\[
zM=8.
\]
This counts combinations of geometric directions and internal states. It does **not** count independent spatial propagation channels. One must distinguish
\[
z=\text{geometric coordination},\qquad
M=\text{internal multiplicity},\qquad
b_{\mathrm{dyn}}=\text{dynamical branching}.
\]
The TEG identification would require the extra equality
\[
b_{\mathrm{dyn}}=zM=8,
\]
which state counting does not give.

---

## 4. Control: local tetrahedral walk

Take the four unit tetrahedral directions obtained from
\[
v_1=(1,1,1),\;
v_2=(1,-1,-1),\;
v_3=(-1,1,-1),\;
v_4=(-1,-1,1)
\]
by \(n_i=v_i/\sqrt{3}\). Then
\[
\sum_{i=1}^4 n_i^a n_i^b=\frac43\,\delta^{ab}.
\]
(The un-normalised \(v_i\) give \(4\,\delta^{ab}\), not \(4/3\).)

The local Fourier symbol of the graph Laplacian has the small-momentum expansion
\[
\lambda(k)=-c\,k^2+O(k^4),\qquad c>0.
\]
Hence the ordinary local walk has
\[
d_w=2.
\]
If the large-scale Hausdorff dimension remains \(d_H=3\), the standard relation
\[
d_s=\frac{2d_H}{d_w}
\]
gives
\[
d_s=3.
\]
This is the baseline.

---

## 5. No-go: finite internal space, local finite range

Enlarge the state space to \(\mathcal H_{\mathrm{geom}}\otimes\mathbb C^M\) with \(M<\infty\). Let
\[
(T\psi)_\alpha(x)=\sum_{r\in\mathcal S}\sum_{\beta}T_{\alpha\beta}(r)\,\psi_\beta(x+r)
\]
be translation invariant, with \(\mathcal S\) finite. Then \(\hat T(k)\) is analytic at \(k=0\). If the linear drift vanishes, the critical eigenvalue is generically
\[
\lambda_0(k)=1-k_a D^{ab}k_b+O(k^4).
\]
Isotropy gives \(1-\lambda_0(k)=D|k|^2+O(k^4)\), so again \(d_w=2\).

**Structural result.**
\[
\text{finite }M+\text{local finite-range dynamics}\;\not\Rightarrow\; d_s\neq d_H.
\]
In particular, two intertwiners do not produce \(d_s=\ln 8\).

The same conclusion holds if the internal transitions are given by \(|F_{ij}|^2\), or by any fixed stochastic matrix on \(\mathbb C^2\). Unitarity of \(F\) makes the point sharper: recoupling is a change of internal basis, not a scale-dependent filter.

Assigning finite waiting times to the two internal states, or a finite persistence, can generate *crossovers*. It does not generically produce an anomalous *asymptotic* \(d_w\).

---

## 6. Two programmes, both open

The older TEG texts identified \(d_s=D_{\mathrm{eff}}=d_f=\ln 8\). That collapses two different hypotheses.

**Programme A** (this note). Keep \(d_H=3\). Then
\[
d_s=\ln 8 \quad\Longleftrightarrow\quad d_w=\frac{6}{\ln 8}\simeq 2.88539008.
\]
Ordinary diffusion is not enough. One needs anomalous transport.

**Programme B.** Reduce the Hausdorff dimension itself, \(d_H\simeq\ln 8\), and keep \(d_w=2\). Then \(d_s\simeq\ln 8\) would follow from the same relation, but by a different mechanism (fractal support, not anomalous walk). Programme B is **not** established by \(zM=8\) either, and is not proved here.

These are not two names for one theorem. A future construction must say which one it is testing.

---

## 7. Diagnostic numbers, not TEG constants

Under Programme A one may parametrize \(D(L)\sim L^{-\theta}\) and use \(d_w=2+\theta\). The target \(d_w=6/\ln 8\) would require
\[
\theta=\frac{6}{\ln 8}-2\simeq 0.88539008.
\]
On dyadic scales \(L_n=2^n\), a phenomenological survival factor \(Q(L_n)\sim q^n\) would then have
\[
q_*=2^{-\theta}\simeq 0.54134113.
\]

These numbers are **inverse diagnostics**. They are what Programme A would have to *reproduce*. They are not derived from SU(2), and they must not be inserted into a coarse-graining in order to “confirm” \(\ln 8\).

No matrix element of \(F\) equals \(q_*\). The values \(1/4\) and \(3/4\) are the recoupling probabilities; they are not a spectral-dimension mechanism.

---

## 8. What has been ruled out

1. \(z=4\) alone: local tetrahedral walk, \(d_s=3\) if \(d_H=3\).
2. \(z=4\) plus \(M=2\), still local and finite-range: same leading exponent.
3. Unitary recoupling: no attenuation factor.
4. Finite internal waiting times: crossovers, not a derived asymptotic \(d_s=\ln 8\).
5. Counting \(zM=8\) as if it were \(b_{\mathrm{dyn}}\).

Negative controls are the content of this stage.

---

## 9. The open problem (the missing bridge)

Define an explicit hierarchy \(T_n\) on scales \(L_{n+1}=2L_n\), each copy carrying \(\mathcal H_{\mathrm{int}}\simeq\mathbb C^2\), and a coarse-graining
\[
C_n:\mathcal H_n\to\mathcal H_{n+1}
\]
built from tetrahedral incidence — not from a target number. Measure
\[
\sigma_i(C_n),\qquad q_{\mathrm{eff}}(L_n),\qquad d_w(L),\qquad d_s(L).
\]
Report whatever emerges.

The question is not “does \(q_{\mathrm{eff}}\) approach \(0.541\)?”. The question is whether *any* independently specified tetrahedral rule produces anomalous transport at all.

Even a positive answer for \(d_s\) would still leave gravity open: a spectral dimension is not an effective Einstein equation.

---

## 10. Falsifiability

The present form of the \(\ln 8\) hypothesis fails if every physically motivated \(C_n\) yields
\[
d_w\to 2,\qquad d_s\to d_H.
\]
A value near \(\ln 8\) obtained only by imposing \(q_*\) or \(\theta\) is not a confirmation.

A genuine confirmation would have the shape
\[
\text{microscopic tetrahedral rules, fixed first}\;\longrightarrow\; d_w\text{ or }d_H\text{ measured}\;\longrightarrow\; d_s.
\]

---

## 11. Status of claims

| Item | Status |
|---|---|
| \(N_{\min}=4\) for a 3-simplex | Theorem |
| \(\dim\mathcal H_{\mathrm{int}}=2\) for four \(j=1/2\) | Theorem |
| \(F^\top F=I\) | Theorem |
| Local tetrahedral walk: \(d_w=2\) | Theorem (control) |
| Finite \(M\) + local finite range \(\not\Rightarrow d_s=\ln 8\) | Theorem (no-go) |
| \(zM=8\) as state count | Definition |
| \(b_{\mathrm{dyn}}=8\) | **Not shown** |
| \(d_s=\ln 8\) | **Hypothesis** |
| Programme A (\(d_H=3\), \(d_w\simeq 2.885\)) | Open |
| Programme B (\(d_H\simeq\ln 8\), \(d_w=2\)) | Open, distinct |
| Effective gravitational dynamics from either programme | Open |

---

## 12. Conclusion

Two facts stand:
\[
\text{3D + discrete + simplicial + minimal}\;\Rightarrow\;\text{tetrahedron},
\]
\[
\bigl(\tfrac12\bigr)^{\otimes 4}\text{ singlets}\;\Rightarrow\;\dim\mathcal H_{\mathrm{int}}=2.
\]
Their product is eight. Eight is not a spectral dimension.

\[
4\times 2=8 \;\not\Rightarrow\; d_s=\ln 8.
\]

The missing arrow is dynamical: a coarse-graining that turns internal multiplicity into anomalous transport (Programme A), or a derivation of reduced Hausdorff dimension (Programme B). Until one of those arrows is built and tested, \(d_s=\ln 8\) remains a hypothesis inside an incomplete framework.

Both a positive and a negative outcome of the next stage are useful. The value of the present note is that the hypothesis is now a precise question rather than an identification.

---

## Appendix. Core relations

\[
\begin{aligned}
N_{\min}&=4,\\
\dim\mathcal H_{\mathrm{int}}&=2,\\
zM&=8 \quad\text{(count, not }b_{\mathrm{dyn}}\text{)},\\
d_s&=2d_H/d_w,\\
d_H=3\text{ and }d_s=\ln 8 &\implies d_w=6/\ln 8\simeq 2.88539,\\
d_w=2+\theta &\implies \theta\simeq 0.88539,\\
q_*=2^{-\theta}&\simeq 0.54134 \quad\text{(diagnostic only)}.
\end{aligned}
\]

---

## Next writing task (not in this note)

- citations: Modesto; Ambjørn–Jurkiewicz–Loll; Sotiriou–Visser–Weinfurtner; heat-kernel literature on graphs;
- a short numerical \(P(0,t)\) on a finite tetrahedral graph \(\otimes\,\mathbb C^2\);
- one explicit candidate for \(C_n\), specified *before* looking at \(d_s\).
