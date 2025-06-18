import math

class Solution:
    def findNumbers(self, nums):
        # main_count = 0
        # for element in nums:
        #     count = 0
        #     while element > 0:
        #         element = element % 10
        #         count = count + 1
        #         element = element // 10
        #     if count % 2 == 0:
        #         main_count +=1

        # return main_count
        # count = 0
        # for num in  nums:
        #     if(len(str(num))%2 == 0):
        #         count+=1
        # return count

        # return sum(1 for num in nums if len(str(num)) % 2 == 0)


        return sum(1 for num in nums if (math.log10(num)+1 % 2) == 0)

        # here except string method all methods are best one.....


nums = [12,345,2,6,7996]
sol = Solution()
ans = sol.findNumbers(nums)
print(ans)
