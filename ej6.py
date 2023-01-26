# Sum square difference
# - N^2 + N^3 (N in range(101))

def hundred():
    sum2 = 0
    sum3 = sum2
    for i in range(1, 101):
        sum2 += i
        sum3 += i * i
        # print(i, "+ itself = ", sum2, ";")
        # print(i, "^2= ", sum3, ";")
    sum2 = sum2*sum2
    return sum2 - sum3


print(hundred())
