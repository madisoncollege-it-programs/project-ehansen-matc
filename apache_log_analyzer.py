#!/usr/bin/env python3
"""
Author: Eric Hansen 
Email: ehansen@madisoncollege.edu 
Description: This code helps parse through apache log files to make them easier to read and know who is requsting info from a web server.
"""

""" Milestone 9 """
import sys                                                                  
import subprocess                                                           
import argparse #Makes argparse available to use 

def IPAddressCount(apache_log_file_name):                                   
    completeProcess = subprocess.run(f"cat {apache_log_file_name} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5" , stdout=subprocess.PIPE , shell=True)
    strOutput = completeProcess.stdout.decode()                             
    return strOutput                                                        

def main():                                                                  
    parser = argparse.ArgumentParser(description="A new parser for our script")                   #sets a variable called parser that I can use argparse's modules and functions with 
    parser.add_argument('-f' , '--filename' , dest='fileName' , metavar='[a log file]' , required=True , type=str , help='enter the filename')   #adds a argument that is required to enter before the script will run
    intro = "This script will help you read and analyze apache log files\n"
    print(intro)                                                             
    result = IPAddressCount(parser.parse_args().fileName)  #uses the variable that parser made called fileName in the IPAddressCount function                           
    print(result)                                                       
    outputFile = open("apache_analysis.txt" , "w")                      
    outputFile.write(result)                                  

if __name__ == '__main__':                                                  
    main()                                                                  