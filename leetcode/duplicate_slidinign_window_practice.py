def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    longest = 0
    sett = set()
    n = len(s)

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l+=1
        
        window = (r-1)+1
        longest = max(longest, window)
        sett.add(s[r])

    return longest
