class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price=1000
        max_profit=0
        nums=prices

        for num in nums:
            if num<min_price:
                min_price=num
            profit=num-min_price
            max_profit=max(profit,max_profit)
        return max_profit