class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numsi=set(nums)
        chunaidkhan=1##rizzon we take both as 1 iz bcuz it takes 2 vals compare
        for i in numsi:
            if i - 1 in numsi:
                continue
            
            dhoni=1
            j=i+1
            while j in numsi:
                dhoni += 1
                j += 1
            chunaidkhan=max(chunaidkhan,dhoni)
            
        return chunaidkhan

