import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def task6(df: pd.DataFrame, value: float) -> pd.DataFrame:
    return df.loc[df['temp_day'] >= value]

def task7(df: pd.DataFrame, value1: float, value2: float) -> pd.DataFrame:
    df =  df.loc[df['temp_day'] >= value1]
    df =  df.loc[df['temp_day'] <= value2]
    return df

def custom(df: pd.DataFrame, month: int, year: int) -> pd.DataFrame:
    df['data'] =  df['data'].apply(str) 
    print(df.dtypes)
    #df_custom = df.loc[(df['temp_day'] >= 20)]
    data1 = str(str(year)+"-"+str(month) +"-"+"01")
    data2 = str(str(year)+"-"+str(month) +"-"+"31")
    df_custom = df.loc[(df['data'] >= data1) & (df['data'] <= data2)]
    df_custom = df.loc[(df['data'] <= data2)]
    print(df_custom)             
    print(df_custom.info())
    print(df_custom)  
    print(df_custom)  

def main() -> None:

    df = pd.read_csv("C:\PYTHON\PythonLab4\dataset.csv") #1

    df.columns = ['data', 'temp_day', 'wind', 'pressure_day', 'temp_even', 'pressure_even'] #2
    

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

    value = 20                             #6
    df_t6 = task6(df, value)
    print(df_t6)

    value1, value2 = 15, 23                #7
    df_t7 = task7(df, value1, value2)
    print(df_t7)

    #df = df.groupby(['temp_day', 'temp_f_day']).mean()    #8
    #print(df)

    plt.plot(df['temp_day'])
    plt.title("Temperature graph in Celsius")  #Fahrenheit temperature graph
    plt.xlabel("Day")
    plt.ylabel("Temp")
    plt.plot(df['temp_day'])
    plt.show()

    plt.title("Temperature graph in Fahrenheit")
    plt.xlabel("Day")
    plt.ylabel("Temp")
    plt.plot(df['temp_f_day'])
    plt.show()


    df['data'] =  df['data'].astype(str)  
    print(df.dtypes)
    month, year = 8, 2021
    custom(df, month, year)






if __name__ == '__main__':
    main()   