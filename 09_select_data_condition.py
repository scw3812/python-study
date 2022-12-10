import pandas as pd

df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')

# print(df['키'] >= 185)
# filt = df['키'] >= 185
# print(df[filt], df[~filt], sep='\n')
# print(df.loc[df['키'] >= 185, ['수학', '과학']])
# print(df.loc[(df['키'] >= 185) & (df['학교'] == '북산고'), ['수학', '과학']])
# print(df.loc[(df['키'] >= 200) | (df['키'] < 170)])
# print(df.loc[df['이름'].str.startswith('송')])
# print(df.loc[~df['이름'].str.contains('강')])
# langs = ['Python', 'Java']
# print(df.loc[df['SW특기'].isin(langs)])
# langs = ['python', 'java']
# print(df.loc[df['SW특기'].str.lower().isin(langs)])
print(df.loc[df['SW특기'].str.contains('Java', na=False)])
