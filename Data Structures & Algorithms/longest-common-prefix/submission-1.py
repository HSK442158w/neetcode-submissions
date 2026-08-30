class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        prefix=strs[0]#assume first word as the smolest or the starting shi tht matches
        for w in strs[1:]:#skip firstone 
            while not w.startswith(prefix):#checking shi if it there in other word
                prefix=prefix[:-1]#shorten it from last by 1
            if prefix=="":
                return ""
        return prefix
         
        

        

        
        