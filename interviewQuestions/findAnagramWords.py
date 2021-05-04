import string
import os
import sys
import time

#  Input:
#  An input string contains the given set of words as below:
#  sInput = "ARMY AZYY"
#  sInput = "ARMY MARY AMRY AYMR AZYY ZAYY"

#  Output:
#  Strings in list: ['MARY', 'AMRY', 'AYMR', 'ARMY'] are anagrams
#  Strings in list: ['AZYY', 'ZAYY'] are anagrams

#  If no anagrams found then print message below:
#  No anagrams found in those strings: ARMY AZYY


def findAnagrams (sInput):

         sList = sInput.split(' ')
         anagramsList = []
         snList = []
         
         for i in sList:
             snList.append(i)
         
         for sItem in sList:
              itemLen = len(sItem)
              snList.remove(sItem)
              sanagramsList = []
              
              if len(snList) == 0:
                  break
              else:
                for nItem in snList:
                  if len(nItem) == itemLen:
                     stts = isAnagrams(nItem, sItem)
                     if stts == True:
                         sanagramsList.append(nItem)
                    
                if len(sanagramsList) != 0:
                   sanagramsList.append(sItem)
                   anagramsList.append(sanagramsList)
                   upDateList(sList, sanagramsList)
                   upDateList(snList, sanagramsList)
                elif len(sList) == 2:
                  sItem = sList[0]
                  nItem = sList[1]
                  stts = isAnagrams(nItem, sItem)
                  if stts == True:
                     anagramsList.append(snList)
                 
      
         return anagramsList


def isAnagrams(item1, item2):

    flag1 = True
    flag2 = True
    flag = False
    
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

    return flag

    
        
def upDateList(oList, inputList):

    for item in inputList:
        if item in oList:
            oList.remove(item)

    return oList

    
    

if __name__ == "__main__":
  
  #sInput = "ARMY AZYY"
  sInput = "ARMY MARY AMRY AYMR AZYY ZAYY"
  
  anagramsList = findAnagrams(sInput)
  if len(anagramsList) != 0:
    for i in anagramsList:
      if len(i) != 0:
         print "Strings in this list: %s are anagrams"%i
  else:
      print "No anagrams found in those strings: %s"%sInput

