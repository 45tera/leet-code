# checks the odd numbers ONLY
def naive(upper_bound):
    # i: for all odd numbers less than upper_bound
        # j: for all odd numbers less than i
    for i in range(3, upper_bound, 2): #checking the odd numbers till upper bound
        for j in range(3, i, 2): # all odd from 3 onwards till odd number specified
            if i % j == 0:
                break # why break? - if there is no remainder, means divide easily.
                #as long as you find on number that can divide - means its a factor
                # then it is not a prime.
        else:
            prime.append(i)
    return prime

# uses prime list to check the odd numbers given
def improved(upper_bound):
    prime = [2]
    for i in range(3, upper_bound, 2):
        found = False
            for j in prime:
        if i % j == 0:
            found = True
            break
        if not found:
            prime.append(i)
    return prime

# uses rooted limit to check - limits
def improved2(upper_bound):
    prime = [2]
    rooted_limit = math.floor(math.sqrt(upper_bound))
    for i in range(3, upper_bound, 2):
      found = True 
      for j in prime:
        if j > rooted_limit:
          break
        if i % j == 0:
          found = False #found that it is not a prime
          break
      if found:
        prime.append(i)
    return prime

# cool test cases
l1 = naive(200)
l2 = improved(200)
l3 = improved2(200)
res = l1 == l2 == l3
print(res)
