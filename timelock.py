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
import sys
import md5
import hashlib

################################################################################

DEBUG = True

#determine if to use custom system time and, if so, what it should be
useCustomSysTime = True
valueCustomSysTime = "2015 05 15 14 00 00"

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
		#for non custom system time
		pass

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

        ###########need to change to handle if not two nums or two letters
        code = alpha[:2] + nums[:2]
        print code
###############################MAIN#############################################
getCode(getHex())
