class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, n in enumerate(nums):
            diferença = target - n
            if diferença in result:
                return [result[diferença], i]
            result[n] = i    
        return []