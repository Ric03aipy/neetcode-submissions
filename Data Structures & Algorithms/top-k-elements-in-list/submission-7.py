class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # index of bucket === frequency
        # index = 0 --> frequency 0
        # index = 1 --> frequency 1
        freq_buckets = [[] for _ in range(len(nums)+1)]

        # frequency dictionary - standard -
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for val, freq in count.items(): 
            freq_buckets[freq].append(val)

        # build the result
        res = []
        for i in range(len(nums), -1, -1):
            for v in freq_buckets[i]:
                res.append(v)
                if len(res) == k: return res
        return res