def findfirstnegativeNo(arr,k):

    l=[]
    s=[]

    i=0

    for j in range(len(arr)):

        if arr[j]<0:
            s.append(arr[j])

        size=j-i+1

        if size<k:
            continue
        elif size==k:

            if len(s)==0:
                l.append(0)
            else:
                l.append(s[0])

            if len(s)>0 and arr[i]==s[0]:
                s.pop(0)
            i+=1

    print(l)

arr=[12,-1,-7,8,-15,30,16,28]
findfirstnegativeNo(arr,3)


