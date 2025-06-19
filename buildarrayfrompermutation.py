class Solution:
    def buildArray(self, nums):
        # num_list = []
        n = len(nums)
        # for i in range(n):
        #     num_list.append(nums[nums[i]])
        # return num_list
        return [nums[nums[i]] for i in range(n)]