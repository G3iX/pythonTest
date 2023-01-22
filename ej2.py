# Even Fibonacci numbers
FibonacciNumbersArr = [1, 2]
i = 0
while True:
    NewFibonacciNumber = FibonacciNumbersArr[i] + FibonacciNumbersArr[i+1]
    FibonacciNumbersArr.append(NewFibonacciNumber)
    FibonacciNumbers2MultiplesArr = list(filter(lambda x: x % 2 == 0, FibonacciNumbersArr))
    if sum(FibonacciNumbers2MultiplesArr) >= 4000000:
        print(FibonacciNumbers2MultiplesArr)
        # print(FibonacciNumbersArr)
        # FibonacciNumbers2MultiplesArr = list(filter(lambda x: x % 2 == 0, FibonacciNumbersArr))
        # print(FibonacciNumbers2MultiplesArr)
        # print(sum(FibonacciNumbersArr))
        print(sum(FibonacciNumbers2MultiplesArr))
        break
    i += 1
    # FibonacciNumbersArr.append(NewFibonacciNumber)
