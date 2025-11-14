class Solution:
    def search(self, nums: List[int], target: int) -> int:
        numMap = {}
        n = len(nums)

        for i in range(n):
            numMap[nums[i]] = i
        
        for i in range(n):
            if target in numMap:
                return numMap[target]
            else:
                return (-1)