from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for word in wordDict:
                if len(word) > i:
                    continue
                if s[i-len(word): i] == word:
                    dp[i] = dp[i-len(word)]
                    if dp[i]==True:
                        break
        return dp[n]
