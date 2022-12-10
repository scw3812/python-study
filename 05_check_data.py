import pandas as pd

df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')

# print(df.describe())
# df.info()
# print(df.head(4))
# print(df.tail(4))
# print(df.values, df.index, df.columns, df.shape, sep='\n')

# print(df['키'].describe())
print(df['키'].min(), df['키'].count(), df['학교'].nunique(), '\n', df['키'].nlargest(3), '\n', df['학교'].unique())
