
def printCollection(collection):
    for v in collection:
        print(v,end=" ")
    print()


# Append Function
myList = ["One","Two","Three","Four"]
myList.append("Five")
myList.append("Six")
printCollection(myList)
#------------------------


# Pop Function
print("\n", myList.pop())
print()
#------------------------


# Remove Function
myList.remove("Three")
printCollection(myList)
#------------------------


# Insert Function
myList.insert(2,"Three")
printCollection(myList)
#------------------------


# Extend Collection
myList.extend(["Six","Seven","Eight","Nine","Ten"])
printCollection(myList)
#------------------------

# Manual Iteration Using Index
length = len(myList)
for index in range(length):
    print(myList[index],end=" ")
print()
#------------------------



#Count number of item occurences in a collection
myList.append("Three")
myList.append("Three")
totalThree =  myList.count("Three")
print("Total three: ", totalThree)
#------------------------


#Sort the collection
myList.sort()
printCollection(myList)
#------------------------

#Reverse the collection
myList.reverse()
printCollection(myList)
#------------------------


print()
listNumbers = [1,2,3,4,5,6,7,8,9,10]
print(listNumbers)
print(listNumbers[4:])
print(listNumbers[:5])
print(listNumbers[0:5])
