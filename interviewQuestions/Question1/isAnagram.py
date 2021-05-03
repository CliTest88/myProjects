import string
import os
import sys
import time


# This is a simple program which just verify two words
def isAnagrams(sInput):

    
    flag1 = True
    flag2 = True
    flag = False
    
    sList = sInput.split(' ')
    item1 = sList[0]
    item2 = sList[1]
    
    oItem = list(item1)
    eItem = list(item2)
  
    for item in oItem:
        if item in item2:
           pass
        else:
            flag1 = False
            break
    
    for item in eItem:
        if item in item1:
            pass
        else:
            flag2 = False
            break

    if flag1 == True and flag2 == True:
        flag = True
        
    if flag == True:
      print "%s is an anagram of %s" %(item1,item2)
    else:
      print "%s is not an anagram of %s" %(item1,item2)
    return flag

    
        


    
    

if __name__ == "__main__":
  
  
  sInput = "ARMY MARY"
  
  flag = isAnagrams(sInput)


    
