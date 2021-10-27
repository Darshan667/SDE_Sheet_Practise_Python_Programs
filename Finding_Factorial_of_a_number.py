
#TODO Finding Factorial for a given Number

#TODO WAY-1 Normal methode

    #TODO Conditions
    # 1. The number should not be less than 0
    # 2. The factorial of number 0 is always 1
    # 3. sample exmple 5! = 120 i.e (5*4*3*2*1)
    #    so that we are using for loop in the range from 1 to num+1 

#TODO program

user_input = int(input("Enter your favorite Number: ")) # taking input from the user
number = 1                                              # initially the number is 1
if user_input < 0:                                      # if number is less than 0
    print("No negative number, please enter a value more than 1")
elif user_input == 0:                                   # if number is equal to zero
    print("The Factorial of number 0 is always 1")
else:
    for i in range(1,user_input+1):
        number *=  i
    print(number)                                       # printing the factorial for given number
         
#TODO WAY-2 Using recursive methode

    #TODO Condition
    # 1. The number should not be less than 0
    # 2. The factorial of number 0 is always 1
    # 3. Finding factorial using formula i.e [num * fact(num-1)]

def fact(number):
    if number == 1:
        return 1
    elif number == 0:
        return number
    else:
        return (number * fact(number-1))

if __name__ =='__main__':
    user_input = int(input("Enter your favorite Number: "))
    if user_input < 0:
        print("No negative number, please enter a value more than 1")
    elif user_input == 0:
        print("The Factorial of number 0 is always 1")
    else:
        print("Factorial of %d is:" %(user_input),fact(user_input))