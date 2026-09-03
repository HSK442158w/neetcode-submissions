from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums) / 2
        for i in nums:
            if nums.count(i) >= n:
                jigga=i
        return jigga
        