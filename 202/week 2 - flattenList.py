final_flattened = []

#recursion came after like 10-15 minutes 
def flatten(lst):
    
    for subarr in lst:
        
        if (type(subarr) == int):
            final_flattened.append(subarr)
            
        else:
            flatten(subarr)
            
        
    return final_flattened

print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
