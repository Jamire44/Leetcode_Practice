s = "abcabcbb"

def longest_repeats_wo_repeats(s):

    seen = set()
    best = 0
    l = 0

    for r, chr in enumerate(s):
        while chr in seen:
            seen.remove(s[l])
            l+=1
        seen.add(chr)
        best = max(best, r - l + 1)
    return best

print(longest_repeats_wo_repeats(s))