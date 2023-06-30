def findmaxofSubarray(arr,k):
    s=[]
    res=[]
    i=0
    for j in range(len(arr)):
        while(len(s)>0 and s[-1]<arr[j]):
            s.pop()
        s.append(arr[j])

        size=j-i+1

        if size<k:
            continue

        elif size==k:
            res.append(s[0])
            
            if arr[i]==s[0]:
                s.pop(0)

            i+=1
    print(res)

arr=[1,3,-1,-3,5,3,6,7]
findmaxofSubarray(arr,3)

