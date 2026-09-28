class Solution:
    
    # Alternativa con sorting invece di heapq

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        from collections import defaultdict
        adj_list = defaultdict(list)
        for src, dst in tickets: adj_list[src].append(dst)
        # Davanti quelli più grandi così posso estrarre il più piccolo in O(1) anche con la lista con pop() !
        for src in adj_list: adj_list[src].sort(reverse=True) 

        itinerary = []

        # Algoritmo di Hierholzer
        def dfsHierholzer(node):
            while adj_list[node]: 
                child = adj_list[node].pop()
                dfsHierholzer(child)
            itinerary.append(node)

        dfsHierholzer("JFK")
        return itinerary[::-1]
