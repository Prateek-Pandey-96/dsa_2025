class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        if n == 1:
            return 1
        
        # check odd substrings first
        for i in range(n):
            j, k = i, i
            while j>=0 and k<n and s[j] == s[k]:
                j -= 1
                k += 1
                count += 1

        # check even substrings now
        for i in range(n-1):
            if s[i] == s[i+1]:
                j, k = i, i+1
                while j>=0 and k<n and s[j] == s[k]:
                    j -= 1
                    k += 1
                    count += 1
        
        return count
