class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seennums = {}
        
        for i, num in enumerate(nums):
            internaltarget = target - num
            if internaltarget in seennums:
                return [seennums[internaltarget], i]
            seennums[num] = i