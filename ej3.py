# Largest prime factor
# 600851475143
primeNumsArr = [2]
for Num in range(3, 15):
    for primeNum in primeNumsArr:
        # print(Num, " % ", primeNum, "==", Num % primeNum) # inf. :(
        if Num % primeNum != 0:
            primeNumsArr.append(primeNum)
        else:
            break
print(primeNumsArr)
