#imports
import sys
import helper
import errors

#dev variables
DEV = (sys.argv[1] == "DEV")

#globals
args = helper.setargs(sys.argv, DEV)

