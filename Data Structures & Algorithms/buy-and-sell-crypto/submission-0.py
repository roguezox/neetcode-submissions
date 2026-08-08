class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1,p2 = 0,1
        maxprofit=0
        while p2<len(prices):
            if prices[p1]<prices[p2]:
                profit = prices[p2]-prices[p1]
                maxprofit= max(maxprofit,profit)
            else:
                p1=p2
            p2+=1
        return maxprofit
        

