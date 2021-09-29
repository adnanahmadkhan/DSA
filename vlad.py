# Please write a function that accepts a list of integers and returns an integer.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the 
# future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0

def solution(A):

    maxval = 0
    lenA = len(A)
    for i in range(lenA):
        for j in range(lenA, i):
            if(A[i]<A[j]):
                profit = A[j] - A[i]
                maxval = max(profit, maxval)
    return maxval