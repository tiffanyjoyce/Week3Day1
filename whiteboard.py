def rizz(n):
    n += 1 #range function is exclusive so if we want n to print we must add one
    for x in range(1,n): #loops through range of numbers
        if x % 3 == 0 and x % 5 == 0: #if number in range is divisable by 3 and 5
            print("FizzBuzz") #print
        elif x % 5 == 0: #if number is divisable by 5
            print("Buzz") #print
        elif x % 3 == 0: #if number is divisable by 3
            print("Fizz") #print
        else:
            print(x)

rizz(7) #runs code