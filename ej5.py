# Smallest multiple
# 2520
def type2():
    top = 20
    numArr = range(top, 0, -1)
    count = 1
    sum = top
    lstCount = numArr[count]
    while lstCount != 1:
        tmp = sum
        while sum % lstCount != 0:
            sum += tmp
        count += 1
        lstCount = numArr[count]
    print(sum)


type2()
