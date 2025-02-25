import pandas as pd

city_bike = pd.read_csv('data/citibike-tripdata.csv')
# print(city_bike.head())
# print(city_bike.describe())
# print(city_bike.info())
# print(city_bike['usertype'].value_counts())
# subs = city_bike['usertype'].value_counts()['Subscriber']
# print(subs)
# subscriber_rate = subs / 300000
# print(subscriber_rate)

# print(city_bike['gender'].value_counts())
# print(city_bike['start station id'].nunique())
# print(city_bike['end station id'].nunique())
# print(city_bike['birth year'].min())
# print(city_bike['birth year'].max())
# print(city_bike['start station name'].value_counts())
# print(city_bike['end station name'].value_counts())
city_bike.drop(['start station id', 'end station id'], axis=1, inplace=True)
# print(city_bike.info())
# print(city_bike['birth year'])
city_bike['age'] = 2018 - city_bike['birth year']
city_bike.drop(['birth year'], axis=1, inplace=True)
# print(city_bike['age'])
age_counts = city_bike['age'].value_counts()
# print(age_counts)
# print(city_bike[city_bike['age'] > 60].shape[0])
city_bike['trip duration'] = pd.to_datetime(city_bike['stoptime']) - pd.to_datetime(city_bike['starttime'])
# print(city_bike['trip duration'])

def define_weekend(date):
    if pd.to_datetime(date).dayofweek < 5:
        return 0
    return 1

# city_bike['weekend'] = city_bike['starttime'].apply(define_weekend)
# print(city_bike['weekend'].value_counts())

def time_of_day_def(date):
    hour = pd.to_datetime(date).hour
    if 0 <= hour <= 6:
        return 'night'
    if 6 < hour <= 12:
        return 'morning'
    if 12 < hour <= 18:
        return 'day'
    if 18 < hour <= 23:
        return 'evening'

city_bike['time_of_day'] = city_bike['starttime'].apply(time_of_day_def)
print(city_bike['time_of_day'].value_counts())