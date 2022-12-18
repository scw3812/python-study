import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

days = [1, 2, 3]
az = [2, 4, 8]
pfizer = [5, 1 ,3]
moderna = [1, 2, 5]

plt.plot(days, az, label='az')
plt.plot(days, pfizer, label='pfizer', marker='o', linestyle='--')
plt.plot(days, moderna, label='moderna', marker='s', linestyle='-.')
plt.legend(ncol=3)
plt.show()