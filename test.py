# import pandas as pd

# df = pd.read_csv("laptops.csv", names = ["Brand", "CPU", "GPU", "RAM", "Display", "Price"])

# column_headers = df.columns.tolist()
# print(column_headers)

# filtered_by = input("FILTER BY: ")
# print()
# df = df.sort_values(by = filtered_by)

# print(df.to_string())
# print()
# print()
# print()
# print()
# print()
# print(column_headers)

# # price >= 60000000 and price <= 100000000

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()