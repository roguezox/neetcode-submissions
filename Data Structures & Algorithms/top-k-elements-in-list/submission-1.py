class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            counts[n] = 1 + counts.get(n,0)
        ans = []
        for key, value in counts.items():
            freq[value].append(key)
        for i in range(len(nums),0,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans