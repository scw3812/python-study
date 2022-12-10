import pandas as pd
import numpy as np

df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')

# df['학교'].replace({'북산고':'상북고', '능남고':'무슨고'}, inplace=True)
# df['SW특기'] = df['SW특기'].str.lower()
# df['SW특기'] = df['SW특기'].str.upper()
# df['학교'] = df['학교'] + '등학교'
df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
df['결과'] = 'Fail'
df.loc[df['총합'] > 400, '결과'] = 'Pass'
# df.drop(columns=['키', '학교'], inplace=True)
# df.drop(index=['1번', '4번'], inplace=True)
# filt = df['수학'] < 80
# df.drop(index=df[filt].index, inplace=True)
# df.loc['9번'] = ['이정환', '해남고', 184, 90, 90, 90, 90, 90, 'Kotlin', 450, 'Pass']
# df.loc['4번', 'SW특기'] = 'Python'
# df.loc['5번', ['학교', 'SW특기']] = ['능남고', 'C']
# cols = list(df.columns)
# df = df[[cols[-1]] + cols[:-1]]
df = df[['결과', '학교', '키']]
df.columns = ['Result', 'School', 'Height']
print(df)