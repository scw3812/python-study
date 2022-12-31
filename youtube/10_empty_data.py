import pandas as pd
import numpy as np

df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')

# print(df.fillna('없음'))
# df['학교'] = np.nan
# df.fillna('모름', inplace=True)
# print(df)
# print(df['SW특기'].fillna('확인 중'))
# print(df.dropna())
# df.dropna(axis='index', how='any', inplace=True)
# df.dropna(axis='columns', how='any', inplace=True)
df['학교'] = np.nan
df.dropna(axis='columns', how='all', inplace=True)
print(df)
