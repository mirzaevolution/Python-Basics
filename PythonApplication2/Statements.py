import constant

"""
    Python Program #1
"""

#line continuation statement

number1 = 1 + 2 + \
          3 + 4 + \
          5 + 6
number2 = (1 + 2 + 
           3 + 4 +
           5 + 6)
print(number1)
print(number2)


# One line assignment
var1,var2,var3 = 1,12.4,"Mirza Ghulam Rasyid"
print(var1)
print(var2)
print(var3)


print(constant.PI)
constant.PI = 123;
print(constant.PI)


binary = 0b10100
octal = 0o37
hexadecimal = 0xaf123

print(binary,octal,hexadecimal)


#myName = input("Input your name: ")
#print("Your name is: ", myName)
#age = int(input("Input your age: "))
#print("You are ", age, " years old",sep="")


myMultiLineString = "This is Mirza. " + \
                    "Mirza is a developer."
print(myMultiLineString)

rawString = r"this is \n raw string \n\f\u"
print(rawString)
