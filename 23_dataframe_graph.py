import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./score.txt', sep='\t')
# plt.plot(df['지원번호'], df['키'])
plt.plot(df['지원번호'], df['수학'])
plt.plot(df['지원번호'], df['영어'])

plt.grid(axis='y', color='purple', alpha=0.2, linestyle='--')
plt.show()