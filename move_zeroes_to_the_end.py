class Solution:
    def move_zeroes(self,arr):
        count = 0
        for i in range(len(arr)):

            if arr[i] != 0:
                arr[i] , arr[count] = arr[count] , arr[i]
                count += 1






array = [1,2,0,4,3,0,5,0]
sol = Solution()
sol.move_zeroes(array)
