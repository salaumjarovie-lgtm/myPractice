#Check if a number is positive, negative, or zero.

fromUser = int(input("Enter number: "))
if fromUser > 0:
    print("Number is positive.")
elif fromUser < 0:
    print("Number is negative.")
else:
    print("Number is zero.")