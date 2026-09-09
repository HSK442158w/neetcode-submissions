class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        camp=len(nums)
        for i in range(camp):
            for j in range(i+1,camp,1):
                if nums[i] > nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp

                

        return nums