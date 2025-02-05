from colorama import Fore
import requests as req
import csv

def validate(string):
    valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.0123456789 "
    res = ''
    for c in string:
        if c in valid:
            res += c
    return res.strip()

print("Fetching Data...")
print("(This Might Take A Few Seconds)")

for page in range(1, 11):
    laptops = []
    url = f"https://api2.zoomit.ir/catalog/api/products/search?pageNumber={page}&categorySlug=laptop&pageSize=200"
    response = req.get(url).json()
    products = response["products"]
    source = products["source"]

    for laptop in source:
        other = laptop["keySpecifications"]
        brand = laptop["brand"]["englishTitle"]
        cpu = validate(other[1]["primaryValue"])
        gpu = validate(other[1]["secondaryValue"])
        ram = validate(other[2]["primaryValue"])
        display = validate(other[0]["primaryValue"])
        price = int(laptop["minPrice"])
        
        laptop_list = [brand, cpu, gpu, ram, display, price]

        with open('laptops.csv', 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(laptop_list)

print()    
print(Fore.GREEN + "Data Collected Successfuly!")
print()