class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}   
        for i in nums:
            nums_count[i] = 1 + nums_count.get(i, 0)

        res = list(nums_count.keys())
        res.sort(reverse=True, key=lambda x: nums_count.get(x))
        return res[:k]