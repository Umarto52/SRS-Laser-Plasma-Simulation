import numpy as np
import matplotlib.pyplot as plt

# Constants
e = 1.602e-19
eps0 = 8.854e-12
me = 9.109e-31

# Laser frequency
omega0 = 2.36e15

# Laser amplitude
a0 = 0.1

# Density range
ne = np.logspace(18,22,100)

# Plasma frequency
omega_pe = np.sqrt(ne*e**2/(eps0*me))

# Simplified growth rate
gamma = a0*np.sqrt(omega0*omega_pe)

plt.figure(figsize=(8,5))
plt.loglog(ne,gamma)

plt.xlabel("Electron Density (m^-3)")
plt.ylabel("SRS Growth Rate")
plt.title("Figure 11: SRS Growth Rate vs Electron Density")
plt.grid(True)

plt.savefig("Figure11.png",dpi=300)
plt.show()
