import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./score.txt', sep='\t')
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('여러 그래프 넣기')

axs[0, 0].bar(df['이름'], df['국어'], label='국어점수')
axs[0, 0].set_title('첫 번째 그래프')
axs[0, 0].legend()
axs[0, 0].set(xlabel='이름', ylabel='점수')
axs[0, 0].set_facecolor('lightyellow')
axs[0, 0].grid(linestyle='--', linewidth=0.5)

axs[0, 1].plot(df['이름'], df['수학'], label='수학점수')
axs[0, 1].plot(df['이름'], df['영어'], label='영어점수')
axs[0, 1].legend()

axs[1, 0].barh(df['이름'], df['키'])

axs[1, 1].plot(df['이름'], df['사회'], color='green', alpha=0.5)

plt.show()