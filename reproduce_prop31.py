"""
Reproducibilidad Prop 3.1 - vH3.1
5-cell maximiza densidad de entropía holográfica entre los 6 politopos regulares convexos en 4D a R=1
Fuente V4 y V∂: Coxeter Regular Polytopes 3rd ed. Table I + cálculo directo en el paper
Autor: Miguel Ángel Franco León + verificación colaborativa
"""
import math

data = {
    "5-cell {3,3,3}":   {"n":5,   "V4":0.146, "Vd":1.193,  "a":1.2649},
    "16-cell {3,3,4}":  {"n":8,   "V4":0.667, "Vd":5.333,  "a":1.4142},
    "8-cell {4,3,3}":   {"n":16,  "V4":1.000, "Vd":12.317, "a":1.1547},
    "24-cell {3,4,3}":  {"n":24,  "V4":2.000, "Vd":11.314, "a":1.0000},
    "600-cell {3,3,5}": {"n":120, "V4":3.863, "Vd":47.214, "a":0.8740},
    "120-cell {5,3,3}": {"n":600, "V4":4.193, "Vd":334.22, "a":0.7136},
}

print(f"{'Politopo':<18} {'ln n/V∂':>9} {'ln n/V4':>9} {'margen V∂':>11}")
lnVd_vals = []
for name,d in data.items():
    ln = math.log(d["n"])
    rVd = ln/d["Vd"]
    rV4 = ln/d["V4"]
    lnVd_vals.append(rVd)
    print(f"{name:<18} {rVd:9.4f} {rV4:9.4f}")

# ranking
sorted_Vd = sorted(data.items(), key=lambda kv: math.log(kv[1]["n"])/kv[1]["Vd"], reverse=True)
max_Vd = math.log(sorted_Vd[0][1]["n"])/sorted_Vd[0][1]["Vd"]
second_Vd = math.log(sorted_Vd[1][1]["n"])/sorted_Vd[1][1]["Vd"]
print(f"\nProp 3.1: 5-cell gana por {max_Vd/second_Vd:.2f}x sobre {sorted_Vd[1][0]} en ρ=ln n / V∂")
print(f"Robustez: también gana por {math.log(5)/0.146 / (math.log(8)/0.667):.2f}x en ρ_V=ln n / V4")

# Omega_DM
Omega_DM = 2*math.log(1.5)/3
Omega_m = Omega_DM + 0.049  # usando Omega_b ~0.049-0.0516 candidato
print(f"\nOmega_DM = 2 ln(3/2)/3 = {Omega_DM:.6f}")
print(f"Omega_m ≈ {Omega_m:.4f} (con Omega_b candidato 0.049)")

# chequeo identidad
z_pack, z_fund = 12, 4
Nbits = 3
print(f"\nIdentidad d=3: z_pack - z = {z_pack - z_fund} = 2^Nbits = {2**Nbits} -> {'OK' if z_pack - z_fund == 2**Nbits else 'FAIL'}")
