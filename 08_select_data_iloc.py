import pandas as pd

df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')

# print(df.iloc[0])
# print(df.iloc[:5])
# print(df.iloc[0, 1])
# print(df.iloc[[0, 1], 2])
# print(df.iloc[[0, 1], [2, 4]])
print(df.iloc[:5, 3:8])
