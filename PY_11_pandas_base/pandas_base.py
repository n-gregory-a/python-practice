import pandas as pd

melb_data = pd.read_csv("data/melb_data_ps.csv")
# print(melb_data.head())

melb_df: pd.DataFrame = melb_data.copy()

# print(type(melb_df))

# melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)
melb_df.drop(['index', 'Coordinates'], axis=1, inplace=True)
# print(melb_df.head())

total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
# print(total_rooms)

melb_df['MeanRoomsArea'] = melb_df['BuildingArea']/total_rooms
# print(melb_df['MeanRoomsArea'])

diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area
# print(melb_df['AreaRatio'])

melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
# print(melb_df['Date'])
years_sold = melb_df['Date'].dt.year
# print(years_sold)

melb_df['MonthSale'] = melb_df['Date'].dt.month
# print(melb_df['MonthSale'].value_counts(normalize=True))

delta_days = melb_df['Date'] - pd.to_datetime('2016-01-01')
# print(delta_days)
# print(delta_days.dt.days)

melb_df['AgeBuilding'] = melb_df['Date'].dt.year - melb_df['YearBuilt']
# print(melb_df['AgeBuilding'])

melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
# print(melb_df['WeekdaySale'])

weekend_count = melb_df[melb_df['WeekdaySale'] >= 5].shape[0]
# print(weekend_count)

# print(melb_df['Address'].nunique())

def get_street_type(address):
    exclude_list = ['N', 'S', 'E', 'W']
    address_list = address.split(' ')
    street_type = address_list[-1]

    if street_type in exclude_list:
        street_type = address_list[-2]

    return street_type

street_types = melb_df['Address'].apply(get_street_type)
change_dict = {'Avenue': 'Av', 'Boulevard': 'Bvd', 'Parade': 'Pde'}
street_types = street_types.apply(lambda x: x if change_dict.get(x) is None else change_dict.get(x))
# print(street_types)
# print(street_types.nunique())
# print(street_types.value_counts())

popular_stypes = street_types.value_counts().nlargest(10).index
# print(popular_stypes)


melb_df['StreetType'] = street_types.apply(lambda x: x if x in popular_stypes else 'other')
# print(melb_df['StreetType'])
# print(melb_df['StreetType'].nunique())

def get_weekend(weekday):
    return 0 if weekday < 5 else 1

melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
# print(melb_df['Weekend'])
# print(melb_df[melb_df['Weekend'] == 1]['Price'].mean())

biggest_agencies = melb_df['SellerG'].value_counts().nlargest(49)
# print(biggest_agencies)
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda name: name if name in biggest_agencies else 'other')
# print(melb_df['SellerG'])

min_price_nelson = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min()
min_price_other = melb_df[melb_df['SellerG'] == 'other']['Price'].min()
# print(min_price_nelson)
# print(min_price_other)
# print(min_price_nelson / min_price_other)

unique_list = []

for col in melb_df.columns:
    item = (col, melb_df[col].nunique(), melb_df[col].dtypes)
    unique_list.append(item)

unique_counts = pd.DataFrame(
    unique_list,
    columns=['Column_Name', 'Num_Unique', 'Type']
).sort_values(by='Num_Unique', ignore_index=True)
# print(unique_counts)

# print(melb_df.info())

cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
max_unique_count = 150

for col in melb_df.columns:
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude:
        melb_df[col] = melb_df[col].astype('category')


# print(melb_df['Regionname'].cat.categories)
# print(melb_df['Regionname'].cat.codes)

melb_df['Type'] = melb_df['Type'].cat.rename_categories({
    'u': 'unit',
    't': 'townhouse',
    'h': 'house'
})
# print(melb_df['Type'])

print(melb_df.info())
# print(melb_df['Suburb'].value_counts().nlargest(119))
largest_suburb = melb_df['Suburb'].value_counts().nlargest(119)
melb_df['Suburb'] = melb_df['Suburb'].apply(lambda name: name if name in largest_suburb else 'other')
melb_df['Suburb'] = melb_df['Suburb'].astype('category')
# print(melb_df['Suburb'])
print(melb_df.info())



# countries_df = pd.DataFrame({
#     'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
#     'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
#     'area': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
# })
#
# print(countries_df)
#
# countries_df['pop_ratio'] = (countries_df['population'] * 1000000) / countries_df['area']
#
# print(countries_df)
#
# print(countries_df['pop_ratio'].mean())



# ufo_df = pd.read_csv('data/ufo.csv')
# print(ufo_df.head())
#
# ufo_df['Time'] = pd.to_datetime(ufo_df['Time'])
# # print(ufo_df['Time'])
# years = ufo_df['Time'].dt.year
# # print(years.value_counts())
#
# date =  ufo_df[ufo_df['State'] == 'NV']['Time'].dt.date
# print(date)
#
# date_diff = date.diff().dt.days.mean()
# print(date_diff)



# str1 = 'Опыт работы 8 лет 3 месяца'
# str2 = 'Опыт работы 3 месяца'
# str3 = 'Опыт работы 6 лет'
# def get_experience(arg):
#     splitted = arg.split()
#     splitted = splitted[2:]
#
#     if len(splitted) == 4:
#         return int(splitted[0])*12 + int(splitted[2])
#
#     if splitted[1] == 'лет' or splitted[0] == 'года':
#         return int(splitted[0]) * 12
#
#     if splitted[1] == 'месяца' or splitted[1] == 'месяцев':
#         return int(splitted[0])
#
# print(get_experience(str1))
# print(get_experience(str2))
# print(get_experience(str3))