# implement an algorithm to compute the minimum number of coins to make up a given change, assuming the supply of coins for each denomination are unlimited

# with denomination [1, 3, 4] cents, what is the minimum number of coins to make up 30 cents?
# an example with only 3 denominations: 1-cent, 3-cents and 4-cents
# suppose there is unlimited supply for each denomination
# what is the minimum number of coins to make up 30 cents
# is it 7 4-cents + 2 1-cent => min is 9 coins.
# the smallest is actually 6*4 + 2*3 => 8 coins

denom = [1, 3, 4]
m = len(denom)
n = 30

min_coin = [float('inf')] * (n + 1) #initialises an empty array for results of 
min_coin[0] = 0

# TODO: implement the DP formula in iterative format
def coin_change_unlimited_iter():

    for i in range(1,len(min_coin)):
        for coin in denom:
            if (coin <= i and i-coin >=0):
                min_coin[i] = min(min_coin[i],min_coin[i-coin]+1)
            else:
                break
    
    
coin_change_unlimited_iter()

for e in enumerate(min_coin):
    print(e)

#tera notes: tried to fit a greedy algo into a DP question, remember to stick to the recurrence relation.

#THIS IS NOT MENTIONED. but uh i wanted to try so 🥴
denom = [1, 3, 4]
m = len(denom)
n = 30

min_coin = [float('inf')] * (n) #initialises an empty array for results of 
min_coin[0] = 0

def coin_change_unlimited_recur(i):
    if i == n:
        return min_coin;
    for coin in denom:
        if (coin <= i and i-coin >=0):
            min_coin[i] = min(min_coin[i],min_coin[i-coin]+1)
    coin_change_unlimited_recur(i+1)

## to start
coin_change_unlimited_recur(1)
    
