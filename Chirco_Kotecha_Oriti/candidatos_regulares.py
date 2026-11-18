"""
Candidatos de costo A y B con poliedros REGULARES como representantes
clásicos del volumen, V_n = k_n * a^{3/2} (a = área de cada cara).

  Candidato A: sigma_n = ln D_n(j) / k_n   (entropía por volumen a área fija;
               a j fijo las unidades de a se cancelan en la comparación).
  Candidato B: volumen fijo V0; a_n = (V0/k_n)^{2/3}; S ~ (2n-6) ln a_n
               (régimen semiclásico, unidades en que el área mínima es 1).

Uso:  python candidatos_regulares.py
"""
from fractions import Fraction as F
from math import log, sqrt
from intertwiners import dim_inv

s3, s5 = sqrt(3), sqrt(5)

# k_n = V / a^{3/2} para poliedros regulares con n caras
K_REG = {
    4: (4 / s3) ** 1.5 / (6 * sqrt(2)),                      # tetraedro
    6: 1.0,                                                   # cubo
    8: sqrt(2) / 3 * (4 / s3) ** 1.5,                         # octaedro
    12: (15 + 7 * s5) / 4 * (1 / (0.25 * sqrt(25 + 10 * s5))) ** 1.5,  # dodecaedro
    20: 5 * (3 + s5) / 12 * (4 / s3) ** 1.5,                  # icosaedro
}

if __name__ == "__main__":
    print("k_n (V = k_n a^{3/2}):", {n: round(k, 4) for n, k in K_REG.items()})

    print("\nCandidato A (poliedros regulares): sigma_n = ln D_n(j)/k_n")
    print("  n    j=1/2    j=1    j=3/2    (2n-6)/k_n")
    for n, k in K_REG.items():
        row = []
        for j in (F(1, 2), F(1), F(3, 2)):
            D = dim_inv(n, j)
            row.append(f"{log(D)/k:7.3f}" if D else "    ---")
        print(f" {n:2d}  " + "  ".join(row) + f"   {(2*n-6)/k:7.3f}")

    print("\nCandidato B (volumen fijo): S ~ (2n-6) ln a_n, a_n = (V0/k_n)^(2/3)")
    for V0 in (1e2, 1e3, 1e6):
        vals = ", ".join(f"n={n}: {(2*n-6)*log((V0/k)**(2/3)):.1f}" for n, k in K_REG.items())
        print(f"  V0={V0:g}:  {vals}")
