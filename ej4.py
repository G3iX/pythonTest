# Largest palindrome product

def pal_check(num):
    numsFromPalindromNumbArr = [int(a) for a in str(num)]  # we make list from our number in order to evaluate numbers
    equality = True
    while len(numsFromPalindromNumbArr) > 1 and equality:
        starting = numsFromPalindromNumbArr.pop(0)
        ending = numsFromPalindromNumbArr.pop(len(numsFromPalindromNumbArr) - 1)
        if starting != ending:
            equality = False;
    return equality


palindromeArr = []
for i in range(900, 1000):
    for a in range(900, 1000):
        if pal_check(i * a):
            palindromeArr.append(i * a)
print(max(palindromeArr))
