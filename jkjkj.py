def finddeno():
    N=int(input())
    cur=[]

    for i in range(N):
        cur.append(int(input()))
    M=int(input())
    dp=[0 for i in range(M+1)]
    dp[0]=1
    for i in range(1,M+1):

        sm=0
        for j in range(len(cur)):

            if i-cur[j]>=0:
                sm+=dp[i-cur[j]]

        dp[i]=sm
    return dp[M]

