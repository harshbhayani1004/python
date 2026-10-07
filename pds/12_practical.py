from scipy import stats

data1 = [74, 81, 87, 91, 95, 68, 85, 78]
data2 = [55, 62, 68, 74, 70, 65, 72, 60]

desc = stats.describe(data1)
print(desc)
print(stats.skew(data1))
print(stats.kurtosis(data1))

t_stat, p_val = stats.ttest_ind(data1, data2)
print(t_stat)
print(p_val)

obs = [16, 18, 16, 14, 12, 12]
chi_stat, chi_p = stats.chisquare(obs)
print(chi_stat)
print(chi_p)

shapiro_stat, shapiro_p = stats.shapiro(data1)
print(shapiro_stat)
print(shapiro_p)
