class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0

        l,r = 0, 1

        while r<=len(prices)-1:
            profit = prices[r] -prices[l]
            result = max(result, profit)

            if prices[l] > prices [r]:
                l = r #almost got this on my own except this line 
                # we use l = r, instead of l = l+1, as we would like to have have the lowest
                # l possible, since that is the buying price and lowering the buying prices is 
                #better, since we are checking for prices[l] > prices[r], this means that 
                #in the future, we are getting an even cheaper price, thus it is better
                # for us to buy then, which is why we have to update l to r.
                r = r+1
            else:
                r = r+1
        
        return result
