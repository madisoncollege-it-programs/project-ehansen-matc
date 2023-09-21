#!/usr/bin/env python3
"""
Author: Eric Hansen 
Email: ehansen@madisoncollege.edu 
Description: This code helps parse through apache log files to make them easier to read and know who is requsting info from a web server.
"""

intro = "This script will help you read and analyze apache log files"
apacheLogs = """111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.124 HOME - [01/Feb/1998:01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.125 AWAY - [01/Feb/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 401 9332 "http://www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.126 AWAY - [01/Feb/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 501 207 "http://www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)"""
"----Milestone 1----"
print(intro)                                                #prints the intro variable
#userResponse = input("Would you like to continue? (y/n)")   #takes input from the user and stores it as a variable 
#print(f"You responded: {userResponse}")                     #prints off whatever the the user enters
"----Milestone 2----"                                                  #all of this below is for a single log 
# apacheIP = apacheLogs[0:15]                                  #takes the first 15 characters out of the apacheLog variable and makes a new variable (apacheIP)
# logList = apacheLogs.split(' ')                              #turns apacheLog into a list with each element being after a space
# print(f"Log Request from: {apacheIP:*^22}")                 #formatted string to get just the ip surrounded by *
# print(f"Return code: {logList[8]}")                         #prints the 9th element in the list (0 being included)
"----Milestone 3----" 
logList = apacheLogs.split('\n')                               #this turns each log into a element in a list that are seperated by a new line 
for element in logList:                                        #this is a loop that goes through each element in the list and stores them as "element" 
#   print(element)
    apacheIP = element[0:15]                                   #similar to milestone 2 except it takes out each individual log
    logList = element.split(' ')                               #need to change the variable name because its no longer a single log its an element in the list
    print(f"Log Request from: {apacheIP:*^22}")
    print(f"Return code: {logList[8]}")