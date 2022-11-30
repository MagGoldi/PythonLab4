import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#create some data
var1 = [1, 2, 3, 4, 5, 6]
var2 = [7, 13, 16, 18, 25, 19]
var3 = [29, 25, 20, 25, 20, 18]
var4 = [4, 4, 6, 4, 7, 11]

#define grid of plots
fig, axs = plt.subplots(nrows= 2 , ncols= 2 )

#add title
fig. suptitle('Grid of Plots')

#add data to plots
axs[0, 0].plot(var1, var2)
axs[0, 1].plot(var1, var3)
axs[1, 0].plot(var1, var4)
axs[1, 1].plot(var3, var1)
plt.show()