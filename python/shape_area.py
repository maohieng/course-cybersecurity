
import math

def main():
    x = shapeOfChoice()
    while x == 'n' or x == 'no':
        x = shapeOfChoice()
    
    print('Good bye!')

def shapeOfChoice():
    print('Program to calculate the area of a shape listing below:')
    print('1. Square')
    print('2. Rectangle')
    print('3. Circle')
    print('4. Triangle')
    evalChoice()

    print()
    ext = input('Do you want to exit the program? [y/n] ')
    while ext != 'y' and ext != 'yes' and ext != 'n' and ext != 'no':
        print('Wrong input. Please type y / n / yes / no.')
        ext = input('Do you want to exit the program? [y/n] ')
        print(ext)
    
    return ext

def evalChoice():
    choice = int(input('Please input a number of your choice: '))
    while choice < 1 or choice > 4:
        print('Please input a number from 1 to 4 of choice listing above.')
        choice = int(input('Please input a number of your choice: '))
    
    if choice == 1:
        calSquare()
    elif choice == 2:
        calRectangle()
    elif choice == 3:
        calCircle()
    else:
        calTriangle()

def evalInputLength(name):
    val = eval(input(f'Please input {name}: '))
    while val <= 0:
        print('The input must be positive number.')
        val = eval(input(f'Please input {name}: '))
    
    return val

def calSquare():
    print()
    print('Required data for calculating the area of a square is its side.')
    side = evalInputLength('side')
    area = side * side
    print(f'Area of square side {side} is {area}')

def calRectangle():
    print()
    print('Required data for calculating the area of a Rectangle is its width and height.')
    w = evalInputLength('width')
    h = evalInputLength('height')
    area = w * h
    print(f'Area of rectangle width = {w}, height = {h} is {area}')

def calCircle():
    print()
    print('Required data for calculating the area of a circle is its radius.')
    r = evalInputLength('radius')
    area = math.pi * r * r
    print(f'Area of circle radius = {r} is {area}')

def calTriangle():
    print()
    print('Required data for calculating the area of a Triangle is its base and height.')
    b = evalInputLength('base')
    h = evalInputLength('height')
    area = b * h / 2
    print(f'Area of triangle base = {b}, height = {h} is {area}')

main()