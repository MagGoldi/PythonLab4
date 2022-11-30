import pandas as pd
import numpy as np

def main() -> None:

    df = pd.read_csv("C:\PYTHON\PythonLab4\dataset.csv") #1

    df.columns =['data', 'temp_day', 'wind', 'pressure_day', 'temp_even', 'pressure_even'] #2
    

    nan_value = float("NaN")                        #3  ( null / None / Nan ) ////
    df.replace(" ", nan_value, inplace=True)
    df = df.dropna()
    print(df)


    df[['temp_day', "temp_even"]] =  df[['temp_day', "temp_even"]].astype(int)        #4
    print(df)
    print(df.dtypes)
    df = df.assign(temp_f_day = (df.temp_day *9/5) +32, temp_f_even = (df.temp_even*9/5) +32)
    print(df)


    stats = df[['temp_day', "temp_even", "temp_f_day", "temp_f_even"]].describe()     #5
    print(stats)



if __name__ == '__main__':
    main()   