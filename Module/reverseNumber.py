#### Creating a module to compile all the methods for reverse number ####

#### First method to reverse the number ####

def rev1(inputNumber):
    reverseNumber = 0                                       ## Declearing a variable for reversed number

    while inputNumber != 0:                                 ## running a while loop untill input number becomes zero
        remainder = inputNumber % 10                        ## storing the value of remainder in a variable
        reverseNumber = reverseNumber * 10 + remainder      ## multiplying reverser number value with 10. This will increase the value of a number by 10th place.
                                                            ## Example: 1 * 10 = 10, 10 * 10 = 100, 100 * 10 = 1000, and so on.
        inputNumber = inputNumber // 10                     ## Taking out the quotient from input number

    print('Your reverser number is :', reverseNumber)       ## Print the reversed number

#### Second method to reverse the number ####

def rev2(inputNumber):
    inputNumber = str(inputNumber)                          ## convering the input integer to string
    
    reverseNumber = ''                                      ## Declaring a empty string value for reversed number
	                                              
    for number in inputNumber:                              ## running for loop for inputNumber
       reverseNumber = number + reverseNumber               ## Appending each character in the start of a string
       
    reverseNumber = int(reverseNumber)                      ## Type casting the string into number
  
    print('Your reverse number is :',reverseNumber)         ## Print the reversed number
