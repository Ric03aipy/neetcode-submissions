class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree = Graph con N-1 edges e no loop & unica componente connesse

        # lista di adiacenza
        adj_list = {i:[] for i in range(n)}
        for u,v in edges: 
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        def dfs(node, prev) -> bool: 
            visited.add(node)
            res = True
            for child in adj_list[node]: 
                if child == prev: continue
                if child in visited: return False
                res = res and dfs(child, node)
            return res
            
        return dfs(0, None) and len(visited) == n
        

        
