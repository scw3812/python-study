import pandas as pd

df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')

def add_cm(height):
  return str(height) + 'cm'

df['키'] = df['키'].apply(add_cm)
print(df)

def capitalize(lang):
    if pd.notnull(lang):
      return lang.capitalize()
    return lang

df['SW특기'] = df['SW특기'].apply(capitalize)
print(df)