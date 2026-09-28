class Twitter:

    """
    You should aim for a solution with O(nlogn) time for each getNewsFeed() function call, O(1) time for the remaining      
    methods, and O((N * m) + (N * M) + n) space, where n is the number of followeeIds associated with the userId, m is the 
    maximum number of tweets by any user, N is the total number of userIds, and M is the maximum number of followees for any 
    user.
    """

    from collections import defaultdict

    def __init__(self):
        # Uso set invece di list perché gli ID sono unici e le operazioni di follow/unfollow devono essere O(1)
        # Con list sarebbero O(n)
        self.followers = defaultdict(set) # {userId: set[userId]} per tracciare chi segue chi: "chiave segue valori"
        self.posts = defaultdict(list)     # {userId: list[time, postId]} per tracciare i post di ogni utente
        # Entrambe le precedenti strutture dati costano O(n*m) in spazio - mi manca quel O(n) in  O((N * m) + (N * M) + n)

        # Creo una variabile di supporto per la costruzione della coda di priorità: la priorità è il tempo di inserimento,
        # più è grande più è recente, quindi prioritario. 
        self.global_time = 0 

        self.heaps = defaultdict(list) # {usedId: [top 10 most recent post]} - inutilizzabile della fuznione post

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.global_time, tweetId])
        self.global_time += 1
        # Il fatto che la funzione post debba essere O(1) in tempo significa che non posso mantenere un Heap per ogni utente
        # Perché l'inserimento dei del post obbligherebbe il mantenimento della struttura con un "sift down" di costo O(logn)
        # Però una tale struttura matcherebbe il costo O(n) essendo O(10) quindi costante * n utenti in spazio
        # Quindi tutta la logica dell'Heap va in getNewsFeed



    def getNewsFeed(self, userId: int) -> List[int]:

        # print("Chiamata per", userId)
        # print("Situazione attuale")
        # print("follower:", self.followers)
        # print("post:", self.posts)

        followed = self.followers[userId]
        followed.add(userId) # includo se stesso nella ricerca - ma non nei followers globali quindi rispetto il vincolo
        # soluzone banale:
        # estraggo fino a 10 elementi più recenti per ogni utente - O(10n) space & time
        # ordino per tempo - O(10nlog10n) time
        # prendo i 10 finali - O(10) space
        # non è ottimo ma asintoticamente non è sbagliato rispetto alla richiesta credo - ma è super semplice logicamente
        
        candidates = []
        for user in followed: candidates.extend(self.posts[user][-10:])
        # anche se non ci sono 10 elementi lo slicing semplicemente restituisce tutto
        candidates.sort(key=lambda x: -x[0]) # ordine discendente
        # print(candidates)
        feeds = [post for _, post in candidates[:10]] # i primi 10 più recenti
        return feeds
        

    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId) # discard invece di remove non solleva eccezione
