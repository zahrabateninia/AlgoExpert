# Given an array of positive integers representing the values of coins in your
# possession, write a function that returns the min amount of change( the min sum of money)
# that you cannot create. 

# example: coins = [1,2,5]
# output: 4 

def nonConstructibleChange(coins):
    coins.sort()  
    currentChangeCreated = 0
    
    for coin in coins:
        if coin > currentChangeCreated + 1:
            # If there's a gap, we cannot create `currentChangeCreated + 1`
            return currentChangeCreated + 1
        currentChangeCreated += coin  # Extend the range of change we can create
    
    # If all coins are used, return the next amount of change
    return currentChangeCreated + 1
