import os
import csv

class User():
    def __init__(self):
        self.username = None
        self.password = None
        self.cart = []
        
    def get_users(self):
        users = []
        with open('users.csv', 'r', newline = '') as file:
            data = csv.reader(file)
            for user in data:
                users.append(user)
        return users
    
    def load_user(self, username, password):
        users = self.get_users()
        for user in users:
            if user[0] == username and user[1] == password:
                self.username = username
                self.password = password
                self.cart = eval(user[2])
                return True
        return False
    
    def register_user(self, username, password):
        users = self.get_users()
        for user in users:
            if user[0] == username:
                return False
        self.username = username
        self.password = password
        self.cart = []
        self.update_user()

    def update_user(self):
        is_in = False
        users = self.get_users()
        for user in users:
            if user[0] == self.username:
                users[1] = self.password
                user[2] = self.cart
                is_in = True
                break

        if not is_in:
            users.append([self.username, self.password, self.cart])
        
        with open('users.csv', 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerows(users)

    def add_to_cart(self, laptop_id):
        self.cart.append(laptop_id)
        self.update_user()
    
    def remove_item_from_cart(self, laptop_id):
        try:
            self.cart.pop(laptop_id - 1)
            self.update_user()
            return True
        except:
            return False
    
    def remove_all_cart(self):
        self.cart = []
        self.update_user()