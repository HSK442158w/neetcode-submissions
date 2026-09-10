class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nig=len(nums)
        pro=[1]*nig
        temp=1
        for i in range(nig):
            pro[i] *= temp
            temp*=nums[i]
        temp=1
        for i in range(nig-1,-1,-1):
            pro[i] *= temp
            temp*=nums[i]
        
        return pro

        