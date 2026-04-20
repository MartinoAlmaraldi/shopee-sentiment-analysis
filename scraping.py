from google_play_scraper import reviews, Sort
import pandas as pd

result, _ = reviews(
    'com.shopee.id',
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=10000
)

df = pd.DataFrame(result)
df = df[['content']]
df.columns = ['review']
df = df.dropna(subset=['review'])
df = df.reset_index(drop=True)
df.to_csv('dataset.csv', index=False)