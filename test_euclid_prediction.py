"""
TEG vH3.1 - Test de Falsación Euclid
Verifica si la predicción de TEG sobrevive los datos de Euclid

Autor: Miguel Ángel Franco León
Fecha: 2026-07-10
DOI: zenodo.org/records/211290...
"""

import math

# =============================================================================
# 1. PREDICCIONES TEG vH3.1 - CERO PARÁMETROS LIBRES
# =============================================================================

# Dark matter desde frustración geométrica: F = 2*ln(3/2)
OMEGA_DM_TEG = 2 * math.log(1.5) / 3 # = 0.270310

# Baryones desde BBN + CMB acoustic scale
OMEGA_B_BBN = 0.0490
OMEGA_B_ERR = 0.0010 # incertidumbre 1-sigma BBN

# Predicción total materia TEG
OMEGA_M_TEG = OMEGA_DM_TEG + OMEGA_B_BBN
OMEGA_M_TEG_ERR = OMEGA_B_ERR # solo viene de baryones, DM es exacto

# =============================================================================
# 2. REFERENCIA: ΛCDM Planck 2018 + Euclid Forecast
# =============================================================================

OMEGA_M_PLANCK = 0.315
OMEGA_M_PLANCK_ERR = 0.007

OMEGA_M_EUCLID_SIGMA = 0.0018 # Forecast Full Mission Euclid

# =============================================================================
# 3. TEST DE FALSACIÓN
# =============================================================================

def euclid_falsification_test(omega_m_measured, omega_m_err=OMEGA_M_EUCLID_SIGMA):
    """
    Retorna el veredicto de TEG dado un valor medido de Omega_m por Euclid.
    
    Returns: dict con sigma_tension, verdict, p_value
    """
    # Tensión con TEG
    delta_teg = abs(omega_m_measured - OMEGA_M_TEG)
    sigma_teg = delta_teg / math.sqrt(omega_m_err**2 + OMEGA_M_TEG_ERR**2)
    
    # Tensión con Planck ΛCDM
    delta_lcdm = abs(omega_m_measured - OMEGA_M_PLANCK)
    sigma_lcdm = delta_lcdm / math.sqrt(omega_m_err**2 + OMEGA_M_PLANCK_ERR**2)
    
    # Veredicto
    if sigma_teg > 3.0:
        verdict = "TEG RECHAZADA >3σ"
    elif sigma_teg > 2.0:
        verdict = "TEG EN TENSIÓN >2σ"
    elif sigma_lcdm > 2.0 and sigma_teg < 1.0:
        verdict = "TEG FAVORECIDA, ΛCDM EN TENSIÓN"
    elif sigma_teg < 1.0:
        verdict = "TEG CONSISTENTE <1σ"
    else:
        verdict = "INCONCLUSO"
    
    return {
        "omega_m_measured": omega_m_measured,
        "sigma_teg": sigma_teg,
        "sigma_lcdm": sigma_lcdm,
        "verdict": verdict
    }

# =============================================================================
# 4. REPORTE PRINCIPAL
# =============================================================================

def main():
    print("="*70)
    print("TEG vH3.1 - TEST DE FALSACIÓN EUCLID")
    print("="*70)
    print(f"\n1. PREDICCIÓN TEG:")
    print(f" Ω_DM = 2ln(3/2)/3 = {OMEGA_DM_TEG:.6f} [exacto]")
    print(f" Ω_b = BBN = {OMEGA_B_BBN:.4f} ± {OMEGA_B_ERR:.4f}")
    print(f" Ω_m^TEG = Ω_DM + Ω_b = {OMEGA_M_TEG:.4f} ± {OMEGA_M_TEG_ERR:.4f}")
    
    print(f"\n2. REFERENCIA ΛCDM:")
    print(f" Ω_m^Planck = {OMEGA_M_PLANCK:.3f} ± {OMEGA_M_PLANCK_ERR:.3f}")
    
    print(f"\n3. SEPARACIÓN PREDICHA:")
    delta = OMEGA_M_TEG - OMEGA_M_PLANCK
    sigma_current = delta / math.sqrt(OMEGA_M_TEG_ERR**2 + OMEGA_M_PLANCK_ERR**2)
    sigma_euclid = delta / OMEGA_M_EUCLID_SIGMA
    print(f" Δ = TEG - Planck = {delta:+.4f}")
    print(f" Tensión actual = {sigma_current:.1f}σ")
    print(f" Tensión con Euclid Full = {sigma_euclid:.1f}σ")
    
    print(f"\n4. UMBRALES DE FALSACIÓN con Euclid σ={OMEGA_M_EUCLID_SIGMA}:")
    threshold_2sigma_low = OMEGA_M_TEG - 2*math.sqrt(OMEGA_M_EUCLID_SIGMA**2 + OMEGA_M_TEG_ERR**2)
    threshold_2sigma_high = OMEGA_M_TEG + 2*math.sqrt(OMEGA_M_EUCLID_SIGMA**2 + OMEGA_M_TEG_ERR**2)
    threshold_3sigma_low = OMEGA_M_TEG - 3*math.sqrt(OMEGA_M_EUCLID_SIGMA**2 + OMEGA_M_TEG_ERR**2)
    
    print(f" Si Euclid mide < {threshold_3sigma_low:.4f} → TEG RECHAZADA >3σ")
    print(f" Si Euclid mide < {threshold_2sigma_low:.4f} → TEG EN TENSIÓN >2σ")
    print(f" Si Euclid mide > {threshold_2sigma_high:.4f} → ΛCDM EN TENSIÓN >2σ")
    print(f" Si {threshold_2sigma_low:.4f} < Euclid < {threshold_2sigma_high:.4f} → TEG OK")
    
    print(f"\n5. TESTS RÁPIDOS:")
    for test_val in [0.314, 0.315, 0.318, 0.3193, 0.322]:
        res = euclid_falsification_test(test_val)
        print(f" Euclid = {test_val:.4f} → {res['verdict']:30s} "
              f"(TEG: {res['sigma_teg']:.1f}σ, ΛCDM: {res['sigma_lcdm']:.1f}σ)")
    
    print("\n" + "="*70)
    print("La verdad no pide permiso. Solo verificación.")
    print("Repo: github.com/MiguelAngelFrancoLeon/mfsu-tetraedro")
    print("="*70)

if __name__ == "__main__":
    main()
