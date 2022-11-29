import pandas as pd
import numpy as np

def main() -> None:

    df = pd.read_csv("C:\PYTHON\PythonLab4\dataset2.csv") #1

    df.columns =['data', 'temp_day', 'wind', 'pressure_day', 'temp_evening', 'pressure_evening'] #2

    df_without_nan = df.dropna()  #3  ( null / None / Nan ) ////
    df = df.dropna() 
    print(df_without_nan)

    print('------------------------------')
    print('\nNew Datatypes\n', df.dtypes, sep='') 
    df1 = df.astype("int64", errors='ignore')
    df1.head()
    df1.info()

    df['temp_day'] = pd.to_numeric(df['temp_day'])


    
    #df = df.astype({'temp_day': np.char})
    #print(df)


    #df = df.assign(temp_f_day = df.temp_day +1)
    #df = df.assign(temp_f_even = df.temp_evening +"1")
    #print(df)



if __name__ == '__main__':
    main()   