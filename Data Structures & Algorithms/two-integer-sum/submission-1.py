class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # target - i = i
        for i in range(len(nums)):
            if hashmap.get(nums[i]) == None:
                hashmap[target - nums[i]] = i
            else:
                return [hashmap[nums[i]],i] 
        
