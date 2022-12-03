import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def index_change(df):
    test = df.shape[0]                              #3.5
    df.index = [i for i in range(0, int(test))]
    return df

def task6(df: pd.DataFrame, value: float) -> pd.DataFrame:
    return df.loc[df['temp_day'] >= value]

def task7(df: pd.DataFrame, value1: float, value2: float) -> pd.DataFrame:
    df =  df.loc[(df['temp_day'] >= value1) & (df['temp_day'] <= value2)]
    return df

def custom(df: pd.DataFrame, month: int, year: int) -> pd.DataFrame:
    if(month<10): month = "0"+str(month) 
    data1 = str(str(year)+"-"+ month +"-"+"01")
    data2 = str(str(year)+"-"+ month +"-"+"31")

    df_custom = df.loc[(df['data'] >= data1) & (df['data'] <= data2)]
    df_custom = index_change(df_custom)
    print(df_custom)  
    
    plt.violinplot(df_custom['temp_day'], showmedians=True)
    plt.plot(df_custom['temp_day'])
    plt.title("Temperature graph in Celsius")  #Fahrenheit temperature graph
    plt.xlabel("Day")
    plt.ylabel("Temp")
    plt.plot(df_custom['temp_day'])
    plt.show()




def main() -> None:

    df = pd.read_csv("C:\PYTHON\PythonLab4\dataset.csv") #1
    print(df)

    df.columns = ['data', 'temp_day', 'wind', 'pressure_day', 'temp_even', 'pressure_even'] #2
    print(df)
    
    nan_value = float("NaN")                        #3  ( null / None / Nan ) ////
    df.replace(" ", nan_value, inplace=True)
    df = df.dropna()
    print(df)

    df = index_change(df)
    print(df)

    df[['temp_day', "temp_even"]] =  df[['temp_day', "temp_even"]].astype(int)        #4
    print(df.dtypes)
    df = df.assign(temp_f_day = (df.temp_day *9/5) +32, temp_f_even = (df.temp_even*9/5) +32)
    print(df)

    stats = df[['temp_day', "temp_even", "temp_f_day", "temp_f_even"]].describe()     #5
    print(stats)

    value = 20                             #6
    df_t6 = task6(df, value)
    df_t6 = index_change(df_t6)
    print(df_t6)

    value1, value2 = 15, 23                #7
    df_t7 = task7(df, value1, value2)
    df_t6 = index_change(df_t7)
    print(df_t7)

    df_tmp = df.groupby(['temp_day', 'temp_f_day']).mean()    #8
    print(df_tmp)

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