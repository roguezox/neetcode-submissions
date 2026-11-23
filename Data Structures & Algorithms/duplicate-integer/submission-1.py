class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seennums = set()
        for num in nums:
            if num in seennums:
                return True

            else :
                seennums.add(num)
        return False