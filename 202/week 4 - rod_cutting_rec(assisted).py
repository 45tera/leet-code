# Uses recursion on the remaining piece of length n-i
# follows the max(Pi + Ri) formula, where P is the function call/length segment out and R is the remaining n-i length.

rod_price = [0,1,5,8,9,10,17,17,20,24,30]

# TOP DOWN APPROACH
def rod_cutting_recur(n):
    if n == 0:
        return 0
        
    q =0
    
    for i in range (1, n+1): #EXPLORES ALL POSSIBILITIES FOR 1 TILL N.
        q = max(q, rod_price[i] + rod_cutting_recur(n-i)) #q here is crucial -> storing the max value of the sub possibilities found.
    return q # only returns the max for the subproblems explored.
    
rod_cutting_recur(4)


#MEMOISATION
n_val = 4 
rod_memoise = [-1] * (n_val + 1) #creation of enough slots hence +1; and the -1 initialisation so that 0 is not clashing 

def rod_cutting_mem(n):
    if n == 0:
        return 0

    # Check index 'n' directly - same goes for any memoisation -> any checks done are a BASE CASE.
    if rod_memoise[n] != -1:
        return rod_memoise[n]
        
    q = 0
    for i in range(1, n + 1):
        q = max(q, rod_price[i] + rod_cutting_mem(n - i))
    
    #Record the result at index 'n'
    rod_memoise[n] = q
    
    #Must return the value it found, so that comparison can happen
    return q

print(rod_cutting_mem(n_val))
