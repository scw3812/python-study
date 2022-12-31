import pandas as pd

df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')

# print(df['이름'])
# print(df[df.columns[-1]])
# print(df['영어'][:2])
print(df[df.columns[:3]][3:])
