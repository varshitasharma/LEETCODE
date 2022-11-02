class DSU(object):
    def __init__(self):
        self.par = [i for i in range(1002)]
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        indegree = defaultdict(int)
        sortedEdges=[]
        for e1,e2 in edges:
            indegree[e2]+=1
        for e1, e2 in edges:
            sortedEdges.append([e1,e2,indegree[e2]])
        
        sortedEdges.sort(key = lambda x :x[2]  )
        for edge in sortedEdges:
            if not dsu.union(*(edge[:2])):
                return edge[:2]