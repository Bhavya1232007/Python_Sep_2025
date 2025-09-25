class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        r=[]
        n=len(nums)
        for i in nums:
            if(nums.count(i)>1):
                r.append(i)
                break
        for i in range(1,n+1):         
            if(i not in nums):
                r.append(i)
        return r
