# implement an algorithm to compute the minimum number of coins to make up a given change, assuming the supply of coins for each denomination are unlimited

# with denomination [1, 3, 4] cents, what is the minimum number of coins to make up 30 cents?
# an example with only 3 denominations: 1-cent, 3-cents and 4-cents
# suppose there is unlimited supply for each denomination
# what is the minimum number of coins to make up 30 cents
# is it 8? 7 4-cents + 2 1-cent

denom = [1, 3, 4]
m = len(denom)
n = 30

min_coin = [float('inf')] * (n + 1)
min_coin[0] = 0

# TODO: implement the DP formula in iterative format


for e in enumerate(min_coin):
    print(e)
