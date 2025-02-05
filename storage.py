import pandas as pd
import os
import csv

class Storage():
    def __init__(self):
        pass

    def get_laptops(self):
        laptops = []
        with open('laptops.csv', 'r', newline = '') as file:
            data = csv.reader(file)
            for item in data:
                laptops.append(item)
        return laptops

    def get_laptop(self, laptop_id):
        laptops = self.get_laptops()
        laptop = laptops[int(laptop_id) - 1]
        return laptop