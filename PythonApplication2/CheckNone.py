myNoneValue = None
myIntValue = 1234

def CheckNone(inputValue):
    if(inputValue==None):
        print("Cannot input None value")
    else:
        print(inputValue)


CheckNone(myNoneValue)
CheckNone(myIntValue)


