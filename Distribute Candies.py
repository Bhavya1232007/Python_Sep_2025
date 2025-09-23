class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        if(len(set(candyType))>n/2):
            return n//2
        else:
            return len(set(candyType))
