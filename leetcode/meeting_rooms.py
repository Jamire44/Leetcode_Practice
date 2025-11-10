def meeting(start, end):
    i,j = 0, 0
    cores_atm, max_cores = 0, 0

    while i < len(start) and j < len(end):
        if start[i] <= end[j]:
            cores_atm+=1
            max_cores = max(max_cores, cores_atm)
            i+=1
        else:
            j+=1
            cores_atm-=1
    return max_cores


start = [1,3,5]
end = [3,5,6]
print(meeting(start, end))