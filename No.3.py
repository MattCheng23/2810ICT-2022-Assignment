import pandas as pd
from datetime import datetime
import re


df = pd.read_csv('./DataBase.csv', low_memory=False)

df['OFFENCE_MONTH'] = df['OFFENCE_MONTH'].apply(pd.to_datetime)


# start_time = '2012-3-1'
# end_time = '2013-6-1'
start_time = input('Please enter start time(example: 2012-3-1): ')
end_time = input('Please enter end time(example: 2013-6-1): ')

print(f'The data from {start_time} to {end_time} are:')
start_time = datetime.strptime(start_time,'%Y-%m-%d')
end_time = datetime.strptime(end_time,'%Y-%m-%d')
mask = (df['OFFENCE_MONTH'] > start_time) & (df['OFFENCE_MONTH'] < end_time) &(df['OFFENCE_DESC'].str.contains('Camera',re.IGNORECASE))
# print(mask.value_counts())
print(df[mask])
df[mask].reset_index(drop=True).to_csv(f'{start_time}_to_{end_time}.csv')