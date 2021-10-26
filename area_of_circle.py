#TODO python program to calculate the area of a circle.

# Firstly, we will take input from the user using the input() function for radius and store it in a variable.
# We can use constant to store the value of ‘pi’.
# Now, we will calculate the area of a circle by using the formula area = PI * r * r.
# And at last, print the area of a circle to get the output.

r = int(input("Enter the Radius: "))

pi = 3.142

area_of_circle = pi * r * r

print("Area of cricle is %d"%(area_of_circle))

#TODO by using function and math module
import math
def area(r):
    area =  math.pi * r * r
    return area

if __name__ == '__main__':
    r = int(input("Enter the Radius: "))
    print("Area of cricle is %d"%(area(r)))