import pandas as pd
import os
import csv

class Filter():
    def __init__(self):
        pass

    def filtering(self, filtered_by, df):
        if filtered_by == 1:
            df_sorted = df.sort_values(by="Price")
            print(df_sorted.head(20))