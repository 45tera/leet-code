# brute force - list + check

#check conflict in diagonals
import itertools

def conflict(i1, j1, i2, j2):
    return (i1-i2 == j1-j2) or (i1 - i2 == - (j1-j2))
  
#check conflict horizontally + vertically - solve by generating a pool where the horizontal and vertical dont conflict.

########################
# side quest - understanding itertools.combinations()
# https://docs.python.org/3/library/itertools.html#itertools.combinations
########################
'''
excerpt from documentation - breaking it down 

itertools.combinations(iterable, r)
Return r length subsequences of elements from the input iterable.

//tera's comments: the itertools.combinations function takes in an iterable object, and r, being the window size of the subsequence length (ie. if i list of 6 things, i want to return all possible combinations of 2 things.)

The output is a subsequence of product() keeping only entries that are subsequences of the iterable. 

// AI assisted help thank heavens: product calls upon itertools.product() to create a Cartesian product. It is every possible outcome.

The length of the output is given by math.comb() which computes n! / r! / (n - r)! when 0 ≤ r ≤ n or zero when r > n.

//tera's comments:the number of output subsequences is the computed via n!/r ! (n-r)! 
// why it is n!/r ! (n-r)! is because that is the binomial coefficient, which is n choose r ; which will show us ; but again, note the conditions: when r is between 0 and n, and where r MUST be less than n. (Cannot 5 choose 6; hence n cannot be more than r)


The combination tuples are emitted in lexicographic order according to the order of the input iterable. If the input iterable is sorted, the output tuples will be produced in sorted order.
Elements are treated as unique based on their position, not on their value. If the input elements are unique, there will be no repeated values within each combination.

//tera's comments: the output is also arranged in a numerical (lexicographical is used in the documentation) order but this is ACCORDING to the order of input. if the input iterable object is not sorted, then the output array/subarrays will be produced in a non sorted order, and based off the order of the input.


Roughly equivalent to:

def combinations(iterable, r):
    # combinations('ABCD', 2) → AB AC AD BC BD CD
    # combinations(range(4), 3) → 012 013 023 123

    pool = tuple(iterable) // tuple is a immutable list
    n = len(pool)
    if r > n:
        return  //edge case here as mentioned, cannot R > N
    indices = list(range(r))   

    yield tuple(pool[i] for i in indices) // yield is an interesting read, its like a stream version of return, that does not close the return option. 
    // checkout: https://www.w3schools.com/python/trypython.asp?filename=demo_ref_keyword_yield
    
    while True:

        // checks the case in which it hits the limit, else return the combination.
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
            
        // incrementer
        indices[i] += 1

        // reset phase
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

    // tera's comments: its an interesting concept - it has a key of incrementing the last digit by one, then once it hits the limit of i+n-r, then the second last digit is incremented, and the last digit is brought back to its initial state. Truly a cool brute force algorithm.

    // tera's comments: another thing of note is that it seems to not check previously made combinations (ie. AB checked, then it does not check BA, which is time efficient in that way.)
'''


