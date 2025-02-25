import pandas as pd

countries = pd.Series(
    data= ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    index=['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ'],
    name='countries'
)

#
# print(countries)
#
# countries_from_dict = pd.Series({
#     'UK': 'Англия',
#     'US': 'США'
# },
#     name='countries_from_dict'
# )
#
# print(countries_from_dict)
#
# print(countries.loc[['UK', 'RU', 'KZ']])
#
# print(countries.iloc[5])
# print(countries.iloc[2:5])


# def create_medications(names_ls, counts_ls):
#     return pd.Series(
#         data=counts_ls,
#         index=names_ls
#     )
#
# def get_percent(medications, name):
#     quantity = medications.loc[name]
#     quantities = medications.tolist()
#     quantities_sum = sum(quantities)
#     return quantity * 100 / quantities_sum
#
# names=['chlorhexidine', 'cyntomycin', 'afobazol']
# counts=[15, 18, 7]
# medications = create_medications(names, counts)
#
# print(get_percent(medications, "chlorhexidine")) #37.5


countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'area': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})

countries_df.index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']

countries_df.to_csv('data/countries.csv', index=False, sep=';')
countries_data = pd.read_csv('data/countries.csv', sep=';')
# print(countries_data)


# print(countries_df)

countries_df_2 = pd.DataFrame(
    data=[
['Англия', 56.29, 133396],
        ['Канада', 38.05, 9984670],
        ['США', 322.28, 9826630],
        ['Россия', 146.24, 17125191],
        ['Украина', 45.5, 603628],
        ['Беларусь', 9.5, 207600],
        ['Казахстан', 17.04, 2724902]
    ],
    columns=['country', 'population', 'area'],
    index=['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']
)
# print(countries_df_2)

# print(countries_df.mean(axis=0, numeric_only=True))
# print(countries_df.mean(axis=1, numeric_only=True))
# print(countries_df.population)
# print(countries_df['population'])
# print(type(countries_df.population))
#
# print(countries_df.loc['UK', 'population'])
# print(countries_df.loc['RU', ['population', 'area']])
# print(countries_df.loc[['UA', 'BY', 'KZ'],['population', 'area']])
# print(countries_df.iloc[4:8, 1:3])

def create_company_df(income, expenses, years) -> pd.DataFrame:
    data_for_frame = []
    for i in range(len(income)):
        data_for_frame.append([income[i], expenses[i]])
    return pd.DataFrame(
        data=data_for_frame,
        columns=['Income', 'Expenses'],
        index=years
    )

def get_profit(df, year):
    try:
        data = df.loc[year, ['Income', 'Expenses']]
    except KeyError:
        return None

    return data[0] - data[1]

income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]

# print(create_company_df(income, expenses, years))
# print(get_profit(create_company_df(income, expenses, years), 2013))

# melb_data = pd.read_csv('data/melb_data.csv', sep=',')
# print(melb_data)
# print(melb_data.loc[3521])
# print(melb_data.head())
# print(melb_data.tail(7))
# print(melb_data.shape)

# melb_data['Car'] = melb_data['Car'].astype('int64')
# melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
# melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
# melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
# melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
# print(melb_data.info())

# print(melb_data.describe().loc[:, ['Price', 'Distance', 'BuildingArea']])
# print(melb_data.describe(include=['object']))
# print(melb_data['Type'].value_counts(normalize=True))
# print(melb_data['Price'].mean())
# landsize_median = melb_data["BuildingArea"].median()
# landsize_mean = melb_data["BuildingArea"].mean()
# print(melb_data["BuildingArea"].median())
# print(melb_data["BuildingArea"].mean())
# print(abs(landsize_median - landsize_mean)/landsize_mean)


# mask = melb_data['Price'] < 2000000
# print(melb_data[melb_data['Price'] < 2000000].tail(10))

# print(melb_data[((melb_data['Rooms'] == 3) | (melb_data['BuildingArea'] > 100)) & (melb_data['Price'] < 300000)].shape[0])
# print(melb_data[(melb_data['Price'] < 1000000) & ((melb_data['Rooms'] > 5) | (melb_data['YearBuilt'] > 2015))]['Price'].mean())
# print(melb_data[(melb_data['Type'] == 'h') & (melb_data['Price'] < 3000000)]['Regionname'].value_counts())


student_performance = pd.read_csv('data/students_performance.csv')

# print(student_performance.loc[155]['writing score'])
print(student_performance.info())
# print(student_performance['lunch'].tail())
# print(student_performance.describe())
print()
print('--------------------------------')
print()
# print(student_performance['race/ethnicity'].mode())
# print(student_performance[student_performance['test preparation course'] == 'completed']['reading score'].mean())
# print(student_performance[student_performance['math score'] == 0].shape[0])
# print(student_performance[student_performance['lunch'] == 'standard']['math score'].mean())
# print(student_performance[student_performance['lunch'] == 'free/reduced']['math score'].mean())
# print(student_performance['parental level of education'].value_counts(normalize=True)['bachelor\'s degree'])
median_a = student_performance[student_performance['race/ethnicity'] == 'group A']['writing score'].median()
print(median_a)
mean_c = student_performance[student_performance['race/ethnicity'] == 'group C']['writing score'].mean()
print(mean_c)
print(abs(median_a - mean_c))