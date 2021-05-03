
##############
#  DOCUMENTATION
#  Author: Christine Li
#  Date: 5/1/2021
#  A program prints out all friendly words from given a set of words
##############

#  The Input file: the given set of words with format below:
#  car
#  cheating
#  dale
#  ...
#  The output file: the output set of friendly words with format below:
#  cheating teaching 
#  dale deal lead 
#  listen silent 
#  ...
# A flag is desined to control the output by user:
# True: the result is written to an output file
# False: the result is only displayed on the screen
# Below is commends to run code:

# Usage: python --inFile --outFile --wtFlag
# program can also be run from python IDE directly
 

import string
import os
import sys
import time
import argparse
import optparse




class FriendlyWords:

     def __init__(self, inFile, outFile):
        self.inFile = inFile
        self.outFile = outFile
  

# Function: find all friendly word
     def findFriendlyWords(self):
          
         friendlywordsLst = []
         snList = []
         sList = self.generateList()
  
         for i in sList:
             snList.append(i)
         
         for sItem in sList:
              itemLen = len(sItem)
              snList.remove(sItem)
              sfriendlywordsLst = []
              
              if len(snList) == 0:
                  break
              else:
                for nItem in snList:
                  if len(nItem) == itemLen:
                     stts = self.isFriendlyWord(nItem, sItem)
                     if stts == True:
                         sfriendlywordsLst.append(nItem)
                    
                if len(sfriendlywordsLst) != 0:
                   sfriendlywordsLst.append(sItem)
                   sfriendlywordsLst.sort()
                   friendlywordsLst.append(sfriendlywordsLst)
                   self.upDateList(sList, sfriendlywordsLst)
                   self.upDateList(snList, sfriendlywordsLst)
                else:
                    sList.remove(sItem)
                    
                if len(sList) == 2:
                  sItem = sList[0]
                  nItem = sList[1]
                  stts = self.isFriendlyWord(nItem, sItem)
                  if stts == True:
                     friendlywordsLst.append(snList)
                     
         friendlywordsLst.sort()
         #print friendlywordsLst
         return friendlywordsLst
     
        

# Function: check if two words are friendly
     def isFriendlyWord(self, item1, item2):
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

       
 # update array by removing anagram word
     def upDateList(self, oList, inputList):

         for item in inputList:
             if item in oList:
                oList.remove(item)
             else:
                pass

         return oList



# Function: read given set of words from input file, and store them into an array           
     def generateList(self):

         inList = []
         try:
           fd = open(self.inFile, 'r')
           lines = fd.readlines()
           for line in lines:
               line = line.strip()
               line = line.lower()
               inList.append(line)    
           fd.close()
           return inList
         except (IOError, OSError) as e:
             print " Could not open the file:%s " %self.inFile
             sys.exit()


# A function which prints out the result
     def prtFriendlyWord(self,wtFlag):
          
          inLst = self.findFriendlyWords()
          inLst.sort()
          
          for i in inLst:
              stra = ""
              for ii in i:
                  stra += ii + " "
              print stra

          print wtFlag
          if wtFlag == True:
             self.writeToFile()


#A function which writes the result to output file
     def writeToFile(self):
        
         inLst = self.findFriendlyWords()
        
         try:
           fp = open(self.outFile, 'w')
           for i in inLst:
              stra = ""
              for ii in i:
                  stra += ii + " "
              if wtFlag == True:
                 stra += "\n"
                 fp.write(stra)
              else:
                  pass
         except (IOError, OSError) as e:
             print " Could not write to the file:%s " %self.outFile
             sys.exit()
          
             

if __name__ == "__main__":

  parser = optparse.OptionParser()
  parser = optparse.OptionParser(add_help_option=False)
  parser.add_option("-h", "--help", action="store_true", default=False)
  parser.add_option("-i", "--inFile", help="An input file with set of words")
  parser.add_option("-o", "--outFile", help="An output file with saved friendly words")
  parser.add_option("-f", "--wtFlag", help="Flag")
  options, args = parser.parse_args()

  if options.help:
       print "Usage: python --inFile --outFile --wtFlag"
       sys.exit()
  

  # A flag is desined to control the output by user:
  # True: the result is written to an output file
  # False: the result is displayed on the screen
  
  wtFlag = True
  
  inFile = options.inFile
  outFile = options.outFile
  
  if options.wtFlag:
       wtFlag = options.wtFlag
       print wtFlag
   

  inLst = []
  rootPath = "C:/Users/cli/interview"
  inFile = rootPath + "/input.txt"
  outFile = rootPath + "/output.txt"
  
  
  
  ob = FriendlyWords(inFile,outFile)
  ob.prtFriendlyWord(wtFlag)



     
