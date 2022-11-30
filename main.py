import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task6(df: pd.DataFrame, value: float) -> pd.DataFrame:
    return df.loc[df['temp_day'] >= value]

def task7(df: pd.DataFrame, value1: float, value2: float) -> pd.DataFrame:
    df =  df.loc[df['temp_day'] >= value1]
    df =  df.loc[df['temp_day'] <= value2]
    return df


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
    #plt.show()


    #define grid of plots
    fig, axs = plt.subplots(nrows= 2 , ncols= 1 )

    #add title
    fig. suptitle('Temperature graph')

    #add data to plots
    axs[0].plot(df['temp_day'])
    plt.xlabel("Day")
    plt.ylabel("Temp")
    axs[1].plot(df['temp_f_day'])
    plt.show()

    #plt.plot(df['temp_f_day'])
    #plt.show()





if __name__ == '__main__':
    main()   