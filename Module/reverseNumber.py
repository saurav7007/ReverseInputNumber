#### Creating a module to compile all the methods for reverse number ####

#### First method to reverse the number ####

def rev1(inputNumber):
    reverseNumber = 0

    while inputNumber != 0:
        remainder = inputNumber % 10
        reverseNumber = reverseNumber * 10 + remainder
        inputNumber = inputNumber // 10

    print('Your reverser number is :', reverseNumber)
