class Twitter:

    # ================
    # ripetizione #1
    # ================

    from collections import defaultdict
    import heapq

    def __init__(self):
        self.following = defaultdict(set[int])
        self.tweets = defaultdict(list[tuple[int, int]]) 
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        heap = []

        # popolo l'heap - considero anche l'utente stesso per la ricerca dei feeds
        for idx, user_id in enumerate(self.following[userId] | {userId}): 
            if not self.tweets[user_id]: continue
            last_idx = len(self.tweets[user_id]) - 1
            time, tweet_id = self.tweets[user_id][last_idx]
            heap.append((-time, tweet_id, user_id, last_idx - 1)) 

        heapq.heapify(heap)

        while len(res) < 10 and heap: 
            time, tweet_id, user_id, nxt_idx = heapq.heappop(heap)
            res.append(tweet_id)
            if nxt_idx >= 0:
                time, tweet_id = self.tweets[user_id][nxt_idx]
                heapq.heappush(heap, (-time, tweet_id, user_id, nxt_idx - 1)) 

        return res       


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
