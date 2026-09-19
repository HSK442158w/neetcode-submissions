class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        rr=len(nums)
        dhoni=1
        chunaidkhan=1##rizzon we take both as 1 iz bcuz it takes 2 vals compare
        for i in range(rr-1):
            diff=nums[i+1] - nums[i]
            if diff==1:
                dhoni+=1
                chunaidkhan=max(chunaidkhan,dhoni)
            elif diff==0:
                continue

            else:
                dhoni=1
        return chunaidkhan