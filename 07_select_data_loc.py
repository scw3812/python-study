import pandas as pd

df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')

# print(df.loc['5번', '국어'])
# print(df.loc[['5번', '2번'], '국어'])
# print(df.loc[['5번', '2번'], ['키', '국어']])
print(df.loc['1번':'5번', '키':'영어'])
