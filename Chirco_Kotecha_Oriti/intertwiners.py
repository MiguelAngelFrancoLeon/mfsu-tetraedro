"""
Dimensión del espacio de intertwiners D_n(j) = dim Inv(V_j^{(x) n}) y entropía
del estado maximalmente mezclado S = ln D_n(j).

D_n(j) es la multiplicidad del espín total 0 en el producto de n copias de la
representación de espín j de SU(2). Se calcula por recursión exacta (enteros).

Uso:  python intertwiners.py
"""
from fractions import Fraction as F
from math import log
from collections import defaultdict


def dim_inv(n, j):
    """Multiplicidad de espín total 0 en n copias de V_j (j: Fraction)."""
    d = {F(0): 1}
    for _ in range(n):
        nd = defaultdict(int)
        for J, m in d.items():
            k = abs(J - j)
            while k <= J + j:
                nd[k] += m
                k += 1
        d = nd
    return d.get(F(0), 0)


def entropia(n, j):
    """S = ln D_n(j); None si el espacio es vacío."""
    D = dim_inv(n, j)
    return log(D) if D > 0 else None


if __name__ == "__main__":
    print("Tabla 1: D_n(j) y S/n (estado maximalmente mezclado)")
    for j in (F(1, 2), F(1)):
        print(f"\n j = {j}")
        print("  n   D_n    S/n")
        for n in (4, 5, 6, 7, 8, 10):
            D = dim_inv(n, j)
            if D == 0:
                print(f"  {n:2d}   ---    ---   (espacio vacío)")
            else:
                print(f"  {n:2d}  {D:5d}  {log(D)/n:6.3f}")
