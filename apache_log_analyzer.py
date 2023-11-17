#!/usr/bin/env python3
"""
Author: Eric Hansen 
Email: ehansen@madisoncollege.edu 
Description: This code helps parse through apache log files to make them easier to read and know who is requsting info from a web server.
"""

""" Milestone 10 """
import sys , subprocess , argparse , requests , bs4         #imported requests and bs4 to be used in the script 

def IPLookup(IPAddress):
    url = f"https://tools.keycdn.com/geo?host={IPAddress}"  #this sets a variable of the the URL with the supplied IP address
    print(f"Going to '{url}' to find the location...")         #displays the url being used in the script 
    response = requests.get(url)                            #this pulls all the HTML code from the website
    return response

def IPAddressCount(apache_log_file_name):                                   
    completeProcess = subprocess.run(f"cat {apache_log_file_name} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5" , stdout=subprocess.PIPE , shell=True)
    strOutput = completeProcess.stdout.decode()                             
    return strOutput                                                        

def main():                                                                  
    parser = argparse.ArgumentParser(description="A new parser for our script")                  
    parser.add_argument('-f' , '--filename' , dest='fileName' , metavar='[a log file]' , required=True , type=str , help='enter the filename')
    intro = "This script will help you read and analyze apache log files\n"
    print(intro)                                                             
    result = IPAddressCount(parser.parse_args().fileName)
    noNewLineList = result.split("\n")                                              #these 3 lines take the result from the linux command to get the highest occuring IP
    noNewLineStr = ''.join(noNewLineList)
    spaceList = noNewLineStr.split(" ")
    highestOccurence = str(spaceList[-1])                                                #saves the highest occuring IP as a string 
    print(f"[{highestOccurence}] is the highest occuring IP address in that log")   #prints the highest occuring IP 
    response = IPLookup(highestOccurence)                                           #uses the new function with the highest occuring IP in the log file
    #print(response.text[0:250])                                                    #the raw HTML with only the first 250 characters
    myHTML = bs4.BeautifulSoup(response.text, features="html.parser")
    print("The origin of the IP is in " + myHTML.find_all("dd", class_="col-8 text-monospace")[1].text)     #this is the supplied code that pulls the location of th IP from the website                                                                           
    outputFile = open("apache_analysis.txt" , "w")                      
    outputFile.write(result)                                  

if __name__ == '__main__':                                                  
    main()              