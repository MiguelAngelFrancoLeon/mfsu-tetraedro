# TEG at Solar-System Scales: Mercury perihelion as a consistency bound

Miguel Ángel Franco León  
Note (not a paper) · 31 August 2026  
Repo companion to TEG v8 and TEG-TN-2026-08

**Status.** Order-of-magnitude consistency check. TEG v8 does not supply a derived one-body force law at \(1\,\mathrm{AU}\). This note only asks whether the *already fixed* galactic scales of TEG leave room for Einstein’s Mercury result. It is not a perihelion prediction and not a fit.

---

## 1. What is being asked

GR accounts for Mercury’s anomalous perihelion advance:

\[
\Delta\omega_{\mathrm{GR}}
=\frac{6\pi GM_{\odot}}{c^{2}a(1-e^{2})}
\approx 42.98''/\mathrm{century}.
\]

The residual after GR is at the level of \(\lesssim 0.01''/\mathrm{century}\) in modern ephemerides. Any extra TEG force at \(a\simeq 0.387\,\mathrm{AU}\) has to sit below that residual. The question is whether the galactic TEG parameters already imply that, or whether they would ruin Mercury.

## 2. Scales that TEG has actually fixed

From TEG v8 (SPARC, no per-galaxy fit):

\[
r_J=0.62\,\mathrm{kpc},\qquad
\sigma_{\mathrm{eff}}=0.1088,\qquad
\partial=3-\ln 8.
\]

Convert:

\[
r_J\approx 1.91\times 10^{19}\,\mathrm{m}
\approx 1.28\times 10^{8}\,\mathrm{AU}.
\]

Mercury’s semi-major axis:

\[
a_{\Mercury}\approx 5.79\times 10^{10}\,\mathrm{m},
\qquad
\frac{a_{\Mercury}}{r_J}\approx 3.03\times 10^{-9}.
\]

Solar gravitational acceleration at Mercury:

\[
g=\frac{GM_{\odot}}{a^{2}}\approx 4.0\times 10^{-2}\,\mathrm{m\,s^{-2}}.
\]

The acceleration scale that appears in galactic interpolations of the MOND type (used here only as a *comparison*, not as a TEG axiom) is \(a_0\sim 1.2\times 10^{-10}\,\mathrm{m\,s^{-2}}\), so

\[
\frac{a_0}{g}\approx 3.0\times 10^{-9}.
\]

The two small numbers coincide in order of magnitude: Mercury sits \(\sim 10^{9}\) below the galactic scale of TEG, whether one talks in length or in acceleration.

## 3. What \(\sigma_{\mathrm{eff}}\) is not

\(\sigma_{\mathrm{eff}}=0.1088\) is a galactic roughness parameter. It is **not** a renormalization \(\delta G/G\) at every scale. If it were, Newtonian forces in the Solar System would be wrong at the \(10\%\) level and Mercury would already exclude TEG. That reading is not the v8 model and is not used here.

## 4. Scaling estimate

Assume, as a *bound*, that any extra TEG acceleration at radius \(r\ll r_J\) cannot be larger than the galactic amplitude suppressed by the scale ratio already in the theory:

\[
\left.\frac{\delta a}{a_N}\right|_{r}
\;\lesssim\;
\sigma_{\mathrm{eff}}\left(\frac{r}{r_J}\right)^{n},
\qquad n\geq 1.
\]

Then at Mercury

| suppression | \(\delta a/a_N\) | extra perihelion if it tracked a \(1/r^{2}\) term |
|---|---|---|
| \(n=1\) | \(\sim 3\times 10^{-10}\) | \(\sim 1\times 10^{-8}\,''/\mathrm{century}\) |
| \(n=2\) | \(\sim 1\times 10^{-18}\) | negligible |
| \(\sigma_{\mathrm{eff}}\,a_0/g\) | \(\sim 3\times 10^{-10}\) | \(\sim 1\times 10^{-8}\,''/\mathrm{century}\) |

GR is \(42.98''/\mathrm{century}\). The observational slack is \(\sim 10^{-2}\,''/\mathrm{century}\) or tighter. The scaling remainder is **four to ten orders smaller**. Cassini’s bound \(|\gamma-1|\lesssim 2\times 10^{-5}\) is likewise not challenged by a \(10^{-10}\) fractional correction at \(1\,\mathrm{AU}\).

Jupiter (\(5.2\,\mathrm{AU}\)) still has \(a/r_J\sim 4\times 10^{-8}\). The same conclusion holds for the whole planetary system. The first place where \(r/r_J\) stops being tiny is the outer Oort cloud / inner galactic environment, not the ephemerides.

## 5. What this does *not* prove

- It does not derive a TEG perihelion formula.
- It does not confirm \(z=4\).
- It does not replace SPARC or \(\partial\) as the test of the axiom.
- If a future version of TEG writes a Solar-System operator that is *not* suppressed by \(r/r_J\) or \(a_0/g\), this note is void and that operator must be checked against Mercury and Cassini directly.

## 6. Statement for the repo

> With the galactic scales already fixed by TEG v8, a scale-suppressed extra acceleration at Mercury is of order \(10^{-10}\) or smaller relative to Newton. That is many orders below the GR perihelion term and below present residuals. Einstein’s account of Mercury is left intact. The axiom is not tested in the inner Solar System; it is constrained not to disturb it. The live tests remain SPARC and \(\partial=3-\ln 8\).

No journal version is intended.
