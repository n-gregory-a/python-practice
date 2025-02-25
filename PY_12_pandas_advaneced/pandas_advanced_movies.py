from itertools import product

import pandas as pd
# import re

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# dates_df = pd.read_csv('movies_data/dates.csv')
# movies_df = pd.read_csv('movies_data/movies.csv')
# ratings1_df = pd.read_csv('movies_data/ratings1.csv')
# ratings2_df = pd.read_csv('movies_data/ratings2.csv')


# print(movies_df.nunique())
# print(ratings1_df.nunique())
# dates_df['years'] = pd.to_datetime(dates_df['date']).dt.year
# print(dates_df.head())
# print(dates_df['years'].value_counts())

# ratings_df = pd.concat([ratings1_df, ratings2_df], ignore_index=True)
# print(ratings1_df.tail(1))
# print(ratings2_df.head(1))
# print('Число строк в таблице ratings: ', ratings_df.shape[0])
# print('Число строк в таблице dates: ', dates_df.shape[0])
# ratings_df = ratings_df.drop_duplicates(ignore_index=True)
# print('Число строк в таблице ratings: ', ratings_df.shape[0])

# ratings_dates = pd.concat([ratings_df, dates_df], axis=1)
# print(ratings_dates.tail(7))

# joined = ratings_dates.join(
#     movies_df.set_index('movieId'),
#     on='movieId',
#     how='left'
# )
# print(joined)
#
# merged = ratings_dates.merge(
#     movies_df,
#     on='movieId',
#     how='left'
# )
# print(merged)

#

# rating_movies_df = pd.read_csv('movies_data/ratings_movies.csv')

# print(rating_movies_df.head())

# def get_year_release(arg):
#     # находим все слова по шаблону "(DDDD)"
#     candidates = re.findall(r'\(\d{4}\)', arg)
#     # проверяем число вхождений
#     if len(candidates) > 0:
#         # если число вхождений больше 0,
# 	# очищаем строку от знаков "(" и ")"
#         year = candidates[0].replace('(', '')
#         year = year.replace(')', '')
#         return int(year)
#     else:
#         # если год не указан, возвращаем None
#         return None
#
# rating_movies_df['year_release'] = rating_movies_df['title'].apply(get_year_release)
# print(rating_movies_df.describe())

# sorted_by_year = rating_movies_df[rating_movies_df['year_release'] == 2010]
# sorted_by_year = rating_movies_df.sort_values(by=['year_release', 'rating'])
# print(rating_movies_df[rating_movies_df['year_release'] == 2010].groupby('genres')['rating'].mean().sort_values())
# print(rating_movies_df.groupby('userId').nunique().sort_values(by='genres', ascending=False))
# print(rating_movies_df.groupby('userId')['rating'].agg(['count', 'mean']).sort_values(by=['count', 'mean']).head(30))
# count_mean_df = rating_movies_df[rating_movies_df['year_release'] == 2018].groupby('genres')['rating'].agg(['mean','count'])
# filtered = count_mean_df[count_mean_df['count'] > 10]
# print(filtered)
#
# rating_movies_df['year_rating'] = pd.to_datetime(rating_movies_df['date']).dt.year
# pivot_table = rating_movies_df.pivot_table(values='rating', index='year_rating', columns='genres', aggfunc='mean',
#                                      observed=True)
# print(pivot_table.info())

orders_df = pd.read_csv('data/orders.csv', sep=';')
products_df = pd.read_csv('data/products.csv', sep=';')

# print(orders_df.info())
# print('--------------')
# print(products_df.info())

orders_products = orders_df.merge(
    products_df,
    left_on='ID товара',
    right_on='Product_ID',
    how='left'
)


orders_products['total'] = orders_products['Price'] * orders_products['Количество']
# print(orders_products)
complete_only = orders_products[orders_products['Отменен'] == 'Нет']
print(complete_only)
print(complete_only.groupby('ID Покупателя')['total'].agg('sum'))