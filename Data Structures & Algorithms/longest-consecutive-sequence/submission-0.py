class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = defaultdict(set)
        start = 0
        longest = 0
        for i in range(len(nums)):
            num[nums[i]].add(nums[i])
        for i in range(len(nums)):
            if nums[i]-1 not in num:
                start = nums[i]
                length = 1
                while (start + length) in num:
                    length+=1
                longest = max(length, longest)
        return longest