# Largest prime factor


def eratosthenes_sieve(N):  # error
    a = 2
    if N > 600851475143:
        a = 600851475143 - 851475143
    else:
        a = 2
    all_nums_arr = list(range(a, N + 1))
    all_nums_arr[1] = 0
    # prime_nums_arr = []
    # first_prime = 2
    for first_prime in all_nums_arr:
        if all_nums_arr[first_prime] != 0:
            # prime_nums_arr.append(all_nums_arr[first_prime])
            for prime_num in range(first_prime, N + 1, first_prime):
                all_nums_arr[prime_num - 2] = 0
        first_prime += 1
    prime_nums_arr = sorted(list(set(all_nums_arr)))
    prime_nums_arr.pop(0)
    print(prime_nums_arr)


def funcsieve():  # error somewhere
    # 600851475143
    primeNumsArr = [2, 3, 5, 7]
    # print(end="[")
    for Num in range(11, 10000, 2):
        isPrime = True
        if Num > 10:
            if Num % 10 == 5:
                continue
        for primeNum in primeNumsArr:  # still error:) 27..
            if primeNum * primeNum < Num:
                continue
            if Num % primeNum == 0:
                isPrime = False
                break
        if isPrime:
            primeNumsArr.append(Num)
            # print(".", end="")
    # print("]")
    # for i in range(6):
    #     primeNumsArr.pop(0)
    print(primeNumsArr)  # max(
    return primeNumsArr


def NOerrorbutslower():
    primeNumsArr = [2]
    for Num in range(3, 105000, 2):
        isPrime = True
        if Num > 19:
            if Num % 17 == 0:
                continue
            if Num % 13 == 0:
                continue
            if Num % 11 == 0:
                continue
            if Num % 10 == 5:
                continue
            if Num % 7 == 0:
                continue
            if Num % 3 == 0:
                continue
            if Num % 2 == 0:
                continue
        for primeNum in primeNumsArr:
            if primeNum * primeNum * primeNum < Num:
                continue
            if Num % primeNum == 0:
                isPrime = False
                break
        if isPrime:
            primeNumsArr.append(Num)
        if len(primeNumsArr) >= 10001:
            return primeNumsArr
    return primeNumsArr


# eratosthenes_sieve(600851475143)

def do():
    num = 600851475143
    simplenumA = funcsieve()
    while True:
        temp = simplenumA.pop(len(simplenumA) - 1)
        if num % temp == 0:
            print("Answear:", temp)
            break

        # print("deleted", temp)


do()


def alternative():
    num = 600851475143
    count = 1
    while num != 1:
        count += 1
        if num % count == 0:
            num /= count

    print(count)
