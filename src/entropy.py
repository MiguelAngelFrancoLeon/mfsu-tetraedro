import numpy as np
 
# Analytic bound: s(z) strictly decreasing for z >= 4
z_star = np.e**(1.5) / 2
print(f"z* = e^(3/2)/2 = {z_star:.4f} < 4")
print("=> s(z) strictly decreasing for z in {4,6,8,12,20}")
print()
 
# Numerical verification (normalization-independent)
z_vals = [4, 6, 8, 12, 20]
s = {z: np.log(2*z) / z**(2/3) for z in z_vals}  # C cancels
winner = max(s, key=s.get)
assert winner == 4, "Entropic selection failed"
print(f"argmax s(z) = {winner}  VERIFIED")
print(f"Margin s(4)/s(6) = {s[4]/s[6]:.6f}")
 
# Normalization independence: same margin for any C
for z0 in [4, 6, 8, 12]:
    C = 2 * (1/z0)**(2/3)
    s_norm = {z: np.log(2*z)/(2*C*z**(2/3)) for z in z_vals}
    ratio = s_norm[4]/s_norm[6]
    assert abs(ratio - s[4]/s[6]) < 1e-12
print(f"Normalization independence: VERIFIED (ratio invariant)")
