def findminwindow(s,p):
    map={}
    for x in p:
        if x not in map:
            map[x]=0
        map[x]+=1


    mn=9999
    res=''

    count=len(map)
    i=0

    for j in range(len(s)):
        ch=s[j]

        if ch in map:
            map[ch]-=1

            if map[ch] == 0:
                count -= 1

        if count>0:
            continue

        elif count==0:


            while(count==0):
                if j-i+1<mn:
                    mn=j-i+1
                    res=s[i:j+1]
                ch=s[i]
                if ch in map:
                    map[ch]+=1
                    if map[ch]==1:
                        count+=1
                i+=1
    print(mn)
    print(res)

s='totmaptat'
p='tat'
findminwindow(s,p)









