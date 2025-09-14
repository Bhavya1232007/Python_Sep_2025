from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        ud=sorted(d.items(),key=lambda x:(x[1],-x[0]))
        result=[]
        for key,val in ud:
            for i in range(val):
                result.append(key)
        return result
