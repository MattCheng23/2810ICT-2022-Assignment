import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

df = pd.read_csv('./DataBase.csv', low_memory=False)
df['OFFENCE_MONTH'] = df['OFFENCE_MONTH'].apply(pd.to_datetime)
# start_time = '2012-3-1'
# end_time = '2013-6-1'
start_time = input('Please enter start time(example: 2012-3-1): ')
end_time = input('Please enter end time(example: 2012-3-1): ')
print(f'The data from {start_time} to {end_time} are:')
start_time = datetime.strptime(start_time,'%Y-%m-%d')
end_time = datetime.strptime(end_time,'%Y-%m-%d')
mask = (df['OFFENCE_MONTH'] > start_time) & (df['OFFENCE_MONTH'] < end_time)
df.drop(["OFFENCE_FINYEAR","OFFENCE_MONTH","OFFENCE_DESC","LEGISLATION","SECTION_CLAUSE","FACE_VALUE","CAMERA_IND", "CAMERA_TYPE", "LOCATION_CODE", "RED_LIGHT_CAMERA_IND", "SPEED_CAMERA_IND", "SEATBELT_IND", "MOBILE_PHONE_IND", "PARKING_IND", "CINS_IND", "FOOD_IND", "BICYCLE_TOY_ETC_IND","LOCATION_DETAILS","SCHOOL_ZONE_IND","SPEED_BAND","SPEED_IND","POINT_TO_POINT_IND","TOTAL_VALUE"],axis = 1, inplace = True)
#print(df)
df.set_index("OFFENCE_CODE", inplace=True)
#df.head
plt.figure(figsize=(10,8))
df.plot()
plt.title('Distribution of cases in each offence code ')
plt.xlabel("OFFENCE CODE")
plt.ylabel('TOTAL NUMBER')
plt.show()