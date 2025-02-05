# tandemSpeed =  max(speedA, speedB)
# Write a function that returns the max possible total speed or the min possible total speed of 
# all of the tandem bicycles being ridden on an input parameter, fastest. 
# 
# ex: if there are 4 riders (2 red-shirt riders, 2 blue-shirt riders) who have speeds of 1, 3, 4, 5 and 
# if they are paired on tandem as [1,4], [5,3] total speed is 9

# O(n Log(n)) T | O(1) S 


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if fastest: 
        reverseArrayInPlace(redShirtSpeeds)


    totalSpeed = 0
    for idx, redRider in enumerate(redShirtSpeeds):
        speedDictator = max(redRider, blueShirtSpeeds[idx])
        totalSpeed += speedDictator
        
    return totalSpeed

def reverseArrayInPlace(arr):
     start = 0
     end = len(arr) - 1
     while start < end:
         arr[start], arr[end] = arr[end], arr[start]
         start +=1
         end -= 1