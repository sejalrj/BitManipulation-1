class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        two_numbers = nums[0]
        for n in nums[1:]:
            two_numbers ^= n
        
        #13^6
        diff = two_numbers & (-two_numbers)

        x = 0
        for num in nums:
            if num & diff:
                x^= num
        return [x, two_numbers^x]
