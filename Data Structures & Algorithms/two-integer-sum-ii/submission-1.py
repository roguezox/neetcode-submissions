class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        for i in range(len(numbers)):
            cursum = numbers[left] + numbers[right]
            if cursum == target:
                return [left+1,right+1]
            elif left == right:
                break   
            elif cursum < target:
                left+=1
            elif cursum > target:
                right-=1