import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./score.txt', sep='\t')
plt.figure(figsize=(10, 5))
plt.title('학생별 성적')
index = np.arange(df.shape[0])
w = 0.25
plt.bar(index - w, df['국어'], width=w, label='국어')
plt.bar(index, df['영어'], width=w, label='영어')
plt.bar(index + w, df['수학'], width=w, label='수학')
plt.legend(ncol=3)
plt.xticks(index, df['이름'], rotation=60)
plt.show()