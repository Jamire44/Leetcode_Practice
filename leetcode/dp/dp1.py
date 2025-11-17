def max_points(board, k):
    n = len(board)
    dp = [0] * n

    for i in range(n-1,-1,-1):
        dp[i] = board[i]
        if i + k < n:
            dp[i] += dp[i+k]
        
    return max(dp)
print(max_points([1,-1,3,5,-2,2],2))