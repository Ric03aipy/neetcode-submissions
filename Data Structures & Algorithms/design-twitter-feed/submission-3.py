class Twitter:
    
    # La soluzione 1 non usa l'Heap: è una soluzione valida e fuznionale ma non scala per n gigante (non nei test)
    # Questa è la vera solzuione ottima standard

    from collections import defaultdict
    import heapq 

    def __init__(self):

        self.followers = defaultdict(set) # {userId: set[userId]} per tracciare chi segue chi: "chiave segue valori"
        self.posts = defaultdict(list)     # {userId: list[time, postId]} per tracciare i post di ogni utente

        self.global_time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.global_time, tweetId])
        self.global_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        followed = self.followers[userId]
        followed.add(userId) # includo se stesso nella ricerca - ma non nei followers globali quindi rispetto il vincolo

        # MaxHeap degli ulitmi post per ogni utente seguito - al più n -> O(n) mancante della richieta
        heap = [] 
        for user in followed: 
            if self.posts[user]: 
                # Aggiungo l'ultimo 
                idx = len(self.posts[user]) -1
                time, last_post = self.posts[user][idx] # [time, postId]
                # Aggiungo anche l'indice e l'utente che ha postato
                # come informazione ausiliaria per poter scalare indietro in caso serve
                heapq.heappush(heap, (-time, last_post, user, idx))
        
        feeds = [] 
        # Estraggo finché feeds non ha 10 elementi o non ci sono più post disponibili
        while heap and len(feeds) < 10: 
            time, post, user, idx = heapq.heappop(heap)
            feeds.append(post)
            if idx > 0: # significa che esiste un post precedente (un penultimo o un terzultimo e così via)
                # Reperisco il post
                prev_time, prev_post = self.posts[user][idx - 1]
                # Inserisco nell'heap
                heapq.heappush(heap, (-prev_time, prev_post, user, idx - 1))

        return feeds
                

        

    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId) # discard invece di remove non solleva eccezione
