##Checks if there are enough arguments, and will raise an error
#if they are unsatisfactory.
def checkargs(args):
    if args.__len__() != 6:
        if args.__len__() < 6:
            raise Exception("Missing arguments. Please check your arguments and try again.")
        else:
            raise Exception("Too many arguments. Please check your arguments and try again.")