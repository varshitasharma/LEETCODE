class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        output, adj = [[] for _ in range(n)], defaultdict(list)
        for source, dest in edges: adj[source].append(dest)
        def dfs(parent, child): 
            for dest in adj[child]:
                if output[dest] and output[dest][-1] == parent: continue
                output[dest].append(parent)
                dfs(parent, dest)
        for node in range(n):
            dfs(node, node)
        return output
        