class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        pro=[1]*l
        temp=1
        for i in range(l):
            pro[i] *= temp
            temp*=nums[i]
        temp=1
        for i in range(l-1,-1,-1):
            pro[i] *= temp
            temp*=nums[i]
        
        return pro

        
