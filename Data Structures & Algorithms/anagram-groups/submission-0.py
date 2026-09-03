from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        gg=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            gg[key].append(i)
        return list(gg.values())