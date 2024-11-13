# A subsequence of an array is a set of numbers that are not necessarily adjacent but are in the SAME ORDER as they appear in the array

# Use a  pointer for the potential subsequence array and another pointer for the main array and just go forward and check their values

def isValidSubsequence(array, sequence):
    arrIdx = 0 # main array pointer
    subIdx = 0 # sequence pointer
    while arrIdx < len(array) and subIdx < len(sequence):
        if array[arrIdx] == sequence[subIdx]:
            subIdx +=1 # move forward to the next number if you find a match
        arrIdx +=1
    return subIdx == len(sequence) # if the whole subsequence array numbers were matched, the length of this sequence is equal to the index of the last value of our pointer