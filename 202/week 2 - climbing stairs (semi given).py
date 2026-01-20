'''
Climbing stairs problem:
• It takes n steps to reach the top.
• You can either climb 1 or 2 steps each time.
• In how many distinct ways can you climb to the top?
'''
# First find the base case and also
# M(n) = M(n-1) + M(n-2), M is distinct ways to climb to the top

# inefficient - naive fibonacci method
def climbStairs(n): #fib
    if n == 1 or n==2:
        return n
    
    return climbStairs(n-1) + climbStairs(n-2)
    

print(climbStairs(4)) # Gives 5


# TODO: DP - save the value so it doesnt increase
    
