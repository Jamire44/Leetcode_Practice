def common_prefix(a, b):
    prefix = ""
    for x, y in zip(a,b):
        if x == y:
            prefix += x
        else:
            break
    return prefix


def LCP(arr1, arr2):
    longest = ""

    for num1 in arr1:
        for num2 in arr2:
            prefix = common_prefix(str(num1), str(num2))
            if len(prefix) > len(longest):
                longest = prefix
    return longest


arr1 = [123, 545467, 454, 7765, 4566]
arr2 = [2, 334, 546, 545468]

print(LCP(arr1,arr2))