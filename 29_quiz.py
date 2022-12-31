import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'AppleGothic' # Mac
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)

# 1. 막대 그래프
# plt.bar(df['영화'], df['평점'])

# 2. 세부 사항 적용
# plt.title('국내 Top 8 영화 평점 정보')
# plt.xlabel('영화')
# plt.xticks(rotation=90)
# plt.ylabel('평점')

# 3. 개봉 연도별 평점 변화
# df_group = df.groupby('개봉 연도').mean()
# plt.plot(df_group.index, df_group['평점'])

# 4. 세부 사항 적용
# plt.plot(df_group.index, df_group['평점'], marker='o')
# plt.xticks([2005, 2010, 2015, 2020])
# plt.ylim(7, 10)

# 5. 평점 9점 기준 원 그래프
filt = df['평점'] >= 9.0
values = [len(df[filt]), len(df[~filt])]
labels = ['9점 이상', '9점 미만']

plt.pie(values, labels=labels, autopct='%.1f%%')
plt.legend(loc=(1, 0.3))

plt.show()