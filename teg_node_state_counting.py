#!/usr/bin/env python3
"""
TEG - conteo de estados de un nodo y lectura geometrica de las 8 etiquetas.

Reproduce los resultados del anexo "Node state counting and a geometric reading
of the 8 labels" (borrador preliminar). Solo necesita numpy.

  Parte 1  Nodo z-valente (LQG): dimension del espacio de intertwiners SU(2)
           (diagonalizando el Casimir total) vs. entropia de etiquetas de TEG.
  Parte 2  Geometria: las 8 etiquetas (cara, entra/sale) = vectores +-n_i
           = 8 vertices de un cubo = 3 bits de signo; paridad = orientacion.
  Parte 3  Candidato A: descomposicion de las 8 etiquetas en irreps de Td.
  Parte 4  Candidato B: entropias conjunta y marginales por eje.
  Parte 5  Que factorizacion en bits es invariante bajo Td; accion de S3.

Cada comprobacion imprime PASS/FAIL. No se ajusta ningun parametro.
"""
import itertools
from math import comb, log
import numpy as np

results = []
def check(name, ok):
    results.append(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

# ------------------------------------------------------------------ Parte 1
def spin_mats(j):
    d = int(round(2 * j + 1)); m = np.arange(j, -j - 1, -1)
    sz = np.diag(m).astype(complex)
    sp = np.zeros((d, d), complex)
    for k in range(1, d):
        sp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    return (sp + sp.conj().T) / 2, (sp - sp.conj().T) / (2j), sz

def kron_op(m, k, n, d):
    out = np.eye(1)
    for i in range(n):
        out = np.kron(out, m if i == k else np.eye(d))
    return out

def n_invariants(j, n):
    """Dimension del subespacio SU(2)-invariante de n patas de spin j (nucleo del Casimir total)."""
    d = int(round(2 * j + 1)); S = spin_mats(j)
    J = [sum(kron_op(s, k, n, d) for k in range(n)) for s in S]
    C = sum(x @ x for x in J)
    return int(np.sum(np.abs(np.linalg.eigvalsh(C)) < 1e-8))

catalan = lambda k: comb(2 * k, k) // (k + 1)

print("=== Parte 1: nodo z-valente, patas de spin 1/2 ===")
print("  z | invariantes | Catalan(z/2) | S_LQG=ln(inv) | TEG D_V=ln(2z)")
for z in [2, 3, 4, 5, 6, 8, 10]:
    inv = n_invariants(0.5, z)
    expected = catalan(z // 2) if z % 2 == 0 else 0
    s = f"{log(inv):.4f}" if inv else "  --  "
    print(f" {z:>2} | {inv:>11} | {expected:>12} | {s:>13} | {log(2 * z):.4f}")
    assert inv == expected
check("invariantes = Catalan(z/2) para z par, 0 para z impar (z<=10)", True)

print("\n  Nodo 4-valente, las 4 patas con el mismo spin j:")
for j in [0.5, 1, 1.5, 2]:
    inv = n_invariants(j, 4)
    print(f"   j={j:<3} invariantes={inv}  (2j+1={int(round(2*j+1))})  S=ln={log(inv):.4f}")
    assert inv == int(round(2 * j + 1))
check("z=4, spines iguales: dimension = 2j+1  (ln4 <-> j=3/2, ln8 <-> j=7/2)", True)

# ------------------------------------------------------------------ Parte 2
print("\n=== Parte 2: geometria de las 8 etiquetas ===")
V = np.array([v for v in itertools.product([1, -1], repeat=3) if np.prod(v) == 1], float)
dist = {round(float(np.linalg.norm(V[i] - V[j])), 9) for i in range(4) for j in range(i + 1, 4)}
check(f"los 4 vertices forman un tetraedro regular (arista unica = {sorted(dist)[0]:.4f} = 2*sqrt(2))",
      len(dist) == 1 and abs(sorted(dist)[0] - 2 * np.sqrt(2)) < 1e-9)

ok_normals = True
for i in range(4):
    face = [V[j] for j in range(4) if j != i]
    n = np.cross(face[1] - face[0], face[2] - face[0]); n /= np.linalg.norm(n)
    out = n if np.dot(n, face[0]) > 0 else -n            # saliente: apunta lejos del centro
    ok_normals &= np.allclose(out, -V[i] / np.linalg.norm(V[i]))
check("normal saliente de la cara opuesta al vertice i = -v_i (entrante = +v_i)", ok_normals)
check("las 4 normales cierran (suma = 0)", np.allclose((-V).sum(0), 0))

labels = [(f"cara{i}", "sale", tuple((-V[i]).astype(int))) for i in range(4)] + \
         [(f"cara{i}", "entra", tuple(V[i].astype(int))) for i in range(4)]
cube = set(itertools.product([1, -1], repeat=3))
check("las 8 etiquetas (cara, in/out) = los 8 vertices del cubo (3 signos)", {l[2] for l in labels} == cube)
check("paridad del producto de signos = orientacion (sale <-> -1)",
      all((int(np.prod(l[2])) == -1) == (l[1] == "sale") for l in labels))

# ------------------------------------------------------------------ Parte 3
print("\n=== Parte 3: Candidato A - irreps de Td en las 8 etiquetas ===")
Td = []
for p in itertools.permutations(range(3)):
    for s in itertools.product([1, -1], repeat=3):
        if np.prod(s) == 1:
            M = np.zeros((3, 3))
            for r in range(3):
                M[r, p[r]] = s[r]
            Td.append(M)
check("|Td| = 24", len(Td) == 24)
vecs = [np.array(v, float) for v in sorted(cube)]
idx = {tuple(v.astype(int)): k for k, v in enumerate(vecs)}
perm_of = lambda M: [idx[tuple(np.round(M @ v).astype(int))] for v in vecs]
parity = lambda v: int(np.prod(v))
check("Td preserva la paridad (no intercambia entra/sale)",
      all(all(parity(vecs[k]) == parity(vecs[pk]) for k, pk in enumerate(perm_of(M))) for M in Td))

table = {'A1': [1, 1, 1, 1, 1], 'A2': [1, 1, 1, -1, -1], 'E': [2, -1, 2, 0, 0],
         'T1': [3, 0, -1, 1, -1], 'T2': [3, 0, -1, -1, 1]}       # clases: E, 8C3, 3C2, 6S4, 6sd
cls = {(3, 1): 0, (0, 1): 1, (-1, 1): 2, (-1, -1): 3, (1, -1): 4}; size = [1, 8, 3, 6, 6]
chi = np.zeros(5)
for M in Td:
    c = cls[(int(round(np.trace(M))), int(round(np.linalg.det(M))))]
    chi[c] += sum(1 for k, pk in enumerate(perm_of(M)) if pk == k)
chi /= np.array(size)
mult = {n: round(sum(size[c] * chi[c] * t[c] for c in range(5)) / 24, 6) for n, t in table.items()}
dec = {n: int(m) for n, m in mult.items() if m > 0.5}
print(f"  8 etiquetas = {dec}  (T2 = representacion vectorial de R^3)")
check("descomposicion = 2*A1 + 2*T2 (dims 2 + 6)", dec == {'A1': 2, 'T2': 2})
print(f"  Si las 3 direcciones se asignan solo a T2: S = ln 6 = {log(6):.4f}  != ln 8 = {log(8):.4f}")

# ------------------------------------------------------------------ Parte 4
print("\n=== Parte 4: Candidato B - 3 bits de signo ===")
states = sorted(cube)
def H(p):
    p = np.array([x for x in p if x > 0]); return float(-(p * np.log(p)).sum())
def marg(p, axis):
    q = {1: 0., -1: 0.}
    for pk, v in zip(p, states):
        q[v[axis]] += pk
    return list(q.values())
bulk = np.ones(8) / 8
even = np.array([1.0 if np.prod(v) == 1 else 0 for v in states]); even /= even.sum()
for name, p, expected in [("bulk (8 etiquetas)", bulk, log(8)), ("superficie (1 orientacion)", even, log(4))]:
    Hj = H(p); Hm = [H(marg(p, a)) for a in range(3)]
    print(f"  {name}: H conjunta={Hj:.4f}; marginales por eje={[round(h, 4) for h in Hm]}; info mutua={sum(Hm) - Hj:.4f}")
    check(f"H conjunta de {name} = {'ln 8' if expected == log(8) else 'ln 4'}", abs(Hj - expected) < 1e-9)
check("D_V - D_A = ln 2 = 1 bit (la paridad)", abs((log(8) - log(4)) - log(2)) < 1e-12)

# ------------------------------------------------------------------ Parte 5
print("\n=== Parte 5: simetria y factorizacion en bits ===")
fx = [np.array([v[a] for v in vecs]) for a in range(3)]            # bits de ejes
p_fn = np.array([np.prod(v) for v in vecs])
alt = [fx[0], fx[1], p_fn]                                          # cara(s_x,s_y) + orientacion
same = lambda f, g: np.array_equal(f, g) or np.array_equal(f, -g)
act = lambda f, M: np.array([f[perm_of(M)[k]] for k in range(8)])
inv_axes = all(any(same(act(f, M), g) for g in fx) for f in fx for M in Td)
inv_alt = all(any(same(act(f, M), g) for g in alt) for f in alt for M in Td)
check("factorizacion en bits de EJES invariante bajo Td", inv_axes)
check("factorizacion 'cara (2 bits) + orientacion (1 bit)' NO invariante bajo Td", not inv_alt)
orbit = {int(np.argmax(np.abs(M[r]))) for M in Td for r in [0]}
check("S3 mueve el bit x a los tres ejes (transitivo => pesos iguales 1/3)", orbit == {0, 1, 2})

print("\n=== Resumen ===")
print(f"  {sum(results)}/{len(results)} comprobaciones PASS")
print("  Nota: esto verifica estructura geometrica/algebraica. No deriva sigma_UV,")
print("  ni la hipotesis aditiva de reparto, ni nada sobre curvas de rotacion.")
