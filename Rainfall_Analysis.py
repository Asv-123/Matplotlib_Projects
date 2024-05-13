"""The CSV file labed raindata is used for this project."""

import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('/content/raindata.csv')
print(data)

plt.plot(data.columns[2:],data.iloc[1,2:], marker='o',label = 'New york')
plt.plot(data.columns[2:],data.iloc[5,2:], marker='o',label = 'los Angles')
plt.plot(data.columns[2:],data.iloc[10,2:], marker='o',label = 'Chicago')
plt.plot(data.columns[2:],data.iloc[15,2:], marker='o',label = 'Houston')
plt.plot(data.columns[2:],data.iloc[20,2:], marker='o',label = 'Pheonix')


plt.grid()
plt.xlabel('Months')
plt.ylabel('Rainfall in mm')
plt.title('Rainfall in different cities in 2015')
plt.legend()
plt.show()







