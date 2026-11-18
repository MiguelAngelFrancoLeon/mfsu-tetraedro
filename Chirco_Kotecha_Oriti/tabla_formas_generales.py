"""
Tabla con formas generales: sigma_n = ln D_n(j) / k_n^max.

K_MAX son los volúmenes máximos a áreas de cara iguales (a = 1):
  n=4: tetraedro regular                (analítico)
  n=5: prisma triangular, caras iguales (analítico)
  n=6: cubo                              (analítico)
  n=7: prisma pentagonal, caras iguales (analítico)
  n=8: óptimo numérico de volumen_maximo.py (dos semillas coinciden: 1.6795)
Los valores de n=5 y n=7 coinciden con los hallados por el optimizador numérico.

Uso:  python tabla_formas_generales.py
"""
from fractions import Fraction as F
from math import log, sqrt
from intertwiners import dim_inv

s3, s5 = sqrt(3), sqrt(5)
A_PENT = 0.25 * sqrt(25 + 10 * s5)         # área del pentágono regular de lado 1

K_MAX = {
    4: (4 / s3) ** 1.5 / (6 * sqrt(2)),
    5: sqrt(s3 / 4),                       # V = h = 1/s, con s^2 sqrt(3)/4 = 1
    6: 1.0,
    7: sqrt(A_PENT),                       # V = h = 1/s, con A_PENT s^2 = 1
    8: 1.6795,                             # numérico
}

if __name__ == "__main__":
    print("k_max:", {n: round(k, 4) for n, k in K_MAX.items()})
    print("\n  n    k_max    j=1/2    j=1    j=3/2")
    for n, k in K_MAX.items():
        row = []
        for j in (F(1, 2), F(1), F(3, 2)):
            D = dim_inv(n, j)
            row.append(f"{log(D)/k:7.3f}" if D else "    ---")
        print(f" {n:2d}   {k:6.4f}  " + "  ".join(row))
