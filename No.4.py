import pandas as pd
from datetime import datetime
import re


df = pd.read_csv('./DataBase.csv', low_memory=False)

df['OFFENCE_MONTH'] = df['OFFENCE_MONTH'].apply(pd.to_datetime)


phone_related_mask = df['OFFENCE_DESC'].str.contains('phone',re.IGNORECASE)
phone_related_mask.value_counts()

df[phone_related_mask]

phone_related = df[phone_related_mask].groupby('OFFENCE_FINYEAR').size()
print('Num of Phone related datas by year:')
print(phone_related)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
plt.title('Num of Phone related datas by year:')
phone_related.plot()
plt.ylabel('counts')
plt.show()