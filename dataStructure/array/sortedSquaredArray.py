# given an array of integers sorted in ascending order (not-empty array) return the squared array which is also 
# in ascending order. Be careful about negative integers


# Brute force method : O(nlogn) Time / O(n) space
#  nlong is the best time complexity for the sort method using merge sort or heap sort..

def sortedSquaredArray(array):
    squaredArray = []
    for num in array:
        num *= num 
        squaredArray.append(num)
    # sort method sorts the array in place and returns None
    squaredArray.sort()
    return squaredArray

# Solve the question in linear time bcs the given array is sorted
# hint: largest negative value is on the left and the largest positive value is on the right
#   so we compare the most left value to the right left value (their absolute value)

