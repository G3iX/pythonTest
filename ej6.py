# leetcode 13 - Roman to Integer


def rToIn(s):
    RtoID = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    iNum = 0
    RnL = []
    InL= []
    for i in s:
        RnL.append(i)
    for i in RnL:
        InL.append(RtoID[i])
    # iNum += InL[0]
    for i in range(0, len(InL)-1):
        if InL[i] >= InL[i+1]:
            iNum += InL[i]
            # print(iNum)
        else:
            iNum -= InL[i]
            # print("InL[i] - InL[i - 1] = ", InL[i], "-", InL[i - 1])
        #
    iNum += InL[len(InL) - 1]
    print("-------")
    print(iNum)


rToIn("XLIX")


def roicat(s):
    rtoi = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    inum = 0
    temp = []
    for i in s:
        if len(s) > 1:
            temp.append(rtoi[i])
        else:
            inum = rtoi[i]
            break
    for i in range(1, len(temp)):
        inum += temp[0]
        if temp[i - 1] < temp[i]:
            inum -= temp[i]
        else:
            inum += temp[i]
    if inum < 0:
        inum -= inum * 2
    print(inum)

# roicat("LVIII")
