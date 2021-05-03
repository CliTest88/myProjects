from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
#import Select from 'react-dropdown-select'
import logging
import string
import os
import sys


# Somehow I cann't use npm to install react-dropdown-select on my machine,
# so I am not able to run the test by using react-dropdown-select
# I write some sudo code in python showing basic logical for test
# It is not runnable since elements ids are not real ids
# I only make it partial works



BASE_DIR = "C:\SeleniumWebDrivers"

def TestSelect():

 
        driver_path = os.path.join(BASE_DIR, "chromedriver")
        chrome_options = Options()
        
        #C:\Python27\lib\site-packages\selenium\webdriver\firefox\webdriver.py
        #driver_path = os.path.join(BASE_DIR, "geckodriver")
        #firefox_options = Options()
        #driver = webdriver.Firefox(executable_path=driver_path, options = firefox_options)


        #load webpage for given Url
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)     
        driver.get("https://sanusart.github.io/react-dropdown-select/")
        WebDriverWait(driver, 10);

        #find Select and get all dropdown options list
        selectLink = driver.find_element_by_id('gatsby-chunk-mapping')
        optionsTotal = selectLink.getAllOptions()

        #check if dropdown box has any value selected
        #if not selecled option from dropdown list
        #then select a optionName
        
        selectRow = driver.find_element_by_id(rowId);
        classAttribute =selectRow.getAttribute("class");
        
        if (selectRow in optionsTotal  and !classAttribute.contains("selected"):
             selectItem = driver.find_element_by_id(options.getSelect(selectRow();
	     selecItem.sendKeys("\n")

                                                                      
        #get multi selected options
        selectLink = driver.find_element_by_id('gatsby-chunk-mapping')
        options = isOptionInSelect(selectLink,selectRow);
  
        # very if selected options are in a given dropdown list                                                            
        for optionNmae in options:
            if optionsName in inputOptions:
	       assertTrue(optionName)

        # clear up selected options
        clearButton = driver.find_element_by_id('clearButton_id')
        clearButton.sendKeys("\n")                                                       

        
        driver.quit()
        

def isOptionInSelect(selectLocator,optionName):
        select = ""
        if selectLocator instanceof Select:
            select = selectLocator
        else:
            select = Select(getElement(selectLocator)
		
	options = select.getOptions().findAll{ it.getText().equals(optionName)}
        return options.size() > 0
    

if __name__ == "__main__":
    
TestSelect()
