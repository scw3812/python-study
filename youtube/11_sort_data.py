import pandas as pd
import numpy as np

df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')

# print(df.sort_values('키', ascending=False))
# print(df.sort_values(['수학', '영어'], ascending=[False, True]))
# print(df['키'].sort_values())
print(df.sort_index(ascending=False))