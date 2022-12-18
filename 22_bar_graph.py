import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

labels = ['강백호', '서태웅', '정대만']
values = [190, 187, 184]
# plt.bar(labels, values, color='r')
# colors = ['r', 'g', 'b']
# plt.bar(labels, values, color=colors, alpha=0.5)
# plt.bar(labels, values)
# plt.ylim(175, 195)
# plt.bar(labels, values, width=0.5)
# plt.xticks(rotation=45)
# plt.yticks(rotation=45)
# ticks = ['1번', '2번', '3번']
# plt.xticks(labels, ticks)
# plt.barh(labels, values)
# plt.xlim(175, 195)
bar = plt.bar(labels, values)
# bar[0].set_hatch('/')
# bar[1].set_hatch('x')
# bar[2].set_hatch('..')
plt.ylim(175, 195)
for idx, rect in enumerate(bar):
  plt.text(idx, rect.get_height() + 0.5, values[idx], ha='center', color='b')
plt.show()