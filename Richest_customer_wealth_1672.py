class Solution:
    def maximumWealth(self, accounts):
        count = float('-inf')
        for account in accounts:
            sums = 0
            for value in account:
                sums += value
            if count < sums:
                count = sums
        return count