# Largest palindrome product
from pip._vendor.pyparsing import Optional


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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:  # slow
        NuElLi = []
        while head is not None:
            NuElLi.append(head.val)
            head = head.next
        equality = True
        while len(NuElLi) > 1 and equality:
            starting = NuElLi.pop(0)
            ending = NuElLi.pop(len(NuElLi) - 1)
            if starting != ending:
                equality = False
        return equality
