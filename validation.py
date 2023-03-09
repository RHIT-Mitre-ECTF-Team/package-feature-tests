import os

## Checks if there are enough arguments, and will raise an error
#  if they are unsatisfactory. These is used to validate the raw argument list,
#  not the generated argument dictionary.
def check_args(args):
    if args.__len__() != 6:
        if args.__len__() < 6:
            raise Exception("Missing arguments. Please check your arguments and try again.")
        else:
            raise Exception("Too many arguments. Please check your arguments and try again.")
    if not os.path.exists(args[2]):
        raise Exception("Invalid PACKAGE_OUT path. Please use a valid directory for your package output path.")
    if not args[4].isdigit():
        raise Exception("Invalid input for CAR_ID. Please use a valid 32b unsigned integer.")
    if not args[5].isdigit():
        raise Exception("Invalid input for FEATURE_NUMBER. Please use a valid 32b unsigned integer.")

## Checks if arguments were initialized properly, and will raise
#  an error if they are unsatisfactory.
def check_args_initialized(args):
    if len(args) != 6:
        if len(args) == 0:
            raise Exception("Arguments not initialized. Please ensure that arguments have been properly set before using them.")
        else:
            raise Exception("Arguments have not been properly initialized or have been corrupted.")
        
def check_int_list(list):
    if len(list) > 32:
        raise Exception("Argument longer than 32 bits. Please use a smaller one.")