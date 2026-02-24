#print("Hello! This is my first Python program.")



# positive, negative, or zero
#fromUser = int(input("Enter number: "))
#if fromUser > 0:
#    print("Number is positive.")
#elif fromUser < 0:
#    print("Number is negative.")
#else:
#    print("Number is zero.")

# voting eligibility
#fromUser = int(input("Enter age: "))
#if fromUser >= 18:
#    print("You are eligible to vote.")
#else:
#    print("You are not eligible to vote.")

# grade classifier
#fromUser = int(input("Enter grade: "))
#if fromUser >= 90 and fromUser <= 100:
#    print("You got an A.")
#elif fromUser >= 80 and fromUser < 90:
#    print("You got a B.")
#elif fromUser >= 70 and fromUser < 80:
#    print("You got a C.")
#elif fromUser >= 60 and fromUser < 70:
#    print("You got a D.")
#elif fromUser >= 0 and fromUser < 60:
#    print("You got an F.")
#else:
#    print("Invalid output.")

# sum until zero
#count = 0
#while True:
#    fromUser = int(input("Enter number: "))
#    count += fromUser
#    if fromUser == 0:
#        break   
#print(count)

# print even numbers
count = 0
for i in range(20):
    for i %2 == 0:
        count += 1
    
    print(i)