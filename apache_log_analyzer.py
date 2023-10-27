#!/usr/bin/env python3
"""
Author: Eric Hansen 
Email: ehansen@madisoncollege.edu 
Description: This code helps parse through apache log files to make them easier to read and know who is requsting info from a web server.
"""

intro = "This script will help you read and analyze apache log files"
print(intro)                                                                #prints the intro variable
""" ----Milestone 7---- """
def ParseLogEntry(logParse):                                                #defines the new function to be used in the code
    lineList = logParse.split(' ')                                          #these three lines are the same from previous milestones
    logIP = lineList[0]                                                     #^^^ this is a local variable (used only in the function)
    logHTML = lineList[8]                                                   #^^^
    return logIP , logHTML                                                  #returns both the variables logIP and logHTML to be used ouside the function

def main():                                                                 #this turns the whole script into a function 
    import sys                                                              #Makes it so we can use an argument when starting the script
    varAnswers = ["y", "yes", "yeah"]                                       #List of answers that will continue the code
    if len(sys.argv) > 1:                                                   #Checks if the user input any argument 
        userResponse = sys.argv[1]                                          #Takes the argument and stores it as userResponse
    else:
        userResponse = input("Would you like to continue?\n>>")             #If no argument was there, asks for a value for userResponse
    if userResponse.lower() in varAnswers:                                  #Checks if any of the accepted answers in varAnswers was given
        with open("m5-access.txt" , "r") as logString:                      #opens up an outside file to read called m5-access.txt
            logList = logString.readlines()                                 #makes a list of each line out of the used file
            apache_log_summary = {}                                         #creates a dictionary 
            for line in logList:                
                logIP , logHTML = ParseLogEntry(line)                       #uses the function to go through each line and takes the two variables that were returned from the ParseLogEntry function then applies them as global variables                                            
                if logIP in apache_log_summary:                             #checks if the IP is already in the dictionary 
                    apache_log_summary[logIP] += 1                          #if it is add 1 to its value (showing number of occurrences)
                else:                                                       #if its not put the ip as a key in the dictionary and make its value 1
                    apache_log_summary[logIP] = 1
                if int(logHTML) >= 400:                                     #checks if the integer value of logHTML is greater than or at 400
                    print(f"{logIP} - {logHTML}")                           #if it is, prinits out the IP and the HTML code seprated by a dash 
        outputFile = open("apache_analysis.txt" , "w")                      #opens the analysis file outside the for loop so it doesnt only return the last entry
        for vKey , vValue in apache_log_summary.items():                    #After its done adding to the dict, loop through the dict for each item 
            if vValue >= 5:                                                 #if the number of times that the IP address tried to contact us was greater than 5...
                outputFile.write(f"{vKey} has {vValue}\n")                  #...add it to the analysis file
        outputFile.close()                  
    else:                                                                   #if the input at the start of the script doesnt match anything...
        print("You chose not to continue")                                  #...print this and end the script

if __name__ == '__main__':                                                  #this tests the __name__ variable if the script is being run directly. 
    main()                                                                  #if it is than run the whole main function