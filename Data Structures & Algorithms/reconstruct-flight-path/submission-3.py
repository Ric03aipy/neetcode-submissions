class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        """
        questo non è un Ordinamento Topologico. 
        L'algoritmo che hai appena scritto si chiama Algoritmo di Hierholzer per i Cammini Euleriani.
        Anche se il codice sembra identico al Topological Sort (DFS post-order + inversione finale dell'array), gli obiettivi sono diametralmente opposti:
        Topological Sort: Visita tutti i nodi rispettando le dipendenze. Se c'è un ciclo, l'algoritmo fallisce (impossibile laurearsi).
        Hierholzer (Cammino Euleriano): Visita tutti gli archi (i biglietti) esattamente una volta. È progettato appositamente per gestire i cicli. Quando entri in un ciclo (es. JFK $\rightarrow$ Londra $\rightarrow$ Parigi $\rightarrow$ JFK), il heappop strappa via i biglietti consumati. Quando torni a JFK e non hai più voli, JFK diventa un "vicolo cieco" temporaneo, finisce nell'array finale, e la ricorsione si srotola all'indietro sbloccando il resto del viaggio.
        """

        # L'ordine si può ottenere in 2 modi: algoritmo di sorting oppure heap
        # Visto che non mi serve avere tutto ordinato e subito, ma mi basta estrarre al volo, l'heap è più efficiente
        import heapq

        # Costruzione della lista di adiacenza
        from collections import defaultdict
        adj_list = defaultdict(list)
        for src, dst in tickets: heapq.heappush(adj_list[src], dst)

        itinerary = []

        def dfs(node:str) -> None: # Fa side-effect 
            # Non serve alcun controllo di questo tipo
            # # I primi nodi ad essere aggiunti devono essere i vicoli ciechi e i pecorsi che portano ad essi
            # if not adj_list[node]: 
            #     itinerary.append(node)
            #     return
            while adj_list[node]: 
                # Il figlio che estrae grazie al minheap è quello con valore lessicografico minore 
                # Estrarre dalla lista l'arco è necessario per non restare invischiato in cicli
                child = heapq.heappop(adj_list[node])
                dfs(child)
            # Visita in post ordine del grafo SIMILE all'ordinamento topologico
            itinerary.append(node)

        dfs("JFK")
        # Inversione per costruzione SIMILE all'ordinamento topologico (DFS + inversione)
        return itinerary[::-1]