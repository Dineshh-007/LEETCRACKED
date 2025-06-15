#  Intuition
#
# The problem asks us to reverse a list of characters in-place.
# At first glance, using built-in methods like s.reverse() or slicing s[::-1] might seem easy, but the constraint is in-place modification with O(1) extra space.
#
# The natural and efficient solution is to use the two-pointer technique — swapping characters from both ends of the list moving toward the center.

#  Approach
# 	1.	Initialize two pointers:
# 	•	left = 0 → points to the first character.
# 	•	right = len(s) - 1 → points to the last character.
# 	2.	While left < right:
# 	•	Swap s[left] and s[right].
# 	•	Move left forward and right backward.
# 	3.	The loop stops when both pointers meet or cross. The list is now reversed in-place.


# 	•	Time Complexity:
# O(n) — We process each character once (half the array, but we ignore constants in Big-O).
# 	•	Space Complexity:
# O(1) — No extra space is used; all operations are done in-place with only two pointers.

class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        largest, secondLargest = -1, -1

        for i in range(n):
            if arr[i] > largest:
                secondLargest = largest
                largest = arr[i]

            elif arr[i] < largest and arr[i] > secondLargest:
                secondLargest = arr[i]

        return secondLargest