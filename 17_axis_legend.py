import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y, label='무슨 데이터')
# plt.legend(loc='center')
plt.legend(loc=(0.3, 0.8))
plt.title('꺾은 선 그래프')
plt.xlabel('X축', color='red', loc='right')
plt.ylabel('Y축', color='#00AA00', loc='top')
plt.xticks([1, 2, 3])
plt.yticks([3, 6, 9, 12])
plt.show()

