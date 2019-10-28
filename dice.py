import random

def dice():
    ans = "yes";
    while ans == "yes":
        print(random.randrange(6))
        ans = input("want to roll the dice again?, if so type 'yes': ")

dice()
