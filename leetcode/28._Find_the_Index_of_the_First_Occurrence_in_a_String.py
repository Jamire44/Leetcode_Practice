def strStr(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle) # 9, 3
    if m == 0:
        return 0

    # for i in range(9 - 3 + 1) = 6 + 1 = 7
    for i in range(n - m + 1):
        # if haystack[1:4]
        if haystack[i:i+m] == needle:
            return i

    return -1

print(strStr("sadbutsad", "but"))