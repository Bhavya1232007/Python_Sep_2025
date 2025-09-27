class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        # Iterate from the rightmost digit of num
        for i in reversed(range(len(num))):
            # Add k to the current digit, and update k with the carry-over
            k, num[i] = divmod(num[i] + k, 10)
        
        # If there's still a carry-over in k, prepend its digits to num
        while k > 0:
            num = [k % 10] + num
            k //= 10
            
        return num
