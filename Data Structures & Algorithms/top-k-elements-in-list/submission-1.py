class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mahat=[]
        diddy={}
        for i in nums:
            diddy[i] = diddy.get(i, 0) + 1

        for i in range(k):
            temp=max(diddy,key=diddy.get)
            mahat.append(temp)
            del diddy[temp]
                    

        return mahat



