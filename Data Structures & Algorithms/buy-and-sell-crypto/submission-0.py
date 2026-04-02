class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=100
        max_profit=0


        for num in prices:
            if num<min_price:
                min_price=num

            profit=num-min_price
            if max_profit<profit:
                max_profit=profit
            
        return max_profit
        
        