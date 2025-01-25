number_1 = int(input("Please enter the first number:"))

number_2 = int(input("please enter the second number:"))

char = input("please enter the operation you want to perform +,-,*,/,%:")

if(char=='+'):

    print(number_1+number_2)

elif(char=='-'):
    print(number_1-number_2)

elif(char=='*'):
    print(number_1*number_2)

elif(char=='/'):
    print(number_1 / number_2)

elif(char=='%'):
    print(number_1 % number_2)
else:
    print("Invalid character")
