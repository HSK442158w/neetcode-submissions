class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        bhaiyobheno=[]
        kk=len(nums)
        nums.sort()#-4,-1,-1,0,1,2

        for i in range(kk):
            j = i + 1
            k = kk - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    bhaiyobheno.append([nums[i],nums[k],nums[j]])
                    j += 1
                    while (j < k) and nums[j] == nums[j - 1]:
                        j += 1
                
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    while (j < k) and nums[k] == nums[k + 1]:
                        k -= 1
                
                else:
                    j += 1
                    while (j < k) and nums[j] == nums[j - 1]:
                        j += 1

        return bhaiyobheno