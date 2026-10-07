import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x_norm = np.linspace(-4, 4, 100)
y_norm = stats.norm.pdf(x_norm, 0, 1)

x_exp = np.linspace(0, 5, 100)
y_exp = stats.expon.pdf(x_exp, scale=1)

sample_means = []
for i in range(1000):
    sample = np.random.uniform(0, 10, 30)
    sample_means.append(np.mean(sample))

print("Mean of sample means:", round(np.mean(sample_means), 4))
print("Std of sample means:", round(np.std(sample_means), 4))

plt.subplot(1, 3, 1)
plt.plot(x_norm, y_norm, color="blue")
plt.title("Normal Distribution")
plt.xlabel("x")
plt.ylabel("Density")

plt.subplot(1, 3, 2)
plt.plot(x_exp, y_exp, color="red")
plt.title("Exponential Distribution")
plt.xlabel("x")
plt.ylabel("Density")

plt.subplot(1, 3, 3)
plt.hist(sample_means, bins=30, color="green", edgecolor="black", density=True)
plt.title("Central Limit Theorem")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("16_clt.png")
plt.show()
