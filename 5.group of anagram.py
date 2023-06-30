def findGroupAnagram(s,pat):
    map={}


    for x in pat:
        if x not in map:
            map[x]=0
        map[x]+=1

    res=0
    count=len(map)

    i=0

    for j in range(len(s)):

        ch=s[j]

        if ch in map:
            map[ch]-=1

            if map[ch]==0:
                count-=1

        size=j-i+1

        if size<len(pat):
            continue

        elif size==len(pat):

            if count==0:
                res+=1

            ch=s[i]

            if ch in map:
                map[ch]+=1

                if map[ch]==1:
                    count+=1
            i+=1
    print(res)

s='aabaabaa'
p='aaab'
findGroupAnagram(s,p)
