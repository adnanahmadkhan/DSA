def minWindow(s: str, t: str) -> str:
    table = {}
    localMaxima = ""
    globalMaxima = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    
    for idx,val in enumerate(t):
        if val not in table:
            table[val] = -1
        else:
            table[val] -= 1

    start = 0
    for end in range(len(s)):
        if(s[end] in table):
            table[s[end]] += 1
            if(allFound(table)):
                # retract the sliding window
                while(s[start] not in table or table[s[start]]>=0):
                    if(s[start] in table):
                        if (table[s[start]] == 0):
                            break
                        table[s[start]] -= 1
                    start+=1

                # update local/global maxima
                localMaxima = s[start:end+1]
                globalMaxima = localMaxima if len(localMaxima)<len(globalMaxima) else globalMaxima
                    
    return globalMaxima
        
            
def allFound(table):
    for (k,v) in table.items():
        if(v<0):
            return False
    return True
        
            

# print(minWindow("ADOBECODEBANC","ABC"))


def isAlienSorted( words: list[str], order: str) -> bool:
    if(len(words)==1):
        return True
    
    for i in range(len(words)-1):
        first = words[i]
        second = words[i+1]

        if(not lexiCorrect(first,second,order)):
            return False
        
    return True


def lexiCorrect( first, second, order):
    table = {}
    for idx,val in enumerate(order):
        table[val] = idx

    l_s = len(second)
    for i in range(len(first)):
        if(i<l_s):
            if(table[first[i]]>table[second[i]]):
                return False
            elif(table[first[i]]<table[second[i]]):
                return True

    if(len(second)<len(first)):
        return False
    return True

# print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))


def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    last = len(nums)-1
    target = 0
    results = []
    table = {}
    print(nums)
    
    for first in range(len(nums)-2):
        second=first+1
        while(second<last):
            current_value = nums[first]+nums[second]+nums[last]
            if(current_value>target):
                last-=1
            elif(current_value<target):
                second+=1
            else:
                if(f"{nums[first]} {nums[second]} {nums[last]}" not in table):
                    results.append([nums[first], nums[second], nums[last]])
                    table[f"{nums[first]} {nums[second]} {nums[last]}"] = True
                second+=1
    return results                    

# print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))


# Given an array of integers, we would like to determine whether the array is monotonic (non-decreasing/non-increasing) or not.

def monotonic(array):
    trend = getTrend(array)



def getTrend(array):
    pass


# Given an array with 'empty' spots, fill those empty spots with the preceding number.

# Example

# input array = [8, None, 3]
# output array: [8, 8, 3]

def spots(array):
    currNum = getCurrentNumber(array)
    if(currNum is None):
        return array
    
    for i in range(len(array)):
        if array[i] == None:
            array[i] = currNum
        else:
            currNum = array[i]
    return array

def getCurrentNumber(array):
    if(len(array)==0):
        return None
    c = array[0]
    if c is None:
        for i in range(len(array)-1, 0, -1):
            if array[i] is not None:
                return array[i]
    return c
    
print(spots([None]))



