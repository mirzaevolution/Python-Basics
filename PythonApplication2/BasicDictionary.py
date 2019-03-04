def printDictionary(dictionary):
    for key in dictionary.keys():
        print(key,"=>", dictionary.get(key),end=" ")
    print()


numbers = { "one":1, "two":2, "three":3 }
printDictionary(numbers)


print(numbers.get("two"))

numbers.update({ "four": 4, "five":5 })
printDictionary(numbers)

print(numbers.pop("four"))
printDictionary(numbers)


print(numbers.popitem())
printDictionary(numbers)


