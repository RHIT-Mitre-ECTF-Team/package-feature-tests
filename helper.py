import errors

##Takes in the system arguments and converts them into a more
#readable form of arguments for the main program to use. Specifying
#devmode to be true will print out helper information, such as the exact arguments
#being passed into the program values. Note: Processed arguments are returned, not
#directly modified.
def setargs(system_args, devmode=False):
    #validate arguments
    arglist = []
    if devmode:
        arglist = system_args[2:system_args.__len__()]
        errors.checkargs(arglist)
        print("using arguments:\n"+
            "\t SYSTEM_NAME: "+arglist[0]+"\n"+
            "\t DEPL: "+arglist[1]+"\n"+
            "\t PACKAGE_OUT: "+arglist[2]+"\n"+
            "\t PACKAGE_NAME: "+arglist[3]+"\n"+
            "\t CAR_ID: "+arglist[4]+"\n"+
            "\t FEATURE_NUMBER: "+arglist[5])
    else:
        arglist = system_args[1:system_args.__len__()]
        errors.checkargs(arglist)

    #set argument dict and return
    args = {}
    args["NAME"] = arglist[0]
    args["DEPLOYMENT"] = arglist[1]
    args["PACKAGE OUT"] = arglist[2]
    args["PACKAGE NAME"] = arglist[3]
    args["NAME"] = arglist[4]
    args["NAME"] = arglist[5]
    return args