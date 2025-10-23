def solution(numbers):
    # a < b > c
    # a < b
    # b > c
    
    # a > b < c
    # a > b
    # b < c
    final_arr = []
    l, m, r = 0, 1, 2
    
    while(r <= len(numbers)-1):
        if numbers[l] < numbers[m] and numbers[m] > numbers[r]:
            final_arr.append(1)
        elif numbers[l] > numbers[m] and numbers[m] < numbers[r]:
            final_arr.append(1)
        else:
            final_arr.append(0)
        
        l+=1
        m+=1
        r+=1

    return final_arr

arr = [1, 2, 1, 3, 4]
solution(arr)