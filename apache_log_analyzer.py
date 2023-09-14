#!/usr/bin/env python3
"""
Author: Eric Hansen 
Email: ehansen@madisoncollege.edu 
Description: This code helps parse through apache log files to make them easier to read and know who is requsting info from a web server.
"""

intro = "This script will help you read apache log files"
apacheLog = '111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"'
apacheIP = apacheLog[0:15]
print(intro)

userResponse = input("Would you like to continue? (y/n)")
print(f"You responded: {userResponse}")
print(f"Log Request from: {apacheIP:*^22}")             #formatted string to get just the ip surrounded by *
logList = apacheLog.split(' ')                          #turns apacheLog into a list 
print(f"Return code: {logList[8]}")                     #prints the 9th element in the list (0 being included)
