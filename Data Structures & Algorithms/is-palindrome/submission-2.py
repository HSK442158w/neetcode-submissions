class Solution:
    def isPalindrome(self, s: str) -> bool:
        cbt=""
        
        for i in s:
            if i.isalnum():
                cbt+=i
        cbt=cbt.lower()
        return cbt==cbt[::-1]
