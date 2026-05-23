# Tetrahedral Emergent Gravity (TEG) — SPARC z-sweep

**Franco León (2026)**  
https://github.com/MiguelAngelFrancoLeon/mfsu-tetraedro

---

## What this notebook does

Sweeps the coordination number `z ∈ {3, 4, 5, 6, 8}` and measures
which geometry best fits the **175 SPARC galaxy rotation curves**
using **zero free parameters** — every quantity is derived from the tetrahedral axiom.

**Expected result:** `z = 4` (tetrahedron) achieves the lowest RMSE ≈ 0.15 dex.

---

### Formula (paper eq. 4.1 — authoritative)

$$V^2_{\text{bar}} = \frac{G M_b}{r} \cdot \Phi \cdot [1 - s_{\text{eff}} F(N)] \cdot \left(\frac{r}{r_{\text{ref}}}\right)^{(D_{\text{eff}}-2)/2}$$

$$V^2_{\text{vac}} = G \ln 2 \cdot M_{b,\text{tot}} \cdot \frac{r^2}{r_{\text{max}}^3}$$

All parameters derived — none fitted to data.

| Symbol | Definition | Value at z=4 |
|--------|-----------|-------------|
| $\Phi$ | $\ln z$ | $\ln 4 \approx 1.386$ |
| $D_{\text{eff}}$ | $\ln 2z$ | $\ln 8 \approx 2.079$ |
| $s_{\text{UV}}$ | $2\ln(z_{\text{pack}}/(z_{\text{pack}}-z))/\ln z_{\text{pack}}$ | derived |
| $N_{\text{bits}}$ | $\log_2(2z)$ | **exactly 3** (only for z=4) |
| $s_{\text{eff}}$ | $s_{\text{UV}} / N_{\text{bits}}$ | $\approx 0.1088$ |
| $\ln 2$ | holographic bit $D_V - D_A$ | universal |


## 1 · Setup

# Install dependencies
!pip install numpy matplotlib tqdm requests -q
print('Dependencies ready.')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import glob, os, sys, requests, zipfile, io
from tqdm.notebook import tqdm
print('Imports OK.')

## 2 · Download SPARC data

SPARC (Spitzer Photometry & Accurate Rotation Curves) — Lelli et al. 2016  
http://astroweb.cwru.edu/SPARC/

175 galaxies with photometry + observed rotation curves.
The download is ~2 MB and takes a few seconds.

SPARC_DIR = '/content/sparc_data'
os.makedirs(SPARC_DIR, exist_ok=True)

# Check if already downloaded
existing = glob.glob(os.path.join(SPARC_DIR, '*_rotmod.dat'))

if len(existing) >= 100:
    print(f'SPARC data already present: {len(existing)} files.')
else:
    print('Downloading SPARC rotation curve data...')
    # Individual file list from SPARC website
    SPARC_BASE = 'http://astroweb.cwru.edu/SPARC/'

    # Try to get the file listing
    try:
        r = requests.get(SPARC_BASE, timeout=15)
        import re
        filenames = re.findall(r'href="([^"]+_rotmod\.dat)"', r.text)

        if not filenames:
            raise ValueError('Could not parse file listing')

        print(f'Found {len(filenames)} rotation curve files. Downloading...')
        failed = []
        for fname in tqdm(filenames):
            url  = SPARC_BASE + fname
            dest = os.path.join(SPARC_DIR, os.path.basename(fname))
            if not os.path.exists(dest):
                try:
                    resp = requests.get(url, timeout=10)
                    if resp.status_code == 200:
                        with open(dest, 'wb') as f:
                            f.write(resp.content)
                    else:
                        failed.append(fname)
                except Exception:
                    failed.append(fname)

        downloaded = glob.glob(os.path.join(SPARC_DIR, '*_rotmod.dat'))
        print(f'Downloaded: {len(downloaded)} files. Failed: {len(failed)}')

    except Exception as e:
        print(f'Auto-download failed: {e}')
        print()
        print('Manual download instructions:')
        print('  1. Go to: http://astroweb.cwru.edu/SPARC/')
        print('  2. Download all *_rotmod.dat files')
        print('  3. Upload them to Colab in /content/sparc_data/')
        print('     OR use: files.upload() in a new cell')

files = glob.glob(os.path.join(SPARC_DIR, '*_rotmod.dat'))
print(f'\nTotal SPARC files available: {len(files)}')

### 2b · Manual upload (if auto-download failed)

# Run this cell ONLY if automatic download failed
# It opens a file picker to upload your *_rotmod.dat files manually

MANUAL_UPLOAD = False   # Set to True to activate

if MANUAL_UPLOAD:
    from google.colab import files
    uploaded = files.upload()
    for fname, content in uploaded.items():
        dest = os.path.join(SPARC_DIR, fname)
        with open(dest, 'wb') as f:
            f.write(content)
    print(f'Uploaded {len(uploaded)} files.')
    files_now = glob.glob(os.path.join(SPARC_DIR, '*_rotmod.dat'))
    print(f'Total now: {len(files_now)}')
else:
    print('Skipped — set MANUAL_UPLOAD = True if needed.')

## 3 · Physical constants and derived parameters

import os
import sys
import subprocess
import shutil

# Definimos las rutas exactas dentro del entorno de Google Colab
BASE_DIR = "/content"
DATA_DIR = os.path.join(BASE_DIR, "sparc_data")

print("📥 Sincronizando base de datos SPARC desde el repositorio espejo...")

# 1. Limpieza de seguridad para evitar conflictos si la carpeta ya existía rota
if os.path.exists(DATA_DIR):
    try:
        shutil.rmtree(DATA_DIR)
    except Exception as e:
        # Si Windows o Colab tienen bloqueado el directorio, usamos comando de sistema
        os.system(f"rm -rf {DATA_DIR}")

# 2. SENTENCIA DE DESCARGA: Ejecución directa y controlada del clon de Git
repo_url = "https://github.com/carsondowns-cte/Rotmod_LTG"
try:
    subprocess.run(["git", "clone", repo_url, DATA_DIR], check=True, capture_output=True)
except subprocess.CalledProcessError as e:
    print(f"❌ Error al clonar el repositorio: {e.stderr.decode()}")
    sys.exit(1)

# 3. Forzar el refresco del directorio de trabajo en la máquina virtual
if os.path.exists(DATA_DIR):
    # Listamos y filtramos los archivos *.dat de las galaxias long-term (LTG)
    all_files = os.listdir(DATA_DIR)
    sparc_files = [f for f in all_files if f.endswith('_rotmod.dat')]

    print("-" * 60)
    print(f"✅ ¡Sincronización exitosa en Google Colab!")
    print(f"   Directorio local: {DATA_DIR}")
    print(f"   Total de curvas de rotación detectadas: {len(sparc_files)}")
    print(f"   Primeras galaxias listas: {sparc_files[:3]}")
    print("-" * 60)
else:
    print("❌ Error crítico: La carpeta no se materializó en el disco de Colab.")



# ── Physical constants ────────────────────────────────────────
G      = 4.302e-6   # kpc * (km/s)^2 / Msun
z_pack = 12         # Newton-Gregory kissing number in R^3

# ── External scales (documented limitation — not fitted, not derived) ─────
N0    = 1.5         # saturation scale; stable for N0 in [1, 2]
M_J   = 1e6         # Msun — reference Jeans mass
r_ref = 1.0         # kpc  — unit-fixing convention

# ── Derived quantities (zero free parameters) ─────────────────
def sigma_UV(z):
    """Geometric frustration: s_UV = 2*ln(z_pack/(z_pack-z)) / ln(z_pack)"""
    return 2.0 * np.log(z_pack / (z_pack - z)) / np.log(z_pack)

def N_bits(z):
    """log2(2z) — exact integer 3 ONLY for z=4"""
    return np.log(2.0 * z) / np.log(2.0)

def sigma_eff(z):
    """s_eff = s_UV / N_bits"""
    return sigma_UV(z) / N_bits(z)

def F(N):
    """Saturation: F(N) = 1 - exp(-N/N0)"""
    return 1.0 - np.exp(-N / N0)

# ── Print derivation chain ────────────────────────────────────
z_values = [3, 4, 5, 6, 8]
geom     = {3:'Triangle', 4:'Tetrahedron', 5:'Trigonal bipyramid',
            6:'Octahedron', 8:'Cube'}

print(f'{'z':>3}  {"Geometry":<22} {"sigma_UV":>10} {"N_bits":>8} {"sigma_eff":>11}')
print('-' * 58)
for z in z_values:
    marker = ' ← z=4: N_bits=3 exactly' if z == 4 else ''
    print(f'{z:>3}  {geom[z]:<22} {sigma_UV(z):>10.4f} '
          f'{N_bits(z):>8.4f} {sigma_eff(z):>11.4f}{marker}')

## 4 · SPARC data loader

def load_galaxy(filepath):
    """
    Load one SPARC *_rotmod.dat file.
    Columns: r, Vobs, errV, Vgas, Vdisk, Vbul, SBdisk, SBbul
    Returns (r, Vobs, Mb) or None on quality cut (< 5 points).
    """
    try:
        d = np.loadtxt(filepath, comments='#')
    except Exception:
        return None

    if d.ndim < 2 or len(d) < 5:
        return None

    r    = d[:, 0]   # kpc
    Vobs = d[:, 1]   # km/s

    # Baryonic mass from quadrature of SPARC velocity components
    Mb = (d[:, 3]**2 + d[:, 4]**2 + d[:, 5]**2) * r / G
    Mb = np.maximum(Mb, M_J * 1.1)   # floor at 1.1*M_J

    mask = (r > 0) & (Vobs > 0) & (Mb > 0)
    if mask.sum() < 5:
        return None

    return r[mask], Vobs[mask], Mb[mask]


# Load all galaxies
all_files  = sorted(glob.glob(os.path.join(SPARC_DIR, '*_rotmod.dat')))
galaxies   = [(f, load_galaxy(f)) for f in all_files]
galaxies   = [(f, g) for f, g in galaxies if g is not None]
n_fail     = len(all_files) - len(galaxies)

print(f'Files found  : {len(all_files)}')
print(f'Loaded OK    : {len(galaxies)}')
print(f'Quality cut  : {n_fail}')

## 5 · Velocity prediction (eq. 4.1)

def v_pred(r, Mb, z):
    """
    Total rotation velocity — paper equation 4.1 (authoritative).

    Baryonic:
        V²_bar = G*Mb/r * Phi * [1 - s_eff*F(N)] * (r/r_ref)^((D_eff-2)/2)

    Vacuum entropy (cubic profile, coefficient ln2 = D_V - D_A):
        V²_vac = G * ln2 * Mb_tot * r^2 / r_max^3
    """
    sig  = sigma_eff(z)
    Phi  = np.log(float(z))        # tetrahedral surface entropy
    Deff = np.log(2.0 * z)         # orientation duality

    N = np.log10(Mb / M_J)

    # Baryonic — eq. 4.1
    ampl   = Phi * (1.0 - sig * F(N)) * (r / r_ref) ** ((Deff - 2.0) / 2.0)
    V2_bar = np.maximum(G * Mb / r * ampl, 0.0)

    # Vacuum entropy
    Mb_tot = Mb[-1]
    r_max  = r[-1]
    V2_vac = np.maximum(G * np.log(2.0) * Mb_tot * r**2 / r_max**3, 0.0)

    return np.sqrt(V2_bar + V2_vac)

print('v_pred() defined — equation 4.1 (authoritative form).')

## 6 · z-sweep — main result

results    = {}
residuals  = {}

print(f'Running z-sweep over {len(galaxies)} galaxies...\n')
print(f'{"z":>3}  {"Geometry":<22} {"sigma_eff":>10}  '
      f'{"RMSE (dex)":>11}  {"N_residuals":>13}')
print('─' * 65)

for z in z_values:
    res = []
    for _, (r, Vobs, Mb) in galaxies:
        Vp = v_pred(r, Mb, z)
        m  = Vp > 0
        if m.sum() > 2:
            res.extend(np.log10(Vobs[m] / Vp[m]).tolist())

    rmse         = np.sqrt(np.mean(np.array(res)**2))
    results[z]   = rmse
    residuals[z] = np.array(res)

    marker = ' ◄ MINIMUM' if z == min(results, key=results.get) else ''
    print(f'{z:>3}  {geom[z]:<22} {sigma_eff(z):>10.4f}  '
          f'{rmse:>11.4f}  {len(res):>13}{marker}')

print('─' * 65)
best_z = min(results, key=results.get)
print()

if best_z == 4:
    print(f'✓ PASS — z=4 achieves the lowest RMSE ({results[4]:.4f} dex).')
    print('  The tetrahedral axiom is consistent with SPARC data.')
else:
    print(f'✗ FAIL — z={best_z} achieves lowest RMSE ({results[best_z]:.4f} dex).')
    print('  z=4 does NOT win. The TEG framework must be revised.')

print()
print('Margins relative to z=4:')
for z in z_values:
    if z != 4:
        delta = results[z] - results[4]
        pct   = delta / results[4] * 100
        sign  = '+' if delta >= 0 else ''
        print(f'  z={z}: {sign}{delta:.4f} dex  ({sign}{pct:.1f}%)')

## 7 · Visualizations

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.patch.set_facecolor('#0d1117')
for ax in axes:
    ax.set_facecolor('#161b22')
    for sp in ax.spines.values():
        sp.set_color('#30363d')
    ax.tick_params(colors='#8b949e')
    ax.xaxis.label.set_color('#8b949e')
    ax.yaxis.label.set_color('#8b949e')
    ax.title.set_color('#e6edf3')

colors = {3:'#ff7b72', 4:'#3fb950', 5:'#58a6ff',
          6:'#d2a8ff', 8:'#ffa657'}

# ── Plot 1: RMSE bar chart ─────────────────────────────────────
ax = axes[0]
zs   = list(results.keys())
rmse = [results[z] for z in zs]
bars = ax.bar([str(z) for z in zs], rmse,
              color=[colors[z] for z in zs],
              edgecolor='#30363d', linewidth=0.8)
ax.axhline(results[4], color='#3fb950', linestyle='--',
           linewidth=1, alpha=0.6, label=f'z=4 baseline')
for bar, z, r in zip(bars, zs, rmse):
    ax.text(bar.get_x() + bar.get_width()/2,
            r + 0.002, f'{r:.3f}',
            ha='center', va='bottom',
            color=colors[z], fontsize=9, fontfamily='monospace')
ax.set_title('RMSE by coordination number z', fontsize=11, pad=10)
ax.set_xlabel('z')
ax.set_ylabel('RMSE (dex)')
ax.set_ylim(0, max(rmse)*1.15)
ax.legend(fontsize=8, facecolor='#161b22', edgecolor='#30363d',
          labelcolor='#8b949e')
ax.grid(axis='y', color='#21262d', linewidth=0.5)

# ── Plot 2: Residual distributions ────────────────────────────
ax = axes[1]
bins = np.linspace(-0.6, 0.6, 40)
for z in z_values:
    ax.hist(residuals[z], bins=bins, alpha=0.55,
            color=colors[z], label=f'z={z}',
            histtype='stepfilled', linewidth=0.5)
ax.axvline(0, color='white', linestyle='--', linewidth=0.8, alpha=0.5)
ax.set_title('Residual distributions', fontsize=11, pad=10)
ax.set_xlabel('log₁₀(V_obs / V_pred)')
ax.set_ylabel('Count')
ax.legend(fontsize=8, facecolor='#161b22', edgecolor='#30363d',
          labelcolor='#8b949e')
ax.grid(color='#21262d', linewidth=0.5)

# ── Plot 3: sigma_eff vs z ────────────────────────────────────
ax = axes[2]
z_cont  = np.linspace(2.5, 9, 200)
sig_cont= [sigma_eff(z) for z in z_cont]
ax.plot(z_cont, sig_cont, color='#58a6ff', linewidth=1.5, alpha=0.7)
for z in z_values:
    ax.scatter(z, sigma_eff(z), color=colors[z],
               s=80, zorder=5, edgecolors='white', linewidths=0.5)
    ax.annotate(f'z={z}\nσ={sigma_eff(z):.3f}',
                xy=(z, sigma_eff(z)),
                xytext=(8, 8), textcoords='offset points',
                color=colors[z], fontsize=8, fontfamily='monospace')
ax.set_title('Effective frustration σ_eff(z)', fontsize=11, pad=10)
ax.set_xlabel('z')
ax.set_ylabel('σ_eff = s_UV / N_bits')
ax.grid(color='#21262d', linewidth=0.5)

plt.suptitle('TEG z-sweep — SPARC 175 galaxies\n'
             'Franco León (2026) — zero free parameters',
             color='#e6edf3', fontsize=12, y=1.01)
plt.tight_layout()
plt.savefig('/content/teg_zsweep_results.png',
            dpi=150, bbox_inches='tight',
            facecolor='#0d1117')
plt.show()
print('Saved: /content/teg_zsweep_results.png')

## 8 · Sample rotation curves (z=4)

# Show first 9 galaxies sorted by number of data points
sample = sorted(galaxies, key=lambda x: -len(x[1][0]))[:9]

fig, axes = plt.subplots(3, 3, figsize=(14, 10))
fig.patch.set_facecolor('#0d1117')
axes = axes.flatten()

for ax, (fpath, (r, Vobs, Mb)) in zip(axes, sample):
    ax.set_facecolor('#161b22')
    for sp in ax.spines.values(): sp.set_color('#30363d')
    ax.tick_params(colors='#8b949e', labelsize=8)

    Vp = v_pred(r, Mb, z=4)

    ax.scatter(r, Vobs, color='#58a6ff', s=18,
               zorder=5, label='Observed', alpha=0.9)
    ax.plot(r, Vp, color='#3fb950', linewidth=1.8,
            label='TEG z=4', zorder=4)

    name = os.path.basename(fpath).replace('_rotmod.dat','')
    rmse_g = np.sqrt(np.mean(np.log10(Vobs/Vp)**2))
    ax.set_title(f'{name}  RMSE={rmse_g:.3f}',
                 color='#e6edf3', fontsize=9)
    ax.set_xlabel('r (kpc)', color='#8b949e', fontsize=8)
    ax.set_ylabel('V (km/s)', color='#8b949e', fontsize=8)
    ax.legend(fontsize=7, facecolor='#161b22',
              edgecolor='#30363d', labelcolor='#8b949e')
    ax.grid(color='#21262d', linewidth=0.4)

plt.suptitle('Sample rotation curves — TEG z=4 vs observations',
             color='#e6edf3', fontsize=12, y=1.01)
plt.tight_layout()
plt.savefig('/content/teg_sample_curves.png',
            dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.show()
print('Saved: /content/teg_sample_curves.png')

## 9 · Export results

import json

report = {
    'title'   : 'TEG z-sweep results — SPARC 175 galaxies',
    'paper'   : 'Franco León (2026) — Tetrahedral Emergent Gravity',
    'n_galaxies': len(galaxies),
    'pass'    : best_z == 4,
    'best_z'  : int(best_z),
    'parameters': {
        'N0': N0, 'M_J': M_J, 'r_ref': r_ref,
        'z_pack': z_pack,
        'note': 'N0, M_J, r_ref are external scales — '
                'not fitted, not derived from axiom'
    },
    'z_sweep': [
        {
            'z'        : z,
            'geometry' : geom[z],
            'sigma_UV' : round(float(sigma_UV(z)), 6),
            'N_bits'   : round(float(N_bits(z)), 6),
            'sigma_eff': round(float(sigma_eff(z)), 6),
            'RMSE_dex' : round(float(results[z]), 6),
            'delta_vs_z4': round(float(results[z] - results[4]), 6),
        }
        for z in z_values
    ]
}

with open('/content/teg_zsweep_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print('Report saved: /content/teg_zsweep_report.json')
print()
print(json.dumps(report, indent=2))

# Download all outputs to your local machine
from google.colab import files
for path in ['/content/teg_zsweep_results.png',
             '/content/teg_sample_curves.png',
             '/content/teg_zsweep_report.json']:
    if os.path.exists(path):
        files.download(path)
        print(f'Downloaded: {os.path.basename(path)}')

## Notes

### Formula correction (vs Appendix B)

- **Appendix B (incorrect):** `ampl = Phi × (1 - s·F/(1+s·F))`
- **Eq. 4.1 (this script, correct):** `ampl = Phi × (1 - s·F)`

The difference is 0.3–0.9% in amplitude. This script uses eq. 4.1.

### External scales (honest scope)

| Scale | Value | Origin |
|-------|-------|--------|
| `N0 = 1.5` | Saturation scale | Not derived from axiom — documented limitation |
| `M_J = 10⁶ M☉` | Reference Jeans mass | Not fitted — unit convention |
| `r_ref = 1 kpc` | Distance reference | Not fitted — unit convention |

### Reproducibility

If `z=4` does NOT achieve minimum RMSE on your SPARC download, the model must be revised.
The script prints `FAIL` explicitly in that case — no hidden passes.



