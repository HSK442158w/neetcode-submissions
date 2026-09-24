class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        higa=n/3
        goya={}
        v=[]
        for i in nums:
            goya[i] = goya.get(i, 0) + 1
            
        for i in goya:
            if goya[i] > higa:
                v.append(i)
        return v
