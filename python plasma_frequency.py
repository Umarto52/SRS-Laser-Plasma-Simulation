import numpy as np
import matplotlib.pyplot as plt

# Constants
e = 1.602e-19
eps0 = 8.854e-12
me = 9.109e-31

# Electron density range
ne = np.logspace(18, 22, 100)

# Plasma frequency
omega_pe = np.sqrt(ne * e**2 / (eps0 * me))

plt.figure(figsize=(8,5))
plt.loglog(ne, omega_pe)

plt.xlabel("Electron Density (m^-3)")
plt.ylabel("Plasma Frequency (rad/s)")
plt.title("Figure 10: Plasma Frequency vs Electron Density")
plt.grid(True)

plt.savefig("Figure10.png", dpi=300)
plt.show()
