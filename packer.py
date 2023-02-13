import validation

# globals
ARGS = {}
DEV = False

## Takes in the system arguments and converts them into a more
#  readable form of arguments for the main program to use. Specifying
#  devmode to be true will print out helper information, such as the exact arguments
#  being passed into the program values. Note: Processed arguments are returned, not
#  directly modified.
def initialize_packer(system_args, devmode=False):
    # validate arguments
    arglist = []
    if devmode:
        arglist = system_args[2:system_args.__len__()]
        validation.check_args(arglist)
        print("=================INITIALIZED ARGS=================\n"+
              "SYSTEM_NAME:        "+arglist[0]+"\n"+
              "DEPL:               "+arglist[1]+"\n"+
              "PACKAGE_OUT:        "+arglist[2]+"\n"+
              "PACKAGE_NAME:       "+arglist[3]+"\n"+
              "CAR_ID:             "+arglist[4]+"\n"+
              "FEATURE_NUMBER:     "+arglist[5])
    else:
        arglist = system_args[1:system_args.__len__()]
        validation.check_args(arglist)

    # set argument dict and return
    args = {}
    args["SYSTEM_NAME"] = arglist[0]
    args["DEPL"] = arglist[1]
    args["PACKAGE_OUT"] = arglist[2]
    args["PACKAGE_NAME"] = arglist[3]
    args["CAR_ID"] = int(arglist[4])
    args["FEATURE_NUMBER"] = int(arglist[5])

    # setup globals for future use
    global ARGS, DEV
    ARGS = args
    DEV = devmode

## Generates the packaged feature and returns it
def generate_package():
    #dev mode message
    if DEV:
        print("================GENERATING PACKAGE================\n"+
              "OUTPUT LOCATION:    "+ARGS["PACKAGE_OUT"]+"/"+ARGS["PACKAGE_NAME"]+"\n"+
              "USING INPUTS: \n"+
              "   CAR_ID:          "+ARGS["CAR_ID"].__str__()+"\n"+
              "   FEATURE_NUMBER:  "+ARGS["FEATURE_NUMBER"].__str__())
    
    # NOTE: TEMPORARY GENERATION. PLACEHOLDER FOR NOW
    package = int((ARGS["CAR_ID"] + ARGS["FEATURE_NUMBER"]) / 2)
    
    #dev message
    if DEV:
        print("GENERATED CONTENT:  "+package.__str__())

    #return generated package
    return package
    
## Writes the given package to the package file
def write_package(package):
    with open(ARGS["PACKAGE_OUT"]+"/"+ARGS["PACKAGE_NAME"], "w") as file:
        file.write(package.__str__())
    if DEV:
        print("PACKAGE WRITTEN TO: "+ARGS["PACKAGE_OUT"]+"/"+ARGS["PACKAGE_NAME"])

## Returns processed arguments after validating them
def get_args():
    global ARGS
    validation.check_args_initialized(ARGS)
    return ARGS

## Generates and returns the package feature filename in the
#  format "ectf.<SYSTEM_NAME>.<DEPL>.package.bin"
def get_filename():
    global ARGS
    validation.check_args_initialized(ARGS)
    return ARGS["PACKAGE_NAME"]