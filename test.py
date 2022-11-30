
# import required libraries
import numpy as np
import pandas as pd
  
# create a Dataframe
Mydataframe = pd.read_csv("C:\PYTHON\PythonLab4\dataset_test.csv") #1
  

print(Mydataframe)
  
nan_value = float("NaN")
Mydataframe.replace(" ", nan_value, inplace=True)
print(Mydataframe)
  
Mydataframe = Mydataframe.dropna()
print(Mydataframe)



  