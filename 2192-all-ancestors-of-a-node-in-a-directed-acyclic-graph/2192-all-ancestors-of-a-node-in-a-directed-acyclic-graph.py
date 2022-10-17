class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        '''O(N^2)'''
        output, adj, indegree = [set() for _ in range(n)], defaultdict(list), [0]*n
        for source, dest in edges: 
            adj[source].append(dest)
            output[dest].add(source)
            indegree[dest]+=1
            
        q = deque( [u for u,degree in enumerate(indegree) if degree==0])
        while(q):
            parent = q.popleft()
            for kid in adj[parent]:
                output[kid].update(output[parent])
                indegree[kid]-=1
                if indegree[kid] == 0: q.append(kid)
        return [sorted(a) for a in output]
                
                
                
        '''O(N^2)'''
        # output, adj = [[] for _ in range(n)], defaultdict(list)
        # for source, dest in edges: adj[source].append(dest)
        # def dfs(parent, child): 
        #     for dest in adj[child]:
        #         if output[dest] and output[dest][-1] == parent: continue
        #         output[dest].append(parent)
        #         dfs(parent, dest)
        # for node in range(n):
        #     dfs(node, node)
        # return output