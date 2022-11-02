class Solution:    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, output = len(isConnected), 0
        def countProvince(node):
            if node not in visited:
                visited.add(node)
                for adj,con in enumerate(isConnected[node]):
                    if con: countProvince(adj)
        visited = set()
        for i in range(n):
            if i not in visited:
                countProvince(i)
                output+=1
        return output

# class UnionFind:
#     def __init__(self, size):
#         self.root = [i for i in range(size)]
#         # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
#         # The initial "rank" of each vertex is 1, because each of them is
#         # a standalone vertex with no connection to other vertices.
#         self.rank = [1] * size

#     # The find function here is the same as that in the disjoint set with path compression.
#     def find(self, x):
#         if x == self.root[x]:
#             return x
#         self.root[x] = self.find(self.root[x])
#         return self.root[x]

#     # The union function with union by rank
#     def union(self, x, y):
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX != rootY:
#             if self.rank[rootX] > self.rank[rootY]:
#                 self.root[rootY] = rootX
#             elif self.rank[rootX] < self.rank[rootY]:
#                 self.root[rootX] = rootY
#             else:
#                 self.root[rootY] = rootX
#                 self.rank[rootX] += 1

# class Solution:    
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected)
#         uf = UnionFind(n)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if isConnected[i][j]: uf.union(i,j)
#         parents = set()
#         for i in range(n):
#             parents.add(uf.find(i))
#         return len(parents)