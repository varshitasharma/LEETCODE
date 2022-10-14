class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''TC: O(N) , SC: O(N)'''
        n =len(ratings)
        candies = [1]*n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]: candies[i] = candies[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1] and candies[i]<=candies[i+1]: candies[i] = candies[i+1]+1
        return sum(candies)
        
        
        '''TC: O(NlogN), SC: O(N)'''
        # n = len(ratings)
        # candies = n
        # candy = [1]*n
        # sortedRating = sorted([ (i,rate) for i,rate in enumerate(ratings)], key = lambda x: x[1] )
        # for i,rate in sortedRating:
        #     if i>0 and rate>ratings[i-1] and candy[i] <= candy[i-1]:
        #         candies += candy[i-1]+1-candy[i]
        #         candy[i] = candy[i-1]+1
        #     if i<n-1 and rate>ratings[i+1] and candy[i] <= candy[i+1]:
        #         candies += candy[i+1]+1-candy[i]
        #         candy[i] = candy[i+1]+1
        # return candies
    