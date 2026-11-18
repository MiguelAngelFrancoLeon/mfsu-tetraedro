"""
Volumen máximo de un poliedro convexo de n caras con TODAS las caras de área 1.

Formulación: normales unitarias N_i y números de soporte h_i definen
P = {x : N_i . x <= h_i}. Se maximiza V(P) sujeto a area(cara_i) = 1 para todo i
(SLSQP, varios puntos de partida aleatorios). El resultado k_max = V / a^{3/2}
con a = 1.

Chequeos internos: el politopo debe ser acotado, lo que se verifica con
V = (1/3) sum_i h_i A_i  y  sum_i A_i N_i = 0.

Los óptimos son LOCALES (mejor entre los puntos de partida); no se demuestra
optimalidad global. Validación: n=4 -> 0.4136 (tetraedro regular),
n=6 -> 1.0000 (cubo).

Uso:  python volumen_maximo.py n n_inicios [semilla]
      p. ej.  python volumen_maximo.py 6 40
Requiere numpy y scipy. Para n >= 7 puede tardar varios minutos.
"""
import sys
import numpy as np
from scipy.spatial import HalfspaceIntersection, ConvexHull
from scipy.optimize import minimize


def normales(ang, n):
    th, ph = ang[:n], ang[n:2 * n]
    return np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], 1)


def geometria(x, n):
    """Devuelve (volumen, áreas de cara) o None si la configuración no es válida."""
    N = normales(x[:2 * n], n)
    h = x[2 * n:]
    if np.any(h <= 1e-3):
        return None
    H = np.hstack([N, -h[:, None]])
    try:
        v = HalfspaceIntersection(H, np.zeros(3)).intersections
        if not np.all(np.isfinite(v)):
            return None
        V = ConvexHull(v).volume
    except Exception:
        return None
    A = np.zeros(n)
    for i in range(n):
        p = v[np.abs(v @ N[i] - h[i]) < 1e-7]
        if len(p) < 3:
            continue
        a = np.cross(N[i], [1, 0, 0])
        if np.linalg.norm(a) < 1e-6:
            a = np.cross(N[i], [0, 1, 0])
        a /= np.linalg.norm(a)
        b = np.cross(N[i], a)
        try:
            A[i] = ConvexHull(np.stack([p @ a, p @ b], 1)).volume
        except Exception:
            A[i] = 0
    if abs(V - np.dot(h, A) / 3) > 1e-6 * max(V, 1e-9) or \
            np.linalg.norm((A[:, None] * N).sum(0)) > 1e-5:
        return None
    return V, A


def maximizar(n, inicios, semilla=0):
    rng = np.random.default_rng(semilla)
    mejor = None
    for s in range(inicios):
        Nr = rng.normal(size=(n, 3))
        Nr /= np.linalg.norm(Nr, axis=1)[:, None]
        x0 = np.concatenate([np.arccos(np.clip(Nr[:, 2], -1, 1)),
                             np.arctan2(Nr[:, 1], Nr[:, 0]), np.full(n, 0.8)])

        def obj(x):
            g = geometria(x, n)
            return 1e3 if g is None else -g[0]

        def con(x):
            g = geometria(x, n)
            return np.full(n, -10.0) if g is None else g[1] - 1.0

        try:
            r = minimize(obj, x0, method="SLSQP",
                         constraints=[{"type": "eq", "fun": con}],
                         options={"maxiter": 300, "ftol": 1e-10})
        except Exception:
            continue
        g = geometria(r.x, n)
        if g is None:
            continue
        V, A = g
        if np.max(np.abs(A - 1)) < 1e-5 and (mejor is None or V > mejor[0]):
            mejor = (V, A.copy(), r.x.copy())
            print(f"n={n} semilla={semilla} inicio={s} k={V:.4f}", flush=True)
    return mejor


if __name__ == "__main__":
    n = int(sys.argv[1])
    inicios = int(sys.argv[2])
    semilla = int(sys.argv[3]) if len(sys.argv) > 3 else n
    b = maximizar(n, inicios, semilla)
    if b is None:
        print(f"n={n}: sin solución factible entre los {inicios} inicios")
    else:
        print(f"n={n}: k_max = {b[0]:.4f}   áreas = {np.round(b[1], 4)}")
