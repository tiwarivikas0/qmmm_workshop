import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("energy.xvg", comments=('#', '@'))

x = data[:,0]
y = data[:,1]

plt.plot(x, y, marker='o')
plt.xlabel("Steps", fontsize=14)
plt.ylabel("Potential Energy", fontsize=14)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()

plt.grid(True)
plt.show()

