# Smallest multiple
# 2520
def type2():
    maxRange = 20
    lst = range(maxRange, 0, -1)
    count = 1
    sum = maxRange

    lstCount = lst[count]
    while lstCount != 1:
        tmp = sum
        while sum % lstCount != 0:
            sum += tmp
        count += 1
        lstCount = lst[count]
    print(sum)


type2()
