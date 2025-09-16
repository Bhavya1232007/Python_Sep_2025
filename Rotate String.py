class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        S=list(s)
        G=list(goal)
        l=[]
        for i in S:
            e=S.pop(0)
            S.append(e)
            if(S==G):
                return True
        return False
