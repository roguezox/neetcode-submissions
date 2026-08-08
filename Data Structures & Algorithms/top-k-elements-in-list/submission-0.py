class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n,0)
        ans = []
        for i in range(k):
            max_key = max(counts, key=counts.get)
            ans.append(max_key)
            del counts[max_key]
        return ans