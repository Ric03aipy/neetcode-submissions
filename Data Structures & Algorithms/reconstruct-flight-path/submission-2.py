class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # L'ordine si può ottenere in 2 modi: algoritmo di sorting oppure heap
        # Visto che non mi serve avere tutto ordinato e subito, ma mi basta estrarre al volo, l'heap è più efficiente
        import heapq

        # Costruzione della lista di adiacenza
        from collections import defaultdict
        adj_list = defaultdict(list)
        for src, dst in tickets: heapq.heappush(adj_list[src], dst)

        itinerary = []

        def dfs(node:str) -> None: # Fa side-effect 
            # I primi nodi ad essere aggiunti devono essere i vicoli ciechi e i pecorsi che portano ad essi
            if not adj_list[node]: 
                itinerary.append(node)
                # print("appendo", node)
                return
            while adj_list[node]: 
                # Il figlio che estrae grazie al minheap è quello con valore lessicografico minore 
                # Estrarre dalla lista l'arco è necessario per non restare invischiato in cicli
                child = heapq.heappop(adj_list[node])
                dfs(child)
            itinerary.append(node)
            # print("appendo", node)

        dfs("JFK")
        return itinerary[::-1]