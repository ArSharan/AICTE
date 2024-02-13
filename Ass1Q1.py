def find_biggest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

biggest = find_biggest(num1, num2)
print("The biggest number is:", biggest)