#print out number from 1 to 100
#print multiples of 3, print "fizz"
#print multiples of 5, print "buzz"
# instead of printing of both 3 and 5 , print "fizzbuzz"

for i in range(1,101):
    if(i % 3 == 0) and (i % 5 == 0):
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
         print("buzz")
    else:
        print(i)