class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree, output = defaultdict(int), []
        for source, dest in edges:
            indegree[dest]+=1
        for node in range(n):
            if node not in indegree.keys(): output.append(node)
        return output