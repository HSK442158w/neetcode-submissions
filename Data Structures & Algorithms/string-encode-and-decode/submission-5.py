class Solution:

    def encode(self, strs: List[str]) -> str:
        coin=""
        for i in strs:
            coin+=str(len(i))+"#"+i##########using  length and special char as prefix
        return coin

    def decode(self, s: str) -> List[str]:
        gengar=[] #........"""2#ji4#nigs11#ninahuunkay3#dik"""
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j=j+1
                laaluprasad=int(s[i:j])
            gengar.append(s[j+1:j+1+laaluprasad])
            i=j+1+laaluprasad

        return gengar
