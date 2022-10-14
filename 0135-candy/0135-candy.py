class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = n
        candy = [1]*n
        sortedRating = sorted([ (i,rate) for i,rate in enumerate(ratings)], key = lambda x: x[1] )
        # print(sortedRating)
        for i,rate in sortedRating:
            if i>0 and rate>ratings[i-1] and candy[i] <= candy[i-1]:
                # print(i, candy)
                candies += candy[i-1]+1-candy[i]
                candy[i] = candy[i-1]+1
            if i<n-1 and rate>ratings[i+1] and candy[i] <= candy[i+1]:
                # print(i,candy)
                candies += candy[i+1]+1-candy[i]
                candy[i] = candy[i+1]+1
                
        
        # print(candy)
        return candies
    