import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./score.txt', sep='\t')
df['학년'] = [3, 3, 2, 1, 1, 3, 2, 2]
# plt.scatter(df['영어'], df['수학'])
# plt.xlabel('영어 점수')
# plt.ylabel('수학 점수')
sizes = np.random.rand(8) * 1000
# plt.scatter(df['영어'], df['수학'], s=sizes)
plt.figure(figsize=(7, 7))
plt.scatter(df['영어'], df['수학'], s=df['학년'] * 500, c=df['학년'], cmap='viridis', alpha=0.5)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.colorbar(ticks=[1, 2, 3], label='학년', shrink=0.5, orientation='horizontal')
plt.show()