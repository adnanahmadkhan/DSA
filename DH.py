# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
## given N return smallest positive integer that whose individual digits sum to N

# def solution(N):
#     i = 1;
#     while (1):
#         # Checking if number has
#         # sum of digits = N
#         if (getSum(i) == N):
#             return i;
#             break;
         
#         i += 1;

# def getSum(n):
 
#     sum1 = 0;
#     while (n != 0):
#         sum1 = sum1 + n % 10;
#         n = n // 10;
     
#     return sum1;



# what is the length of the longest bi-valued slice (continuous fragment) in a given array a

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A):
#     # write your code in Python 3.6
#     lastSeen = -1
#     secondLastSeen = -1
#     lbs = 0
#     tempCount = 0
#     lastSeenNumberRepeatedCount = 0

#     for current in A:
#         if (current == lastSeen or current == secondLastSeen):
#             tempCount += 1
#         else:
#             # if the current number is not in our read list it means 
#             # new series has started, tempCounter value in this case will be
#             # how many times lastSeen number repeated before this new number 
#             # encountered + 1 for current number.
#             tempCount = lastSeenNumberRepeatedCount + 1

#         if (current == lastSeen):
#             lastSeenNumberRepeatedCount += 1
#         else:
#             lastSeenNumberRepeatedCount = 1

#             secondLastSeen = lastSeen
#             lastSeen = current

#         lbs = max(tempCount, lbs)
    
#     return lbs
