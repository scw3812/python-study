import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 6]

plt.plot(x, y)
plt.savefig('graph.png')
