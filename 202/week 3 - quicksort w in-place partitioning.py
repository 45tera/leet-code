# Implement function partition with pivot the last element x = A[r]
# After this function, all elements smaller than or equal to x are on the left side of x,
# and all elements greater than x are on the right side of x
# This function should return the index of the pivot
# There shouldn't be any declaration of lists, dictionaries or sets.

def partition(A, p, r):
    # A is a list, p is the starting index and r is the ending index, both inclusive
    # This function should return the index of the pivot
    pivot = A[r]
    
    i = p-1 #
    
    #arr = [10, 7, 8, 9, 1, 2, 5]
    #TODO: implement partition
    for x in range(p,r): #left pointer - NEED TO BE CAREFUL ABOUT DISTINCTION BETWEEN VALUE AND INDEX
       if A[x] < pivot:
           i+=1;
           swap(A,x,i);
    
    swap(A,r,i+1)   
    return i+1

# swap function
def swap(A,a,b):
    A[a], A[b] = A[b], A[a]

def quicksort(arr):
    n = len(arr)
    newP = partition(arr,0,n-1)
    # Left Recur
    partition(arr,0,newP-1)
    # Right Recur
    partition(arr,newP,n-1)

#test cases
arr = [10, 7, 8, 9, 1, 2, 5]
print(arr)
quicksort(arr)
print(arr)
