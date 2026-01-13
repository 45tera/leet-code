# Naive implementation
def ispalindrome(a):
  char_a = list(a)

  if (len(char_a) <= 1):
    return False

  bp = len(char_a) -1
  fp = 0
  while fp < bp:
    if (char_a[fp] != char_a[bp]):
      return False
    fp+=1
    bp-=1
    
return True

# Recursive implementation
def ispalindrome_recur(a):
    # stop case    
    if (len(a)==1 or len(a)==0): 
        return True
        
    # actual function
    back = len(a) -1
    front = 0
    if (a[front] == a[back]): #clearly, i can squish l25-27 into one line;
        return ispalindrome_recur(a[1:-1]) #need to watch out, splicing is start:stop(exclusive)
    else:
        return False



# not very good test cases
print(ispalindrome("ss")) #i missed this case. need to be careful. thanks AI
print(ispalindrome("sas"))
print(ispalindrome("sasb"))
print(ispalindrome("msasm"))
print(ispalindrome_recur("ss")) #i missed this case. need to be careful. thanks AI
print(ispalindrome_recur("sas"))
print(ispalindrome_recur("sasb"))
print(ispalindrome_recur("msasm"))
