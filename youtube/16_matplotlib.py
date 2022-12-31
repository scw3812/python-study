import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# print([f.name for f in fm.fontManager.ttflist])
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

# x = [1, 2, 3]
# y = [2, 4, 6]
# plt.plot(x, y)
# plt.title('Line Graph')
# plt.title('꺾은 선 그래프')
plt.plot([-1, 0, 1], [-2, 0, 2])
plt.show()

