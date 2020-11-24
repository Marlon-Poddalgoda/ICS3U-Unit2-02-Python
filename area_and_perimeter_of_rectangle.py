#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on November 2020
# This program calculates the area and perimeter of a rectangle
#     with user input


def main():
    # this function calculates the area and perimeter

    # input
    Length = int(input("Enter length of the rectangle (mm): "))
    Width = int(input("Enter width of the rectangle (mm): "))

    # process
    area = Length*Width
    perimeter = 2*(Length+Width)

    # output
    print("")
    print("Area is {} mm²".format(area))
    print("Perimeter is {} mm".format(perimeter))


if __name__ == "__main__":
    main()
