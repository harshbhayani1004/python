from scipy import stats
import numpy as np

marks = [68, 74, 81, 87, 74, 81, 91, 87, 68, 95]
pop_mean = 75
alpha = 0.05

sample_mean = np.mean(marks)
t_stat, p_val = stats.ttest_1samp(marks, pop_mean)

print("Sample Mean:", sample_mean)
print("Hypothesized Mean:", pop_mean)
print("t-statistic:", round(t_stat, 4))
print("p-value:", round(p_val, 4))
print("Significance level (alpha):", alpha)

if p_val < alpha:
    print("Reject Null Hypothesis: Significant difference found")
else:
    print("Fail to Reject Null Hypothesis: No significant difference")
