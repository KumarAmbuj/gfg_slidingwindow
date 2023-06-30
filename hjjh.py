def findgroup():
    N=int(input())
    numberlist=[]

    for i in range(N):
        numberlist.append(int(input()))

    N2=int(input())
    S=int(input())

    flag=1
    for i in range(S,len(numberlist),S):

        if N2 not in numberlist[i-S:i]:
            flag=0
            break
    return flag



