from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if coin > i:
                    continue
                dp[i] = min(dp[i], 1 + dp[i-coin])

        return int(dp[amount]) if dp[amount] != float("inf") else -1
