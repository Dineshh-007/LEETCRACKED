# Time complexity -----> O(n)

arr = [3, -4, 5, 4, -1, 7, -8]
n=len(arr)

maxSum=float('-inf')   
curSum=0

for i in range(n):
    curSum+=arr[i]
    maxSum=max(curSum,maxSum)
    if curSum<0:
        curSum=0

print(maxSum)

