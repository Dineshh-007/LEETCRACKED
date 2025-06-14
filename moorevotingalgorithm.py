#Two solutions available----->First one is otimized approach

#Intuition: The intuition behind this approach is that if an element occurs more than n/2 times in the array (where n is the size of the array), it will always occupy the middle position when the array is sorted. Therefore, we can sort the array and return the element at index n/2. 

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]

# class Solution:
#     def majorityElement(self, nums: List[int]):
#         freq=0
#         ans=0
#         for i in range(0,len(nums)):
#             if freq==0:
#                 ans=nums[i]
#                 freq=1
#             elif ans == nums[i]:
#                 freq+=1
#             else:
#                 freq-=1

#         return ans