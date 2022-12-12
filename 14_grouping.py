import pandas as pd

df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')

# print(df.groupby('학교').get_group('북산고'))
# print(df.groupby('학교').mean())
# print(df.groupby('학교').size())
# print(df.groupby('학교').size()['능남고'])
# print(df.groupby('학교')['키'].mean())
# print(df.groupby('학교')[['국어', '영어', '수학']].mean())
df['학년'] = [3, 3, 2, 1, 1, 3, 2, 2]
# print(df.groupby(['학교', '학년']).mean())
# print(df.groupby('학년').mean().sort_values('키'))
# print(df.groupby(['학교', '학년']).sum())
# print(df.groupby('학교')[['이름', 'SW특기']].count())
school = df.groupby('학교')
# print(school['학년'].value_counts().loc['북산고'])
print(school['학년'].value_counts(normalize=True).loc['북산고'])