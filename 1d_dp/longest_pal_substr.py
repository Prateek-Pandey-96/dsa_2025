class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mx_len = 1
        result = ''

        if n == 1:
            return s
        # check odd substrings first
        for i in range(n):
            j, k = i, i
            while j>=0 and k<n and s[j] == s[k]:
                j -= 1
                k += 1
            k -= 1
            j += 1
            mx_len = max(mx_len, k-j+1)
            if mx_len == k-j+1:
                result = s[j:k+1]

        # check even substrings now
        for i in range(n-1):
            if s[i] == s[i+1]:
                j, k = i, i+1
                while j>=0 and k<n and s[j] == s[k]:
                    j -= 1
                    k += 1
                k -= 1
                j += 1
                mx_len = max(mx_len, k-j+1)
                if mx_len == k-j+1:
                    result = s[j:k+1]
        
        return result
