import random
from tkinter import Scale
import tkinter

import pyperclip


class Password:

    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        self.random_letters = 0
        self.random_numbers = 0
        self.random_symbols = 0

    def scale(self):
        """Display scales for numbers, letters, and symbols"""
        self.scale_letters = Scale(from_=0, to=20, command=self.set_letters_quantity, orient=tkinter.HORIZONTAL, length=200, label="How many letters in password?")
        self.scale_letters.grid(column=1, row=5)

        self.scale_numbers = Scale(from_=0, to=20, command=self.set_numbers_quantity, orient=tkinter.HORIZONTAL, length=200, label="How many numbers in password?")
        self.scale_numbers.grid(column=1, row=6)

        self.scale_symbols = Scale(from_=0, to=20, command=self.set_symbols_quantity, orient=tkinter.HORIZONTAL, length=200, label="How many symbols in password?")
        self.scale_symbols.grid(column=1, row=7)

    def generate_password(self):
        """Generates encrypted password using random module"""
        password_letters = [random.choice(self.letters) for _ in range(self.random_letters)]
        password_numbers = [random.choice(self.numbers) for _ in range(self.random_numbers)]
        password_symbols = [random.choice(self.symbols) for _ in range(self.random_symbols)]

        password_list = password_letters + password_numbers + password_symbols
        random.shuffle(password_list)

        final_password = "".join(password_list)
        pyperclip.copy(final_password)

        return final_password

    def set_letters_quantity(self,value):
        """Sets the number value in random_letters"""
        self.random_letters = int(value)

    def set_numbers_quantity(self, value):
        """Sets the number value in random_numbers"""
        self.random_numbers = int(value)

    def set_symbols_quantity(self, value):
        """Sets the number value in random_symbols"""
        self.random_symbols = int(value)

