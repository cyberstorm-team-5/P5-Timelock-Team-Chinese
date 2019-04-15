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

################################################################################

#global vars here
DEBUG = True



################################################################################

#functions here



###############################MAIN#############################################

#get epoch from stdin
epochIn = sys.stdin.read().strip('\n')
print(epochIn)

#epochTime = time.struct_time(tm_year=epochIn[0], tm_mon=epochIn[1], tm_mday=epochIn[2], tm_hour=epochIn[3], tm_min=epochIn[4], tm_sec=epochIn[5])
epochTime = time.strptime(epochIn, "%Y %m %d %H %M %S")

print(epochTime)
a = time.mktime(epochTime)
utcEpoch = time.gmtime(a)

print(newh)
