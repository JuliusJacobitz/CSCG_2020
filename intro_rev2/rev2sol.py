"""
b = input("string pls")

a = b.replace("\\",",")

print(b, a)


"""



inCString = "0123456789abcdefghijklmnopqrstu"
inArray = [271,272,273,274,275,276,277,300,301,302,352,353,354,355,356,357,360,361,362,363,364,365,366,367,370,371,372,373,374,375]
solArray = ['s', 't', 'a', '7', '1', 'c', 350, 't', 'r', '4', 'n', '5', 'f', '0', 'r', 'm', '4', '7', '1', '0', 'n', 350, 'i', 't', 350, 'i', 's']


def solrev2(inChar,inNumbers,solArray):
    for indexSol in range(len(solArray)):
        for indexInp in range(len(inNumbers)):
            a = str(inNumbers[indexInp])
            b = str(solArray[indexSol])

            if a == b:

                solArray[indexSol] = inChar[indexInp]


    print(solArray)


solrev2(inCString,inArray,solArray)

#350 ausprobiert musste ja quasi _ oder - oder so sein :)

pw = ""
for i in solArray:
    if i == 350 :
        i = "_"
    pw += str(i)

print(pw)
