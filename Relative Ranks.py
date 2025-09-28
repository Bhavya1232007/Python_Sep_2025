class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=sorted(score,reverse=True)
        ranks=["Gold Medal","Silver Medal","Bronze Medal"]
        d={}
        r=[]
        if(len(score)>2):
            for i in range(0,3):
                d[s[i]]=ranks[i]
            for i in range(3,len(s)):
                d[s[i]]=str(i+1)
            for i in score:
                r.append(d[i])
        elif(len(score)==1):
            r=["Gold Medal"] 
        elif(len(score)==2):
            for i in range(0,len(s)):
                d[s[i]]=ranks[i]
            for i in score:
                r.append(d[i])           
        return r

        
