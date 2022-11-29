import pandas as pd
import numpy as np


df = pd.read_csv("C:\PYTHON\PythonLab4\dataset_test.csv") #1

df.columns =['data', 'temp_day', 'wind', 'pressure_day', 'temp_evening', 'pressure_evening'] #2

df_without_nan = df.dropna()  #3  ( null / None / Nan ) ////
df = df.dropna() 
print(df_without_nan)

df1 = df["pressure_evening"].astype("float64")

print('------------------------------')
print('\nNew Datatypes\n', df.dtypes, sep='') 
df1 = df.astype("int64", errors='ignore')
df1.head()
df1.info()