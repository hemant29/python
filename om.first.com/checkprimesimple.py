import sys
number = int(input("Please enter a number" + "\n" + ">>>"))
#number = int(number)
prime = False #initiate boolean for true false, default false
if number > 0:
    for x in range (2, number - 1): #this range excludes number and 1, both of which number is divisible by
        if number % x != 0: #If number isn't evenly divisible by x, start over with the next one
            continue 
        elif number % x == 0: #If number is evenly divisible by x, it can't be prime
            #print("The number is not prime.")
            prime = True
            break
    if prime:
            print("The number is not prime.") #number wasn't evenly divisible by any x, so it's prime
    else :
        print("The number is prime.")
elif number == 0:
    print("The number is not prime.") #According to the Google, 0 is not prime
else:#if number is less than 0, the number is not prime (according to the Google).
    sys.exit(0)
