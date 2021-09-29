
## array with sum = 0

# def solution(N):
#     # write your code in Python 3.6

#     if N==1:
#         return [0]
#     elif N%2==0:
#         array=[0]*N
#         num=1
#         for i in range(int(N/2)):
#             array[i]=-num
#             num+=1
#         num=1
#         for i in range(int(N/2),N):
#             array[i]=num
#             num+=1
#         return array
#     else:
#         array=[0]*N
#         num=1
#         for i in range(int(N/2)):
#             array[i]=-num
#             num+=1
#         num=1
#         for i in range(int(N/2)+1,N):
#             array[i]=num
#             num+=1
#         return array
          


# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")

# string transformation

# def solution(S):
#     # write your code in Python 3.6
#     while(True):
#         transformations = 0
#         S1 = S.replace("AB", "")
#         if(S1 != S):
#             transformations +=1
#         S2 = S1.replace("BA", "")
#         if(S2 != S1):
#             transformations +=1
#         S3 = S2.replace("CD", "")
#         if(S3 != S2):
#             transformations +=1
#         S4 = S3.replace("DC", "")
#         if(S4 != S3):
#             transformations +=1
#         if(transformations == 0):
#             break
#         transformations = 0
#         S = S4
#     return S




















# import random
# def solution(length):
#     letters = ['AB', 'BA', 'CD', 'DC']
#     s = ''.join(random.choice(letters) for i in range(length))
#     text_file = open("chars.txt", "w")
#     n = text_file.write(s)
#     text_file.close()



# solution(2500)


















# # N Counters

# def solution(N, A):
#     # write your code in Python 3.6
#     counters = [0] * N
#     n = len(A)
#     max_val = 0
#     for i in range(n):
#         if A[i] > N:
#             counters = [0] * N
#         else:
#             if (counters[A[i] - 1] < set_val):
#                 counters[A[i] - 1] = set_val
#             counters[A[i]-1] += 1
#             max_val = max(counters[A[i]-1], max_val)
    
#     for i in range(N):
#         counters[i] += max_val
#     return counters

# print(solution(5, [3,4,4,6,1,4,4]))





# frog river one
# earliest when frog can jump
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(X, A):
#     # write your code in Python 3.6
#     count = [0] * X
#     n = len(A)
#     l = X
#     for i in range(n):
#         if(count[A[i]-1] != 1):
#             l-=1
#             count[A[i]-1] = 1
#         if(l == 0):
#             return i
#     return -1   




# Tape equilibrium

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A):
#     # write your code in Python 3.6
#     sum_A = sum(A)
#     len_A = len(A)
#     curr = A[0]
#     results = []

#     if(len_A==2):
#         return abs(A[0]-A[1])
    
#     for i in range(1, len_A):
#         val = abs(curr-(sum_A-curr))
#         results.append(val)
#         curr+=A[i]
#     return min(results)





# #missing element


# def solution(A):
#     # write your code in Python 3.6
#     if((len(A)==1)):
#         return 2
#     A.sort()
#     for i in range(len(A)-1):
#         if(A[i+1] == A[i]+1):
#             continue
#         else:
#             return A[i]+1






















# # frog jump
# import math
# def solution(X, Y, D):
#     # write your code in Python 3.6
#     if(X == Y):
#         return 0
#     return math.ceil((Y-X)/D)























# odd occurences in array

# def solution(A):
#     # write your code in Python 3.6
#     if(len(A) == 1):
#         return A[0]
#     pairs = {}

#     for i in A:
#         if i not in pairs:
#             pairs[i] = 1
#         else:
#             pairs[i] += 1
    
#     for i in pairs.keys():
#         if((pairs[i]%2) == 1):
#             return i
















# cyclic rotation

# def solution(A, K):
#     # write your code in Python 3.6
#     pass
#     # very simple forgot to add the code here :(





















# binary gap


# def solution(N):
#     b_N = bin(N)[2:]
#     tmp = []
#     idx_of_1 = [index for index, value in enumerate(b_N) if value == '1']

#     if(len(idx_of_1) == 1):
#         return 0

#     for i in range(len(idx_of_1)-1):
#         tmp.append(idx_of_1[i+1]-idx_of_1[i]-1)
#     return max(tmp)

# print(solution(1041))





















# missing element
# def solution(A):
#      A.sort()
#      if (A[0] > 1): 
#         return 1
#      if (A[-1] < 1):
#         return 1

#      for i in range(len(A)-1):
#         if (A[i] < 1 and A[i+1] > 1):
#             return 1
#         if((A[i+1] == A[i]+1) or (A[i+1] == A[i]) or (A[i] < 1)):
#             continue
#         if(A[i+1] > A[i]+1):
#             return A[i]+1
#      return A[-1]+1
