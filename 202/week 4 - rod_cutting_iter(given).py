#
rod_price = [0,1,5,8,9,10,17,17,20,24,30]

n = len(rod_price) -1 # -1 addresses the '0' at the start
max_price = [0] * (n+1) 
first_cut = [0] * (n+1)

def rod_cutting_iterative():
  for i in range(1, n+1): # i stands for the length of the rod
    for j in range(1, i+1): # j stands for the possible cuts from 1 till i (non-inclusive of i+1)
      new_price = rod_price[j] + max_price[i-j]
      if new_price > max_price[i]:
        max_price[i] = new_price
        first_cut[i] = j

rod_cutting_iterative()
print('max_price:', max_price)
print('first_cut:', first_cut)
