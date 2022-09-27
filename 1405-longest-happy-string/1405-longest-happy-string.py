class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        cntA, cntB, cntC = 0, 0, 0 # used to count the occurrences of corresponding character 
        
        for i in range(a+b+c):
            maxCount = max(a, b, c)
            if (a == maxCount and cntA < 2) or (cntB == 2 and a >= 1) or (cntC == 2 and a >= 1):
                res.append('a')
                a = a-1
                cntA = cntA+1
                cntB, cntC = 0, 0
            elif (b == maxCount and cntB < 2) or (cntA == 2 and b >= 1) or (cntC == 2 and b >= 1):
                res.append('b')
                b = b-1
                cntB = cntB+1
                cntA, cntC = 0, 0
            elif (c == maxCount and cntC < 2) or (cntA == 2 and c >= 1) or (cntB == 2 and c >= 1):
                res.append('c')
                c = c-1
                cntC = cntC+1
                cntA, cntB = 0, 0
        # end loop

        return "".join(res)
        
        
#         max_heap = []
#         if a != 0:
#             heappush(max_heap, (-a, 'a'))
#         if b != 0:
#             heappush(max_heap, (-b, 'b'))
#         if c != 0:
#             heappush(max_heap, (-c, 'c'))
#         s = []
#         while max_heap:
#             first, char1 = heappop(max_heap) # char with most rest numbers
#             if len(s) >= 2 and s[-1] == s[-2] == char1: # check whether this char is the same with previous two
#                 if not max_heap: # if there is no other choice, just return
#                     return ''.join(s)
#                 second, char2 = heappop(max_heap) # char with second most rest numbers
#                 s.append(char2)
#                 second += 1 # count minus one, because the second here is negative, thus add 1
#                 if second != 0: # only if there is rest number count, add it back to heap
#                     heappush(max_heap, (second, char2))
#                 heappush(max_heap, (first, char1)) # also need to put this part back to heap
#                 continue
			
# 			#  situation that this char can be directly added to answer
#             s.append(char1)
#             first += 1
#             if first != 0:
#                 heappush(max_heap, (first, char1))
#         return ''.join(s)