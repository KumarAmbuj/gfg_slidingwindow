def findlongestsubstring(s,k):
    map={}

    mx=0
    i=0

    for j in range(len(s)):
        ch=s[j]

        if ch not in map:
            map[ch]=0

        map[ch]+=1

        if len(map)<k:
            continue
        elif len(map)==k:
            mx=max(mx,j-i+1)
        elif len(map)>k:
            while(len(map)>k):
                ch=s[i]

                map[ch]-=1

                if map[ch]==0:
                    del map[ch]

                i+=1
    print(mx)
s='aabacbebebe'
findlongestsubstring(s,3)




