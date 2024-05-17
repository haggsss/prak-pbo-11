# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:09:16 2024

@author: kusfi
"""

def full_name_decorator(func):
    def wrapper(first_name, last_name, title, nim):
        full_name = f"{title} {first_name} {last_name} - NIM: {nim}"
        return f"Full Name: {full_name}"
    return wrapper

@full_name_decorator
def display_name(first_name, last_name, title, nim):
    pass

# Contoh penggunaan
first_name = "Syahrul"
last_name = "Arifin"
title = "Mr."
nim = "064002300031"

print(display_name(first_name, last_name, title, nim))

