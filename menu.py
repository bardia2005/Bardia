from colorama import Style, Fore, Back
from user import User
from storage import Storage
import pandas as pd
import time
import os

def clean():
    os.system("cls")

class Menu():
    def __init__(self):
        self.user = User()
        self.storage = Storage()
    
    def main_menu(self):
        print()
        print(Fore.BLUE + "================== " + Fore.RED + "MAIN MENU" + Fore.BLUE + " ==================")
        print()
        print(Fore.GREEN + "                  1. Sign in                    ")
        print(Fore.GREEN + "                  2. Sign up                    ")
        print(Fore.GREEN + "                  3. Exit                       ")
        print()
        choice = input(Fore.WHITE + "Choose Option: ")

        if choice == '3':
            exit()
        if choice == '2':
            clean()
            self.sign_up()
        if choice == '1':
            clean()
            self.sign_in()
        else:
            print()
            print(Fore.RED + "Invalid input, try again...")
            time.sleep(2)
            clean()
            self.main_menu()

    def sign_up(self):
        username = input(Fore.BLUE + "Enter your Username: ")
        password = input(Fore.BLUE + "Enter your Password: ")
        res = self.user.register_user(username, password)
        print()
        if res == False:
            print(Fore.RED + "This account already exists, Please Sign in...")
        else:
            print(Fore.GREEN + "Account Successfuly Made, Redirecting...")
        time.sleep(2)
        clean()
        self.main_menu()
    
    def sign_in(self):
        username = input(Fore.WHITE + "Enter Your Username: ")
        password = input(Fore.WHITE + "Enter Your Password: ")
        res = self.user.load_user(username, password)
        if res == False:
            print()
            print(Fore.RED + "Incorrect Username/Password, Please try again...")
            time.sleep(2)
            clean()
            self.main_manu()
        else:
            print()
            print(Fore.GREEN + "Successfuly Signed in, Redirecting...")
            time.sleep(2)
            clean()
            self.login_menu()
    
    def login_menu(self):
        print()
        print(Fore.BLUE + "================== " + Fore.RED + "SHOPPING MENU" + Fore.BLUE + " ==================")
        print()
        print(Fore.GREEN + "                  1. Show Laptops                    ")
        print(Fore.GREEN + "                  2. Show Shopping-Cart                    ")
        print(Fore.GREEN + "                  3. Exit                       ")
        print()
        choice = input(Fore.WHITE + "Choose Option: ")

        if choice == '3':
            exit()
        if choice == '2':
            clean()
            self.shopping_cart()
        if choice == '1':
            clean()
            self.show_laptops()
        else:
            print()
            print(Fore.RED + "Invalid input, try again...")
            time.sleep(2)
            clean()
            self.login_menu()

    def shopping_cart(self):
        
        cart = self.user.cart
        for laptop_id in cart:
            print(cart.index(laptop_id) + 1, *self.storage.get_laptop(laptop_id))

        print()
        print(Fore.BLUE + "1. Delete One")
        print(Fore.BLUE + "2. Delete All")
        print(Fore.BLUE + "3. Buy All")
        print(Fore.BLUE + "4. Back")
        print()
        choice = input(Fore.WHITE + "Enter Your Choice: ")
        print()
        
        if choice == '4':
            clean()
            self.login_menu()
        if choice == '3' or choice == '2':
            clean()
            self.user.remove_all_cart()
            self.login_menu()
        if choice == '1':
            id = int(input(Fore.WHITE + "Enter ID to remove: "))

            clean()
            self.user.remove_item_from_cart(id)
            self.login_menu()
    
    def show_laptops(self):

        df = pd.read_csv("laptops.csv")
        print(df.head(20))

        print()
        print(Fore.GREEN + "1. Add laptop to cart")
        print(Fore.GREEN + "2. Go Back")
        print(Fore.GREEN + "3. Filter")
        print()
        choice = input(Fore.WHITE + "Choose Option: ")

        # if choice == '3':
        #     print(Fore.GREEN + "1. Brand name")
        #     print(Fore.GREEN + "2. CPU")   
        #     print(Fore.GREEN + "2. GPU")   
        #     print(Fore.GREEN + "2. RAM")   
        #     print(Fore.GREEN + "2. Display")   
        #     print(Fore.GREEN + "2. Price")   
        #     print()
        #     filtered_by = int(input("Filter by: "))
        #     self.filter.filtering(filtered_by, df)

        if choice == '2':
            clean()
            self.login_menu()
        if choice == '1':
            id = input(Fore.WHITE + "Enter ID to add: ")
            clean()
            self.user.add_to_cart(id)
            self.login_menu()        
        else:
            print()
            print(Fore.RED + "Invalid input, try again...")
            time.sleep(2)
            clean()
            self.show_laptops()        
            Fore.WHITE

# Driver Code

menu = Menu()
menu.main_menu()
