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
#              the epoch from stdin (formatted YYYY MM DD mm SS) and using the
#              system's current time to calculate and output a 4-character code.
################################################################################

from time import time
import sys

################################################################################

#global vars here
DEBUG = True



################################################################################

#functions here



###############################MAIN#############################################


#confirm proper usage of program
if(len(sys.argv) < 6):
	print("Usage: ./timelock.py YYYY MM DD mm SS")
	exit()




