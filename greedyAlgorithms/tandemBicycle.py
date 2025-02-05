# tandemSpeed =  max(speedA, speedB)
# Write a function that returns the max possible total speed or the min possible total speed of 
# all of the tandem bicycles being ridden on an input parameter, fastest. 
# 
# ex: if there are 4 riders (2 red-shirt riders, 2 blue-shirt riders) who have speeds of 1, 3, 4, 5 and 
# if they are paired on tandem as [1,4], [5,3] total speed is 9


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if fastest == True:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse = True)

    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse = True)

    totalSpeed = 0
    for idx, redRider in enumerate(redShirtSpeeds):
        speedDictator = max(redRider, blueShirtSpeeds[idx])
        totalSpeed += speedDictator
        
    return totalSpeed
