import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-12/Downloads/auto-mpg (2).csv")
print(data)
#statistical details of dataset
stats=data.describe()
print(stats)
#get all cars with 8cylinders
print(data['cylinders']==8)
#get the number of car manufactured in  each year
print(data['model-year'].sum())
