#!/usr/bin/env python3

# Implement binary search: the list should be SORTED
# Whe our left pointer is greater than right pointer we know that the target was not found in our array

# Time Complexity: O(log(N)) why? bcs we are eliminating half of our array every time we traverse
# Space Complexity: O(1) why? we are not storing values somewhere else, we're using the array itself
# but if we implement it recursively, S would be O(log(N)) bcs of stack memory

def binarySearch(array, target):
    left = 0 # index of first element
    right = len(array) - 1 # index of the last element (round the num down)
    
    while(left <= right): # till the left index is smaller than the right one 
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif(target < array[mid]):  
            right = mid -1
        else:
            left = mid + 1
    return -1