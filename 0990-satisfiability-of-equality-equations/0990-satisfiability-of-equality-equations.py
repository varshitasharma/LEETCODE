class Solution:
    def union(self, x, y):
        self.root[self.find(y)] =self.find(x)
    
    def find(self, x):
        while(self.root[x] != x):
            x = self.root[x]
        return x
    
    def equationsPossible(self, equations: List[str]) -> bool:
        self.root = { ch : ch for ch in [chr(i) for i in range(ord('a'),ord('z')+1)]}
        for e in equations:
            if e[1] == "=" :  self.union(e[0], e[3])
        # print(self.root)
        for e in equations:
            # print(self.union(e[0], e[3]))
            if e[1]=='!' and self.find(e[0]) == self.find(e[3]): return False
        return True
                