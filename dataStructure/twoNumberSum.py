#!/usr/bin/env python3

# Usage example: 
# Input: array = [3,4,-1,11,8] and targetSum=10 -> Output: [-1,11]

# Use a hash table for O(n) time /   O(n) space

def twoNumberSum(array, targetSum):
    # currentNum + Y = targetSum => Y = targetSum - currentNum -> Add numbers that we have in a dictionary as Y, if Y was there return it
    nums = {} 
    for num in array:
        potentialMatch = targetSum - num 
        if potentialMatch in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True

    return []
    










# Worst way to solve it (nested for loop)
# O(n^2) T , O(1)S:
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i+ 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []