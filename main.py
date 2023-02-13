# imports
import sys
import packer
import validation

# dev variables
DEV = (sys.argv[1] == "DEV")

# initializations
packer.initialize_packer(sys.argv, DEV)

# globals
args = packer.get_args()
package_name = packer.get_filename()

# temporary
package = packer.generate_package()
packer.write_package(package)
