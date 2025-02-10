class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []  # Fixed indentation
        for char in s:  # Fixed indentation
            if '0' <= char <= '9':  
                if ans:
                    ans.pop()
            else:
                ans.append(char)
        return ''.join(ans)
