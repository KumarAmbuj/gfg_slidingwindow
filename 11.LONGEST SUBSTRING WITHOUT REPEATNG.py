def findlongestSubstring(s):
    mx=0

    map={}
    i=0
    for j in range(len(s)):
        ch=s[j]

        if ch not in map:
            map[ch]=0

        map[ch]+=1

        if j-i+1==len(map):
            mx=max(mx,j-i+1)
        elif len(map)<j-i+1:
            while(len(map)<j-i+1):
                ch=s[i]
                map[ch]-=1
                if map[ch]==0:
                    del map[ch]
                i+=1
    print(mx)

s='pwwkew'
findlongestSubstring(s)