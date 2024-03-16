def toNumber(roman):
    numbers={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }
    total = 0
    i=0
    oncekiHarf=""
    for i in range(0,len(roman)-1):
        for x,y in numbers.items():
            if roman[i]==x and y<numbers[roman[i+1]]:
                total+=numbers[roman[i+1]]-y


                break

            elif y>numbers[roman[i-1]] and i!=0:
                break

            elif roman[i]==x:

                total+=y

                break

    if numbers[roman[len(roman)-2]]>numbers[roman[len(roman)-1]]:
        total+=numbers[roman[len(roman)-1]]


    return total


print(toNumber("MCMVII"))
print(toNumber("MMXI"))
print(toNumber("XC"))
print(toNumber("MCMXC"))


