# this is leet code solution (322)

def coinChange(coins, amount):
    # Initialize a list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Iterate through coin denominations and update the dp array
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
amount = 11
result = coinChange(coins, amount)
print(result)  # Output: 3 (11 = 5 + 5 + 1)

