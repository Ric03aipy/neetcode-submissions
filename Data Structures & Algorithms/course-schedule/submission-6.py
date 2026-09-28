class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {course_id:[] for course_id in range(numCourses)}
        for l in prerequisites: 
            for i in range(len(l)): 
                if i + 1 < len(l): 
                    preMap[l[i]].append(l[i+1])
                # L'ultimo elemento di una lista, non avendo un successore non ha un prerequisito nella lista corrente
        
        # Elementi visitati
        visited = set()
        
        def dfs(node:int) -> bool: 

            # Ciclo 
            if node in visited: return False 

            # Nessun prerequisito per il nodo corrente
            if preMap[node] == []: return True 

            # Marco questo corso/nodo come visitato
            visited.add(node)

            # Ricorsione dfs per tutti i figli
            for pre in preMap[node]:
                # Se un prerequisito non può essere soddisfatto non potrà neanche il corso corrente
                if not dfs(pre): return False 
            
            visited.remove(node)
            preMap[node] = []
            return True

        # Dfs per ogni nodo: serve se non è un grafo completamente connesso - approccio stile Topological sort
        for node in preMap.keys(): 
            if dfs(node) == False: return False
        return True

        
        