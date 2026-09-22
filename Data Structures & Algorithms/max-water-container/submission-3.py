class Solution:
    def maxArea(self, h: List[int]) -> int:
        i=0
        j=len(h)-1
        area=0
        while i<j:
            mini=min(h[i],h[j])
            tutu=j-i
            area=max(mini*tutu,area)
            if h[i]<h[j]:
                i+=1
            else:
                j-=1
        return area