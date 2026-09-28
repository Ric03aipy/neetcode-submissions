class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # ==============
        # ripetizione #2
        # ==============

        # il problema della ricerca si sposta dagli elementi dell'array al taglio sull'array
        n, m = len(nums1), len(nums2)
        if n > m: return self.findMedianSortedArrays(nums2, nums1)

        # qui sono sicuro che nums1 sia la più corta 

        # perché voglio cercare sulla più corta? Per una questione di validità! non potrei acceddere a valori che sforano la lista più corta 
        left, right = 0, n
        half = (m + n + 1) // 2
        while left <= right: 
            # indice di divisione
            mid = left + (right - left) // 2
        
            # grandezze attorno al divisore
            l1 = nums1[mid-1] if mid > 0 else -float("inf")
            r1 = nums1[mid] if mid < n else float("inf")
            l2 = nums2[half-mid-1] if half-mid > 0 else -float("inf")
            r2 = nums2[half-mid] if half-mid < m else float("inf")

            # calcolo della mediana
            if l1 <= r2 and l2 <= r1: 
                if (m + n) % 2 == 0: 
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return float(max(l1,l2))

            if l1 > r2: right = mid - 1
            else: left = mid + 1
        
