class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total_cost = 0 

        cost = min(cost1 + cost2 , costBoth)
        min_need = min(need1 , need2)

        total_cost = cost* min_need

        if need1 > min_need :
            cost = min(costBoth, cost1)
            total_cost = total_cost + (need1-min_need)*cost
        else:
            cost = min(costBoth , cost2)
            total_cost = total_cost + (need2-min_need)*cost
        

        return total_cost