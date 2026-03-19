denom = [(1,10), (3,6), (4,2)] 
n = 30 # Target
m = len(denom) # Number of coin types

# Initialize: Rows = Coin types + 1 (for the "no coin" row), Cols = Target + 1
dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

# Base Case: 0 coins to make 0 cents
for j in range(m + 1):
    dp[j][0] = 0

def limited_coin_change():
    # Loop through each coin type (j)
    # We use 1-based indexing for j to easily look back at dp[j-1]
    for j in range(1, m + 1):
        coin_val, coin_qty = denom[j-1] 
        
        # Loop through every target amount (i) from 1 to 30
        for i in range(1, n + 1):
            
            # This is your 'k' loop from the image formula
            # k is the number of coins of the current type you choose to use
            for k in range(0, coin_qty + 1):
                
                # Check if we can even afford to use k coins
                if i >= k * coin_val:
                    # Logic: Use k coins + best way to make the remainder 
                    # using PREVIOUS coin types (j-1)
                    remainder = i - (k * coin_val)
                    
                    # Look at the previous row (j-1) for the remainder
                    res = k + dp[j-1][remainder]
                    
                    # Update current cell with the minimum found
                    dp[j][i] = min(dp[j][i], res)

limited_coin_change()
print(f"Min coins for {n}: {dp[m][n]}")
