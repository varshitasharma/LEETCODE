class Solution:
    def union(self, a, b):
        self.uf[self.find(b)] = self.find(a)

    def find(self, a):
        while self.uf[a] != a:
            a = self.uf[a]
        return a
    
    def detectCycle(self, V):
        self.visited[V] = True
        for i in range(len(self.adjList[V])):
            nextV = self.adjList[V][i]
            if self.visited[nextV]:
                return (V, nextV)
            ret = self.detectCycle(nextV)
            if ret[0]:
                return ret
        return (None, None)
    
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.uf = [0] + [i + 1 for i in range(len(edges))]
        self.adjList = [[] for i in range(len(edges) + 1)]      # Adjancency List
        hasFather = [False] * (len(edges) + 1)                  # Whether a vertex has already got a parent
        criticalEdge = None

        for i, edge in enumerate(edges):
            w, v = edge[0], edge[1]
            self.adjList[w].append(v)
            if hasFather[v]:
                criticalEdge = (w, v)                           # If a vertex has more than one parent, record the last edge
            hasFather[v] = True
            if self.find(w) == self.find(v):                    # If a loop is found, record the edge that occurs last
                cycleEdge = (w, v)
            self.union(w, v)

        if not criticalEdge:                                    # Case 1
            return cycleEdge
        self.visited = [False] * (len(edges) + 1)
        (w, v) = self.detectCycle(criticalEdge[1])
        return (w, v) if w else criticalEdge                    # Case 2 and 3


# class DSU(object):
#     def __init__(self):
#         self.par = [i for i in range(1002)]
#         self.rnk = [0] * 1001

#     def find(self, x):
#         if self.par[x] != x:
#             self.par[x] = self.find(self.par[x])
#         return self.par[x]

#     def union(self, x, y):
#         xr, yr = self.find(x), self.find(y)
#         if xr == yr:
#             return False
#         elif self.rnk[xr] < self.rnk[yr]:
#             self.par[xr] = yr
#         elif self.rnk[xr] > self.rnk[yr]:
#             self.par[yr] = xr
#         else:
#             self.par[yr] = xr
#             self.rnk[xr] += 1
#         return True


# class Solution:
#     def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
#         dsu = DSU()
#         indegree = defaultdict(int)
#         sortedEdges=[]
#         for e1,e2 in edges:
#             indegree[e2]+=1
#         for e1, e2 in edges:
#             sortedEdges.append([e1,e2,indegree[e2]])
        
#         sortedEdges.sort(key = lambda x :x[2]  )
#         print(sortedEdges)
#         for edge in sortedEdges:
#             if not dsu.union(*(edge[:2])):
#                 return edge[:2]