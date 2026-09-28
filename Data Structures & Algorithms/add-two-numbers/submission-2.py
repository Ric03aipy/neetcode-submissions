# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Osservazioni
        # - le due liste potrebbero avere lunghezza differente quindi ci sarà una prima fase parallela e poi un "attacco quella che non è finita"
        # - la noia la da il riporto -> se faccio divmod per 10 e la divisione è != 0 allora registro il modulo e mi porto dietro il riporto; il riporto è sempre 1 (se non è 0)
        # - il riporto deve esistere anche quando "attacco" il pezzo rimanente (se è tipo 9->9->9) si deve propagare in 0->0->0->1 
        # - all'ultimo se c'è un "leading zero" (leading leggendo da destra, che è l'inizio) vuol dire che c'è stato un riporto finale, allora devo creare un nuovo nodo - è l'unico caso di creazione di un nodo nuovo
        # - viene richiesto O(1) in space, quindi non posso creare una lista nuova, ma devo sommare una lista all'altra
        # - non so quale lista è più corta, quindi potrei prevenitvamente calcolare la lunghezza di entrambe e risolvere poi stabilendo a priori che l1 è più corta (come? swappando le liste) -> la comodità costa n+m, una passata lineare per entrambe
        # - l'ultimo punto si può eviare facendo il doppio controllo su chi ha ancora elementi validi
        
        # - scelgo arbitrariamente che il mio contenitore da modificare e ritornare sarà l1 (in codice verò però forse preferirei non fare side effect, ma allocare spazio extra - anche se dipende dal caso d'uso)

        # dry run o distinzione di casi: 
        # Uguale misura: 
        # [] -> [] -> [] -> / 
        # [] -> [] -> [] -> / 
        # facile perché finiscono insieme, bisogna solo evenutualmente creare il nodo nuovo per il riporto

        # L1 più lunga: 
        # [] -> [] -> [] -> [] -> [] -> / 
        # [] -> [] -> [] -> / 
        # resta da aggiungere e propopagare il riporto

        # L2 più lunga:
        # [] -> [] -> [] -> / 
        # [] -> [] -> [] -> [] -> [] /
        # questo è il caso più complicato perché bisogna ricordare il riporto, attaccare la lista che manca, aggiungere il riporto e propagarlo -> mi serve ricordare chi è l'ultimo nodo valido di l1 

        # Casi strani da capire: singoletti e liste vuote (11->caso uguale misura, 10, 01, 00)

        # i dummy mi servono probabilmente per coprire i casi vuoti - da esaminare meglio
        dummy1 = ListNode(next=l1)
        curr1 = dummy1
        prev1 = None
        dummy2 = ListNode(next=l2)
        curr2 = dummy2
        carry = 0

        while curr1 and curr2: 
            s = curr1.val + curr2.val + carry
            new_carry, reminder = divmod(s, 10) 

            curr1.val = reminder
            carry = new_carry

            prev1 = curr1
            curr1 = curr1.next
            curr2 = curr2.next

        # if not curr1 and not curr2: print("Entrambe finite")

        # l2 non finita
        if curr2: 
            # print("Curr2 non è finita")
            # print(f"il valore che riceve un nuovo puntatore è {prev1.val}")
            prev1.next = curr2
            curr1 = prev1.next # ora posso continuare a leggere curr1
        


        # che abbia attaccato l2 o che l1 fosse già più lunga di l2 devo propagare il riporto se c'è
        # print("while curr1:")
        while curr1: 
            prev1 = curr1
            # print(f"valore correntemente esplorato = {curr1.val}")
            s = curr1.val + carry
            # print(" ", s)
            new_carry, reminder = divmod(s, 10) 
            curr1.val = reminder
            carry = new_carry 
        
            curr1 = curr1.next # il riporto mi serve a partire dal primo elemento nuovo
            
        # print("fine while curr1")
        
        # if not prev1: print(f"qui prev è none, carry={carry}")
        # attacco l'ultimo nodo
        curr1 = prev1

        if carry != 0 and curr1: 
            curr1.next = ListNode(1, None)
        
        return l1



        