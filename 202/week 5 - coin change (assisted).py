# implement an algorithm to compute the minimum number of coins to make up a given change, assuming the supply of coins for each denomination are unlimited

# with denomination [1, 3, 4] cents, what is the minimum number of coins to make up 30 cents?
# an example with only 3 denominations: 1-cent, 3-cents and 4-cents
# suppose there is unlimited supply for each denomination
# what is the minimum number of coins to make up 30 cents
# is it 7 4-cents + 2 1-cent => min is 9 coins.

denom = [1, 3, 4]
m = len(denom)
n = 30

min_coin = [float('inf')] * (n + 1) #initialises an empty array for results of 
min_coin[0] = 0

# TODO: implement the DP formula in iterative format
def coin_change_unlimited_iter(n):
    max_value_coin = -1
    minimum_coin_count = -1
    remainder = -1
    if (min_coin[n-1]):
        ??
    
    for coin_pointer in range(-1,denom):
        next_coin_value = denom[coin_pointer+1]
        if next_coin_value <= n:
            max_value_coin = next_Coin_value
        else:
            break
            
    while (minimum_coin_count != 0 or):
        remainder = n % max_value_coin 

        if (remainder != 0):
            
            
        else:
            minimum_coin_count = n // max_value_coin
            
        
    

for e in enumerate(min_coin):
    print(e)

#tera notes: tried to fit a greedy algo into a DP question, remember to stick to the recurrence relation.
