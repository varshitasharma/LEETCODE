```
output, adj = [[]], defaultdict(list)
for source, dest in edges: adj[source].append(dest)
def dfs(parent, child):
for dest in adj[child]:
if output[dest] and output[dest][-1] == parent: continue
output[dest].append(parent)
print(output)
dfs(parent, dest)
# print(indegree)
print(adj)
for node in range(n):
dfs(node, node)
return output
```