#!/usr/bin/env python2.7
################################################################################
# Authors: Team Chinese (Lane Arnold, Christopher Boquet,
# 	   Christopher Bouton, Darrell Durousseaux, Clay Fonseca,
#	   Rebecca Grantham, Andrew Maurice)
# Class: CSC 442
# Date: 5-1-2019
# Github Repo: https://github.com/cyberstorm-team-5/P5-Timelock-Team-Chinese
# Description: Program 5: TimeLock
#              The Python code will implement the TimeLock algorithm by reading
#              the epoch from stdin (formatted YYYY MM DD HH mm SS) and using the
#              system's current time to calculate and output a 4-character code.
################################################################################

import time
import datetime
import sys
import md5

################################################################################

DEBUG = True

#determine if to use custom system time and, if so, what it should be
useCustomSysTime = False
valueCustomSysTime = "2015 01 01 00 01 00"

#how long (in seconds) a code would be valid for
secondsValid = 60


################################################################################

#convert a time string (formatted YYYY MM DD HH mm SS) into UTC
def toUTC(timeString):
        #convert string into time struct, then convert the struct to
        #UTC time since epoch to return
        timeStruct = time.strptime(timeString, "%Y %m %d %H %M %S")
        return int(time.mktime(timeStruct))


#retrieve the hex value to use for retrieving the code
def getHex():
        
	#retrieve time from stdin and convert it to UTC
	epochTime = toUTC(sys.stdin.read().strip('\n'))

	#determine whether to use custom or real system time
	if (useCustomSysTime):
                #retrieve global for custom system time and convert it to UTC
		systemTime = toUTC(valueCustomSysTime)
		
	else:
		#for non custom system time, get the dateTime and retrieve the necessary data
                #from it, formatted "YYYY MM DD HH mm SS" for consistency
		dateTime = datetime.datetime.now()
		systemTime = toUTC("{} {} {} {} {} {}".format(dateTime.year, dateTime.month, \
                                dateTime.day, dateTime.hour, dateTime.minute, dateTime.second))

        #compute unadjusted time elapsed
	timeElapsed = systemTime - epochTime
	#adjust time elapsed based on how long (in seconds) the code is valid for
	timeElapsedAdjustment = timeElapsed % secondsValid

	#get the true (adjusted) time elapsed converted to hex with md5
	#to return for retrieving the code
	trueTimeElapsed = str(timeElapsed - timeElapsedAdjustment)
	return (md5.new(md5.new(trueTimeElapsed).hexdigest()).hexdigest())


#use a hex string to retrieve the secret code (first two letters a-f from left
#to right and first two numbers 0-9 from right to left)
def getCode(hexString):
        #show full hexstring for debugging
        if(DEBUG):
                print(hexString)
        
        #setup strings for holding the letters and numbers found in the hex
        alpha = ""
        nums = ""

        #retrieve the first 4 letters from left to right
        for i in hexString:

                #append the letter found to the end of the alpha string
                if (i.isalpha()):
                        alpha += i
                        
                        #once four letters are found, no longer need anymore
                        if(len(alpha) >= 4):
                                break
                        
        #retrieve the first 4 numbers from right to left
        for i in range(len(hexString)-1, -1, -1):
                
                #append the number found to the end of the nums string
                if (not hexString[i].isalpha()):
                        nums += hexString[i]
                        
                        #once four numbers are found, no longer need anymore
                        if(len(nums) >= 4):
                                break

        #retrieve the four digit code, handling special cases of not having enough
        #digits or letters retrieved from the hex string
        if(len(alpha) >= 2 and len(nums) >= 2):
                #no special case needed
                code = alpha[:2] + nums[:2]

        elif(len(alpha) < 2):
                #combine all of the letters and numbers in the string, removing an
                #extra number from the end if there is one (index 5 if len(alpha) == 1)
                code = alpha + nums
                code[:4]
                
        else:
                #not enough numbers, so either use three letters if there is one number,
                #or all letter if no numbers
                if(len(nums) == 1):
                        code = alpha[:3] + nums
                else:
                        code = alpha

        #send resulting 4-digit code to stdout
        print code


###############################MAIN#############################################
getCode(getHex())
