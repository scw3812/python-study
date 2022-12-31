import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'AppleGothic' # Mac
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

df_m = pd.read_excel('202211_202211_연령별인구현황_월간.xlsx', skiprows=3, index_col='행정기관', usecols='B, E:Y')
df_m.iloc[0] = df_m.iloc[0].str.replace(',', '').astype(int)

df_w = pd.read_excel('202211_202211_연령별인구현황_월간.xlsx', skiprows=3, index_col='행정기관', usecols='B, AB:AV')
df_w.columns = df_m.columns
df_w.iloc[0] = df_w.iloc[0].str.replace(',', '').astype(int)

plt.barh(df_m.columns, -df_m.iloc[0] // 1000)
plt.barh(df_w.columns, df_w.iloc[0] // 1000)
plt.title('2022 대한민국 인구 피라미드')
plt.savefig('2022_인구피라미드.png', dpi=100)

plt.show()