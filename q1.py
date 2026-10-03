import numpy as np

y = np.array([0, 2, 4, 6, 8, 10, 12, 14], dtype=float)

H = np.array([0, 1, 1.5, 3, 3.5, 3.2, 2, 0], dtype=float)

U = np.array([0, 0.1, 0.12, 0.2, 0.25, 0.3, 0.15, 0], dtype=float)

h = y[1] - y[0]

HU = H * U

A_trap = (h / 2) * (H[0] + H[-1] + 2 * np.sum(H[1:-1]))

Q_trap = (h / 2) * (HU[0] + HU[-1] + 2 * np.sum(HU[1:-1]))


Uavg_trap = Q_trap / A_trap


print("PART (a) - TRAPEZOIDAL RULE")
print("--------------------------------")
print("Area =", A_trap, "m^2")
print("Discharge =", Q_trap, "m^3/s")
print("Average velocity =", Uavg_trap, "m/s")


A_13 = (h / 3) * (H[0] + H[4]+ 4 * (H[1] + H[3])+ 2 * H[2])

A_38 = (3 * h / 8) * (H[4] + H[7]+ 3 * (H[5] + H[6]))

A_simp = A_13 + A_38

Q_13 = (h / 3) * (HU[0] + HU[4]+ 4 * (HU[1] + HU[3])+ 2 * HU[2])

Q_38 = (3 * h / 8) * (HU[4] + HU[7]+ 3 * (HU[5] + HU[6]))

Q_simp = Q_13 + Q_38

Uavg_simp = Q_simp / A_simp


print("\nPART (b) - SIMPSON'S RULE")
print("--------------------------------")
print("Area =", A_simp, "m^2")
print("Discharge =", Q_simp, "m^3/s")
print("Average velocity =", Uavg_simp, "m/s")