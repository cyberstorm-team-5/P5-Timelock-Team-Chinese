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

######CONVERT TO UTC TIME TO MAKE DAYLIGHT SAVINGS WORK

import time
import sys
import md5
import hashlib

################################################################################

#global vars here
DEBUG = True

customSystemTime = True

################################################################################
code = ""
alpha = ""
nums = ""
#functions here
def get_hex():
	epochIn = sys.stdin.read().strip('\n')
	epochTime = time.strptime(epochIn, "%Y %m %d %H %M %S")
	temp = time.mktime(epochTime)
	a = int(temp)
	if (customSystemTime):
		systemtime = "2015 01 01 00 01 30"
		bconv = time.strptime(systemtime, "%Y %m %d %H %M %S")
		temp2 = time.mktime(bconv)
		b = int(temp2)
	else:
		#for non custom system time
		pass

	c = b-a
	d = c %60
	correctDifference = c - d
	convertToHex = str(correctDifference)
	temp3 = md5.new(convertToHex).hexdigest()
	global code
	code += md5.new(temp3).hexdigest()

def get_code():
        for i in code:
                if (i.isalpha() == True):
                        global alpha
                        alpha += i
                else:
                        global nums
                        nums += i
        global Code
        Code = alpha[:2] + nums[-1] + nums[-2]
        print Code
###############################MAIN#############################################
get_hex()
get_code()
