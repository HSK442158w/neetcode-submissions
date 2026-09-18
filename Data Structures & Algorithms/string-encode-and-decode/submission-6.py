class Solution:

    def encode(self, strs:List[str]) -> str:
        jinja=""
        for i in strs:
            ko=str(len(i))
            jinja+=ko + "#" + i
        return jinja

    def decode(self, s:str) -> List[str]:
        gron=[] #.............2#ji4#nigg11#ninammunkay3#dik
        i=0
        while i < len(s):
            j=i
            while s[j]!="#":
                j+=1
                laser = int(s[i:j])
            gron.append(s[j + 1:j + 1 + laser])
            i=j+1+laser

        return gron