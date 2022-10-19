# Welcome

# Problem Statement: 
    A restaurant keeps a log of (eater_id, foodmenu_id) for all the diners. The eater_id is a unique number for every diner and foodmenu_id is unique for every food item served on the menu. Write a program that reads this log file and returns the top 3 menu items consumed. If you find an eater_id with the same foodmenu_id more than once then show an error.

# Solution: 

## Library Used:
-
    unittest (no need to install by default installed when you install Python)

## Flow:-
- main File
    * The Solution Logic is in "app/main.py" file, We are reading the logfiles as input and with the help of python Filehandling reading the data, process the data with the help of dictionary, loop and conditions.
    * We are returing output as top 3 menu ids 
    * If we got repeated data in logfiles like same eater_id, menu_id then we are returing Error message

- logfiles
    * logfiles are input files inside logfiles/ folder which contain sample files.
    * The format is like "Log: (eater_id,menu_id)".

- test File:
    * This file use Unittest library to call the main file by sending logfiles as input, one by one and compare the program result with correct result and then provide the test status


## To Run 
    python -m unittest test
- The above command run the test.py file and check the test cases

- If you want to run some other sample files then follow-
    * Run the main file by following command and enter the logfile path as user input
    ## 
        python app/main.py


# Contributor
  - Vivek Sharma
