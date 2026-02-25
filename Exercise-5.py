#Classify the grade based on the score.

fromUser = int(input("Enter grade: "))
if fromUser >= 90 and fromUser <= 100:
    print("You got an A.")
elif fromUser >= 80 and fromUser < 90:
    print("You got a B.")
elif fromUser >= 70 and fromUser < 80:
    print("You got a C.")
elif fromUser >= 60 and fromUser < 70:
    print("You got a D.")
elif fromUser >= 0 and fromUser < 60:
    print("You got an F.")
else:
    print("Invalid output.")