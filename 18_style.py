import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 6]
# plt.plot(x, y, linewidth=5)
# plt.plot(x, y, marker='o', linestyle='None')
# plt.plot(x, y, marker='v', markersize=10)
# plt.plot(x, y, marker='X', markersize=10)
# plt.plot(x, y, marker='X', markersize=10, markeredgecolor='red', markerfacecolor='yellow')
# plt.plot(x, y, linestyle='--')
# plt.plot(x, y, color='pink')
# plt.plot(x, y, 'ro--')
# plt.plot(x, y, 'bv:')
# plt.plot(x, y, 'go')
# plt.plot(x, y, marker='o', mfc='red', ms=10, mec='blue', ls=':')
# plt.figure(figsize=(5, 10), dpi=150)
plt.figure(facecolor='yellow')
plt.plot(x, y)
plt.show()

