class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {course_id:[] for course_id in range(numCourses)}
        for l in prerequisites: 
            for i in range(len(l)): 
                if i + 1 < len(l): 
                    preMap[l[i]].append(l[i+1])
                # L'ultimo elemento di una lista, non avendo un successore non ha un prerequisito nella lista corrente
        
        visited = set()
        
        def dfs(node:int) -> bool: 
            if node in visited: return False # Ciclo 
            if preMap[node] == []: return True # Nessun prerequisito per il nodo corrente
            visited.add(node)
            for pre in preMap[node]: # copia perche cambia la sixe di un set
                if dfs(pre) == False: return False # Se un prerequisito non può essere soddisfatto non potrà neanche esserlo questo corso
            visited.remove(node)
            preMap[node] = set()
            return True

        # Dfs per ogni nodo: serve se non è un grafo completamente connesso
        for node in preMap.keys(): 
            if dfs(node) == False: return False
        return True

        
        