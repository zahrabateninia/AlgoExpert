# given an array of integers sorted in ascending order (not-empty array) return the squared array which is also 
# in ascending order. Be careful about negative integers


# Brute force method : O(nLogn) Time / O(n) space

#  nLong is the best time complexity for the sort method using merge sort or heap sort..

def sortedSquaredArray(array):
    squaredArray = []
    for num in array:
        num *= num 
        squaredArray.append(num)
    # sort method sorts the array in place and returns None
    squaredArray.sort()
    return squaredArray


# more professional code :) 
def sortedSquaredArray(array):
    sortedSquaredArray = [0 for _ in array] # create a list the same length as array and filled with zeros!
    # _ is a common convention for variables that are only needed to iterate but not used ---coool
    for idx in range(len(array)):
        value = array[idx]
        sortedSquaredArray[idx] = value * value

    sortedSquaredArray.sort()
    return sortedSquaredArray







# Two Pointer solution O(n) time and O(n) space

# Solve the question in linear time bcs the given array is sorted
# hint: largest negative value is on the left and the largest positive value is on the right
#   so we compare the most left value to the right left value (their absolute value)
#   the output array will be filled form right to left and it's sorted for sure

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))): # only one iteration through the list so O(n) time 
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1
    return sortedSquares

