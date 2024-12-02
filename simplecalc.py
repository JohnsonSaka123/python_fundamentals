# a simple python calculator
number_1= int(input("Enter a numbers x: "))
number_2 = int(input("Enter a number y: "))

options = input("addition(A) or subtraction(S) or multiply(M) or divide(D): ")

if options == "addition":
    add = number_1 + number_2
    print(add)
elif options == "subtraction":
    sub = number_1 - number_2
    print(sub)
elif options == "multiply":
    multi = number_1 * number_2
    print(multi)
else:
    div = number_1 / number_2
    print(div)
