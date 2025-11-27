class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        tot_sum = nums[0]

        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            tot_sum = max(tot_sum, cur_sum)

        return tot_sum