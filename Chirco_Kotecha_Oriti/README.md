# Scripts de reproducibilidad — Nota técnica CKO–TEG (borrador preliminar)

Acompañan a la nota técnica *«Equilibrio estadístico de tetraedros
(Chirco–Kotecha–Oriti) y el axioma de coordinación tetraédrica en TEG:
compatibilidad conceptual y un contraste elemental»*. Con ellos pueden
reproducirse las cifras de las tablas de la sección 6.

**Alcance.** Los cálculos son un contraste elemental y exploratorio. No
constituyen una derivación ni una refutación del axioma z = 4 de TEG; sus
limitaciones se discuten en la sección «Limitaciones» de la nota.

## Requisitos

- Python 3.9 o superior
- `intertwiners.py`, `candidatos_regulares.py` y `tabla_formas_generales.py`:
  solo biblioteca estándar.
- `volumen_maximo.py`: `numpy` y `scipy`.

## Archivos

| Archivo | Qué calcula | Tabla de la nota |
|---|---|---|
| `intertwiners.py` | D_n(j) = dim Inv(V_j^{⊗n}) y S/n del estado maximalmente mezclado | Tabla 1 |
| `candidatos_regulares.py` | Candidato A (σ_n = ln D_n / k_n) y candidato B (volumen fijo) con poliedros regulares | Tabla 2 y valores del candidato B |
| `volumen_maximo.py` | Volumen máximo de un poliedro de n caras con todas las caras de área 1 | k_n^max de la Tabla 3 |
| `tabla_formas_generales.py` | σ_n con los volúmenes máximos | Tabla 3 |

Los cuatro scripts deben estar en la misma carpeta (los demás importan
`intertwiners.py`).

## Uso

```
python intertwiners.py
python candidatos_regulares.py
python tabla_formas_generales.py
python volumen_maximo.py 6 40        # n = 6, 40 puntos de partida
```

Salidas de referencia (redondeo a tres cifras):

- `intertwiners.py`: D_4 = 2, D_6 = 5, D_8 = 14, D_10 = 42 para j = 1/2 (números
  de Catalan); D_4 … D_10 = 3, 6, 15, 36, 91, 603 para j = 1 (n = 4, 5, 6, 7, 8, 10).
- `volumen_maximo.py`: n = 4 → k = 0.4136 (tetraedro regular); n = 6 → k = 1.0000
  (cubo); n = 5 → 0.6580 (prisma triangular); n = 7 → 1.3117 (prisma pentagonal);
  n = 8 → 1.6795.

## Advertencias sobre `volumen_maximo.py`

- Es un optimizador local (SLSQP) con puntos de partida aleatorios. La tasa de
  éxito por inicio es baja (típicamente de 1 de cada 10 a 1 de cada 20 para
  n = 4 y 6), por lo que se recomiendan **al menos 25–40 inicios**. Con muy
  pocos inicios puede devolver «sin solución factible».
- Para n ≥ 7 puede tardar varios minutos (usar `semilla` distinta para
  comprobar que los resultados coinciden).
- Los valores son **óptimos locales**; no se demuestra optimalidad global. Para
  n = 4, 5, 6 y 7 coinciden con las formas analíticas esperadas; el valor de
  n = 8 (1.6795) es numérico y coincidió entre dos semillas.
- El programa verifica que el politopo sea acotado (V = ⅓ Σ h_i A_i y
  Σ A_i N_i = 0) y descarta configuraciones inválidas.

## Limitaciones conocidas (resumen)

1. Se usa el volumen **máximo** a áreas fijas y no el volumen medio sobre el
   espacio de formas; esa elección podría cambiar el orden entre valencias.
2. El volumen es clásico; a espín pequeño no es una buena aproximación.
3. Con espines iguales, las valencias impares no existen para j semientero
   (el espacio de intertwiners es vacío).
4. La extensión a formas generales se realizó después de observar el resultado
   con poliedros regulares.
