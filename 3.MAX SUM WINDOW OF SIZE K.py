def findmaxsum(arr,k):

    sum=0
    mx=0
    i=0
    for j in range(len(arr)):

        sum+=arr[j]

        size=j-i+1

        if size<k:
            continue

        elif size==k:
            mx=max(mx,sum)
            sum-=arr[i]
            i+=1

    print(mx)

arr=[2,5,1,8,2,9,1]
findmaxsum(arr,3)




