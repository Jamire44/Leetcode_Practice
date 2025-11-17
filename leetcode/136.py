nums = [2,2,1]

def singleNumber(nums: list[int]):
    mapp = {}
    for num in nums:
        mapp[num] = mapp.get(num, 0) + 1

    # print(mapp)

    for k, v in mapp.items():
        if v == 1:
            return k

print(singleNumber(nums))