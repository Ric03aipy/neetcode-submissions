class TimeMap:

    def __init__(self):
        # INFO CRUCIALE: All the timestamps of set are strictly increasing.
        # --> idea: {key : (val, ts)}; se timestamp non crescenti forse un max/minheap (non so di che parlo)
        self.ds = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ds: self.ds[key] = []
        self.ds[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ds: return ""

        # stiamo cercando il timestamp più vicino -> segue pattern binary search on answer visto in Koko

        arr = self.ds[key]
        left, right = 0, len(arr) - 1
        last_candidate = None
        while left <= right: 
            mid = left + (right - left) // 2
            mid_val, mid_ts = arr[mid]
            
            if mid_ts <= timestamp: 
                last_candidate = mid_val
                left = mid + 1
            else: 
                right = mid - 1
        return last_candidate if last_candidate else ""