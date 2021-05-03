
# Somehow I cann't use npm to install react-dropdown-select on my machine,
# so I am not able to run the test by using react-dropdown-select
# I also write some sudo code in python showing basic logical for test
# It is not runnable since elements ids are not real ids
# I only make it partial works

==============workflow for Python uiTest==================

•	Setup all testing enviroment
•       Download and install selenium
•	Setup selenium webdriver
•	
•	======== code logical==========
•	Navigate to a Web page.
•	Locate an HTML element on the Web page.
•	Perform an action on an HTML element.
•	Anticipate the browser response to the action.
•	Run tests and record test results using a test framework.
•	Select multi name options from dropdown list
•	Get get all selected option name
•	veryfy name is in dropdown list
•	clear all selected options
•	Conclude the test.


============JavaScript react-dropdown-select=========
       I have include some sample react-dropdown-select test which I leant from internet
       But no environment to verify on my current machine
   
       Just find there are set of API functions provided by web site provided for react-dropdown-select
       So we can use API call function to write the tests
======================JavaScript react-dropdown-select tests use API call functions======================
•	Logical is as below:
•	Use API functionn call to find all items in dropdown list
•	Use Api call to check if there is any dropdwon item is selected or is multi selected
•	If no item be selected then fire event to selected one
•	Wait for response, and get selected value
•	Verify if selected name in total options list
•	if yes, get selected value
•	Verify if selected names in total options list
•	clear all selected options
•	Conclude the test.