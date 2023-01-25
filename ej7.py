import collections

magazine = "asd"
# print([*magazine])

ransomNote = collections.Counter(magazine)
# print(ransomNote)
# = [*magazine]

# adoda = ransomNote.pop(0)
# print(adoda)


# string = "geeks"
# print([*string])
def das():
    mg = [*magazine]
    rn = [*ransomNote]
    if len(mg) < len(rn):
        return False
    else:  # len(mg) >= len(rn)
        for i in range(len(mg) - 1):
            while len(rn) > 0:
                if rn[i] == mg[i]:
                    rn.pop(i)
                    mg.pop(i)
                    if (len(rn)) == 0:
                        return True
                    # return False
                else:
                    break
        return False


def Construct(ransomNote, magazine):
    rm = collections.Counter(ransomNote)
    mg = collections.Counter(magazine)

    for leter_char, letter_amount in rm.items():
        if leter_char not in mg or mg[leter_char] < letter_amount:
            return False

    return True


print(Construct("baa", "aab"))

def canCon(ransomNote, magazine):
    mg = [*magazine]
    rn = [*ransomNote]
    if len(mg) < len(rn):
        return False
    else:
        for i in range(len(rn)):
            if rn[i] == mg[i]:
                rn.pop(i)
                mg.pop(i)
                if len(rn) == 0:
                    return True
            #else:

# print(canCon("aa", "aa"))
# print(canCon("aa", "aab"))
# print(canCon("aa", "ab"))

# print(canCon("a", "b"))
# print(canCon("baa", "aab"))
