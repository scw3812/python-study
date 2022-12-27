import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

values = [30, 25, 20, 13, 10 ,2]
labels = ['Python', 'Java', 'JavaScript', 'C#', 'C/C++', 'ETC']
# plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
# explode = [0.2, 0.1, 0, 0, 0, 0]
explode = [0.05] * 6
# plt.pie(values, labels=labels, explode=explode)
# plt.legend(loc=(1.2, 0.3), title='언어별 선호도')
colors =  ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff']
wedgeprops = { 'width': 0.5, 'edgecolor': 'w', 'linewidth': 2 }

def custom_autopct(pct):
  # return ('%.1f%%' % pct) if pct >= 10 else ''
  return '{:.0f}%'.format(pct) if pct >= 10 else ''
# plt.pie(
#   values, 
#   labels=labels, 
#   autopct=custom_autopct, 
#   startangle=90, 
#   counterclock=False, 
#   colors=colors,
#   wedgeprops=wedgeprops,
#   pctdistance=0.7
# )
df = pd.read_csv('./score.txt', sep='\t')
grp = df.groupby('학교')
values = [grp.size()['북산고'], grp.size()['능남고']]
labels = ['북산고', '능남고']
plt.pie(values, labels=labels)
plt.title('소속 학교')
plt.show()