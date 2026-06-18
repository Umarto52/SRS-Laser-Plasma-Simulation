import numpy as np
import matplotlib.pyplot as plt

# Normalized bandwidth
bandwidth = np.linspace(0.01,10,200)

# Initial growth rate
gamma0 = 1

# Suppression model
gamma_eff = gamma0/(1+bandwidth/gamma0)

plt.figure(figsize=(8,5))
plt.plot(bandwidth,gamma_eff)

plt.xlabel("Laser Bandwidth")
plt.ylabel("Effective SRS Growth Rate")
plt.title("Figure 12: Effective SRS Growth Rate vs Laser Bandwidth")
plt.grid(True)

plt.savefig("Figure12.png",dpi=300)
plt.show()
