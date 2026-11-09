#!/usr/bin/env python3
# Created By: Maeva Tchuenga
# Date: 09, 12 2026
# this program is to find if the area of a rectangle is equal to a
# square.
from logging import root
import math


def main():

    # Get the length and width of the rectangle from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # calculate the area of the rectangle
    area = length * width

    # check if the area is a square.
    root = math.sqrt(area)

    try:
        if length == width and length > 0 and width > 0:
            print(f"The area of the rectangle is a square.")

        elif length <= 0 or width <= 0:
            print("The length and width must be positive numbers.")

        else:
            print(f"The area of the rectangle is not a square.")

    except Exception:
        print("Sorry! user_input is not an integer.")

    if __name__ == "__main__":
        main()
