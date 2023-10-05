#!/usr/bin/env python3
"""
Author: Eric Hansen 
Email: ehansen@madisoncollege.edu 
Description: This code helps parse through apache log files to make them easier to read and know who is requsting info from a web server.
"""

intro = "This script will help you read and analyze apache log files"
# with open("apache_logs.txt" , "r") as logString:            
    # apacheLogs = logString.read()                           #this is the replacement string variable for Milestone 4 so I have it pulled from a file
""" ----Milestone 1---- """
print(intro)                                                #prints the intro variable
#userResponse = input("Would you like to continue? (y/n)")   #takes input from the user and stores it as a variable 
#print(f"You responded: {userResponse}")                     #prints off whatever the the user enters
""" ----Milestone 2---- """                                                  #all of this below is for a single log 
# apacheIP = apacheLogs[0:15]                                  #takes the first 15 characters out of the apacheLog variable and makes a new variable (apacheIP)
# logList = apacheLogs.split(' ')                              #turns apacheLog into a list with each element being after a space
# print(f"Log Request from: {apacheIP:*^22}")                 #formatted string to get just the ip surrounded by *
# print(f"Return code: {logList[8]}")                         #prints the 9th element in the list (0 being included)
""" ----Milestone 3---- """
# logList = apacheLogs.split('\n')                               #this turns each log into a element in a list that are seperated by a new line 
# for element in logList:                                        #this is a loop that goes through each element in the list and stores them as "element" 
#     apacheIP = element[0:15]                                   #similar to milestone 2 except it takes out each individual log
#     logList = element.split(' ')                               #need to change the variable name because its no longer a single log its an element in the list
#     print(f"{apacheIP} - {logList[8]}")
""" ----Milestone 4---- """
# with open("apache_logs.txt" , "r") as logString:                #this opens the file for reading only so I can take from the file without changing it 
#     logList = logString.readlines()                             #readlines() turns the whole string data type file into a list data type and saves it as logList
#     for element in logList:                                     #a loop for going through everything inside the logs.txt file
#         logList = element.split(' ')                            #still need to split each log by a space so I can get just the IP and the HTTP return code
#         outputFile = open("apache_analysis.txt" , "a")          #this will open the new file for appending so I can have a new line each time it goes through and can put it in the file without changing the original 
#         outputFile.write(f"{logList[0]} - {logList[8]} \n")     #this takes the logList variable and puts the IP and HTTP code into the new analysis file and creates a new line to put the next underneath 
#         outputFile.close()                                      #close the file so we dont have an error with it still being open 
#         print(f"{logList[0]} - {logList[8]}")                   #prints the same data put in the new file to the terminal
""" ----Milestone 5---- """
import sys                                                              #Makes it so we can use an argument when starting the script
varAnswers = ["y", "yes", "yeah"]                                       #List of answers that will continue the code
if len(sys.argv) > 1:                                                   #Checks if the user input any argument 
    userResponse = sys.argv[1]                                          #Takes the argument and stores it as userResponse
else:
    userResponse = input("Would you like to continue?\n>>")             #If no argument was there, asks for a value for userResponse
if userResponse.lower() in varAnswers:                                  #Checks if any of the accepted answers in varAnswers was given
    with open("m5-access.txt" , "r") as logString:                  
        logList = logString.readlines()                             
        for element in logList:                
            logList = element.split(' ')
            if int(logList[8]) >= 500:                                  #Takes the integer value of the 8th element in logList and makes sure its at or above 500 before writing it to the file.           
                outputFile = open("apache_analysis.txt" , "a")           
                outputFile.write(f"{logList[0]} - {logList[8]} \n")      
                outputFile.close()
            if int(logList[8]) >= 400:                                  #Takes the integer value of the 8th element in logList and makes sure its at or above 400 before writing it to the file. 
                print(f"{logList[0]} - {logList[8]}")                 
else:
    print("You chose not to continue")
    