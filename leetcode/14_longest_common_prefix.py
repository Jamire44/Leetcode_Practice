def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]

    for s in strs[1:]:
        # Shrink prefix until it matches the start of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix                
    

print(longestCommonPrefix(["dog", "racecar", "car"]))  # ""
print(longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"