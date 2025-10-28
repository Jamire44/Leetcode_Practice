def coinChange(coins: list[int], amount: int):

    coins.sort()
    dp = [0] * amount + 1

    for i in range(1, amount+1):
        minn = float('inf')

        for coin in coins:
            diff = i - coin
            if diff < 0:
                break
            minn = min(minn, dp[diff] + 1)

        dp[i] = min

    if dp[amount] < float('inf'):
        return dp[amount]
    else:
        return -1
