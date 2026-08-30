class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tt={}
        for i,v in enumerate(nums):
            cc=target-v
            if cc in tt:
                return [tt[cc], i]
            tt[v]=i
        return []
#basically ulta shi ,old data in dict and new arebeing serached