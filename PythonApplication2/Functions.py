#Named arguments
def factorial(number):
    if(number<=1):
        return 1
    else:
        return factorial(number-1) * number;

print(factorial(number=12),"\n")

#Multiple arguments
def printNames(*names):
    if(len(names)>0):
        print("**********************\n")
        for name in names:
            print(name)
        else:
            print("\n**********************")
    else:
        print("No names to print")

printNames("Mirza Ghulam Rasyid","Michael Hawk","Han Jensen")

#Lambda - one parameter
power = lambda num: num*num;

print("\nLambda #1: power(12) =",power(12))

#Lambda - two parameters
multiply = lambda num1,num2: num1 * num2;
print("Lambda #2: multiply(3,5) =",multiply(3,5))


#Filter lambda
myList = list(range(1,11))

for item in list(filter(lambda number: number%2==0, myList)):
    print(item,end=' ')

print()
 
 #Map lambda

for item in list(map(lambda number: number*2,myList)):
    print(item,end=' ')


print()