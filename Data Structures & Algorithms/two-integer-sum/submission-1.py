class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countnums = {}

        for i, n in enumerate(nums):
            nextt = target - n
            if nextt in countnums:
                return ([countnums[nextt], i])
            countnums[n] = i
        return

