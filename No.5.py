import numpy as np
import pandas as pd

data = pd.read_csv("DataBase.csv",low_memory=False)
data.info(verbose=False, memory_usage="deep")
df = data[["SPEED_IND", "POINT_TO_POINT_IND", "RED_LIGHT_CAMERA_IND", "SPEED_CAMERA_IND", "SEATBELT_IND", "MOBILE_PHONE_IND", "PARKING_IND", "CINS_IND", "FOOD_IND", "BICYCLE_TOY_ETC_IND"]]
df.info(verbose=False, memory_usage="deep")

df_2col = pd.read_csv(csv , usecols=["SPEED_IND", "POINT_TO_POINT_IND", "RED_LIGHT_CAMERA_IND", "SPEED_CAMERA_IND", "SEATBELT_IND", "MOBILE_PHONE_IND", "PARKING_IND", "CINS_IND", "FOOD_IND", "BICYCLE_TOY_ETC_IND"])
df_2col.info(verbose=False, memory_usage="deep")