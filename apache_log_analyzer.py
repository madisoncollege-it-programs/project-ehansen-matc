#!/usr/bin/env python3
"""
Author: Eric Hansen 
Email: ehansen@madisoncollege.edu 
Description: This code helps parse through apache log files to make them easier to read and know who is requsting info from a web server.
"""


"""Milestone 8"""
import sys                                                                  #Makes it so we can use an argument when starting the script
import subprocess                                                           #makes it so I can use the subprocess module

def IPAddressCount(apache_log_file_name):                                   
    #below I have the linux command running as a subprocess and stores the byte format of it as the completed process
    completeProcess = subprocess.run(f"cat {apache_log_file_name} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5" , stdout=subprocess.PIPE , shell=True)
    strOutput = completeProcess.stdout.decode()                             #this turns the byte format that was came from the subprocess into a string
    return strOutput                                                        #returns the string output

def main():                                                                 #this turns the whole script into a function 
    intro = "This script will help you read and analyze apache log files"
    print(intro)                                                            #prints the intro variable
    varAnswers = ["y", "yes", "yeah"]                                       #List of answers that will continue the code
    if len(sys.argv) > 1:                                                   #Checks if the user input any argument 
        userResponse = sys.argv[1]                                          #Takes the argument and stores it as userResponse
    else:
        userResponse = input("Would you like to continue?\n>>")             #If no argument was there, asks for a value for userResponse
    if userResponse.lower() in varAnswers:                                  #Checks if any of the accepted answers in varAnswers was given
        result = IPAddressCount('m5-access.txt')                            #uses the new function to show what file to look at and stores it as result
        print(result)                                                       #prints it to the terminal
        outputFile = open("apache_analysis.txt" , "w")                      #opens the analysis file for writing 
        outputFile.write(f"{result}")                                       #writes the result into the analysis file 
    else:                                                                   #if the input at the start of the script doesnt match anything...
        print("You chose not to continue")                                  #...print this and end the script

if __name__ == '__main__':                                                  #this tests the __name__ variable if the script is being run directly. 
    main()                                                                  #if it is than run the whole main function