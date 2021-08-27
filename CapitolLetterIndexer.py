def capital_indexes(String):
    allChars = []
    toReturn = []
    num = 0
    for i in String:
        if i.isupper():
            num = num + 1
            print(String)
            toReturn.append(String.index(i)+num-1)
            String = String.replace(i, "", num)
            print(String)
            print(num)
    return toReturn


print(capital_indexes("TEsT"))
