from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        ud=sorted(d.items(),key=lambda x:-x[1])
        result=""
        for key,val in ud:
            result+=key*val
        return result
