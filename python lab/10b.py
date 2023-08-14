import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('data.csv')
print("\nTop 5\n")
print(data.head(5))
print("\nBottom 5\n")
print(data.tail(5))
print("\nInformation\n")
print(data.info())
print("\nDescription\n")
print(data.describe())
data.plot()
plt.title("Visualization of the Dataset")
plt.show()
