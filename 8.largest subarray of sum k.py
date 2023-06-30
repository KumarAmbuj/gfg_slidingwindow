def findlargestsubarray(arr,k):

    mx=0
    i=0
    sum=0

    for j in range(len(arr)):

        sum+=arr[j]

        if sum<k:
            continue

        elif sum==k:
            mx=max(mx,j-i+1)
        elif sum>k:

            while(sum>k):

                sum-=arr[i]
                i+=1

                if sum==k:
                    mx=max(mx,j-i+1)




    print(mx)

arr=[4,1,1,1,2,3,5]
findlargestsubarray(arr,5)


