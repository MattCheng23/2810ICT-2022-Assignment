import pandas as pd
import re
df = pd.read_csv("DataBase.csv",low_memory=False)
#print(df)
df.set_index('OFFENCE_MONTH', inplace=True)
df.index
x = input("Enter a date")
df.loc[[x], ['OFFENCE_CODE', 'OFFENCE_DESC', 'LEGISLATION', 'SECTION_CLAUSE', 'FACE_VALUE', 'CAMERA_IND', 'CAMERA_TYPE', 'LOCATION_CODE', 'RED_LIGHT_CAMERA_IND', 'SPEED_CAMERA_IND', 'SEATBELT_IND', 'MOBILE_PHONE_IND', 'PARKING_IND', 'CINS_IND', 'FOOD_IND', 'BICYCLE_TOY_ETC_IND', 'TOTAL_NUMBER', 'TOTAL_VALUE']]
print(df.loc)

