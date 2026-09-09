class Solution:
    def sortColors(self, nums: List[int]) -> None:
        camp=len(nums)
        for i in range(camp):
            for j in range(i+1,camp):
                if nums[i] > nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                

        