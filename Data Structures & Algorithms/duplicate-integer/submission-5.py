class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nunnu=(list(set(nums)))
        balsdip1=len(nums)
        balsdip2=len(nunnu)
        return balsdip1!=balsdip2
        