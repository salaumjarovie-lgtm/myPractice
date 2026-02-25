#Get the sum of the number until the user enters 0.

count = 0
while True:
    fromUser = int(input("Enter number: "))
    count += fromUser
    if fromUser == 0:
        break   
print(count)