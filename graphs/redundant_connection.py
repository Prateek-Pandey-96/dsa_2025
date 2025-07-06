from typing import List

class Dsu:
    def __init__(self, n):
        self.n = n
        self.rank = [0] * n
        self.par = [i for i in range(n)]

    def findParent(self, x):
        while self.par[x] != x:
            x = self.par[x]
        return x

    def doUnion(self, x, y):
        parx, pary = self.findParent(x), self.findParent(y)
        if parx == pary:
            return
        
        if self.rank[parx] > self.rank[pary]:
            self.par[pary] = parx
        elif self.rank[parx] < self.rank[pary]:
            self.par[parx] = pary
        else:
            self.par[parx] = pary
            self.rank[pary] += 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = Dsu(n)

        for u, v in edges:
            paru, parv = dsu.findParent(u-1), dsu.findParent(v-1)
            if paru != parv:
                dsu.doUnion(paru, parv)
            else:
                return [u, v]

        return []
