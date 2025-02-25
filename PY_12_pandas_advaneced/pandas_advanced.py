import pandas as pd

melb_df = pd.read_csv('data/melb_data_fe.csv')
# print(melb_df.head())
# print(melb_df.info())

melb_df['Date'] = pd.to_datetime(melb_df['Date'])
# print(melb_df['Date'])

def get_quarter(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4


melb_df['quarter'] = melb_df['Date'].dt.month.apply(get_quarter)
# print(melb_df['quarter'].value_counts())

cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
max_unique_count = 150

for col in melb_df.columns:
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude:
        melb_df[col] = melb_df[col].astype('category')

# print(melb_df.info())

# print(melb_df.sort_values(by='Price').head(10))
# print(melb_df.sort_values(by='Date', ascending=False).head(10))
# print(melb_df.sort_values(by=['Distance', 'Price']).loc[::10, ['Distance', 'Price']])
# print(melb_df.sort_values(by=['Price', 'Distance']).loc[::10, ['Price', 'Distance']])

# mask1 = melb_df['AreaRatio'] < -0.8
# mask2 = melb_df['Type'] == 'townhouse'
# mask3 = melb_df['SellerG'] == 'McGrath'
# print(melb_df[mask1 & mask2 & mask3].sort_values(
#     by=['Date', 'AreaRatio'],
#     ascending=[True, False],
#     ignore_index=True
# ).loc[:, ['Date', 'AreaRatio']])

# print(melb_df.sort_values(by='AreaRatio', ascending=False, ignore_index=True).loc[1558])

# mask1 = melb_df['Type'] == 'townhouse'
# mask2 = melb_df['Rooms'] > 2
# print(melb_df[mask1 & mask2].sort_values(
#     by=['Rooms', 'MeanRoomsSquare'],
#     ascending=[True, False],
#     ignore_index=True
# ).loc[18, ['Price']])

# print(melb_df.groupby(by='Type').mean(numeric_only=True))

# print(melb_df.groupby('Type', observed=True)['Price'].mean())

# print(melb_df.groupby('Regionname', observed=True)['Distance'].min().sort_values(ascending=False))

# print(melb_df.groupby('MonthSale', observed=True)['Price'].agg(
#     ['count', 'mean', 'max']
# ).sort_values(by='count',ascending=False))

# print(melb_df.groupby('MonthSale', observed=True)['Price'].agg('describe'))
# print(melb_df.groupby('MonthSale', observed=True)['Price'].describe())

# print(melb_df.groupby('Regionname', observed=True)['SellerG'].agg(['nunique', set]))

# print(melb_df.groupby('Rooms')['Price'].mean().sort_values(ascending=False))

# print(melb_df.groupby('Regionname', observed=True)['Lattitude'].std().sort_values())

# start_date = '2017-05-01'
# end_date = '2017-09-01'
# filtered_df = melb_df[(melb_df['Date'] >= start_date) & (melb_df['Date'] <= end_date)]
# print(filtered_df.groupby('SellerG', observed=True)['Price'].sum().sort_values())

# print(melb_df.groupby(['Rooms', 'Type'], observed=True)['Price'].mean())
# print(melb_df.groupby(['Rooms', 'Type'], observed=True)['Price'].mean().unstack())

# print(melb_df.pivot_table(
#     values='Price',
#     index='Rooms',
#     columns='Type',
#     fill_value=0,
#     observed=True
# ).round())

# print(melb_df.pivot_table(
#     values='Price',
#     index='Regionname',
#     columns='Weekend',
#     aggfunc='count',
#     observed=True
# ))

# print(melb_df.pivot_table(
#     values='Landsize',
#     index='Regionname',
#     columns='Type',
#     aggfunc=['median', 'mean'],
#     fill_value=0,
#     observed=True
# ))

# print(melb_df.pivot_table(
#     values='Price',
#     index=['Method', 'Type'],
#     columns='Regionname',
#     aggfunc='median',
#     fill_value=0,
#     observed=True
# ))

# pivot = melb_df.pivot_table(
#     values='Landsize',
#     index='Regionname',
#     columns='Type',
#     aggfunc=['median', 'mean'],
#     fill_value=0,
#     observed=True
# )

# print(pivot.columns)
# print(pivot['mean']['unit'])

# mask = pivot['mean']['house'] < pivot['median']['house']
# filtered_pivot = pivot[mask]
# print(filtered_pivot)
# print(filtered_pivot.index)

#4.2
# pivot = melb_df.pivot_table(
#     values='BuildingArea',
#     index='Rooms',
#     columns='Type',
#     aggfunc='median',
#     fill_value=0,
#     observed=True
# )
#
# print(pivot)

#4.3
pivot = melb_df.pivot_table(
    values='Price',
    index='SellerG',
    columns='Type',
    aggfunc='median',
    fill_value=0,
    observed=True
)

print(pivot.sort_values(by='unit', ascending=False))