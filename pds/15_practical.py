import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n = 10
p = 0.5
k_binom = np.arange(0, 11)
pmf_binom = stats.binom.pmf(k_binom, n, p)

print("Binomial Probabilities:")
for k, val in zip(k_binom, pmf_binom):
    print(k, ":", round(val, 4))

mu = 4
k_poisson = np.arange(0, 15)
pmf_poisson = stats.poisson.pmf(k_poisson, mu)

print("\nPoisson Probabilities:")
for k, val in zip(k_poisson, pmf_poisson):
    print(k, ":", round(val, 4))

plt.subplot(1, 2, 1)
plt.bar(k_binom, pmf_binom, color="skyblue", edgecolor="black")
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("k")
plt.ylabel("Probability")

plt.subplot(1, 2, 2)
plt.bar(k_poisson, pmf_poisson, color="lightgreen", edgecolor="black")
plt.title("Poisson Distribution (mu=4)")
plt.xlabel("k")
plt.ylabel("Probability")

plt.tight_layout()
plt.savefig("15_distribution.png")
plt.show()
