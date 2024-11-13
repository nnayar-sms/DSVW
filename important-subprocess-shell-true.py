import subprocess
import sys

# ruleid:subprocess-shell-true
subprocess.call("grep -R {} .".format(sys.argv[1]), shell=True)

# ruleid:subprocess-shell-true
subprocess.run("grep -R {} .".format(sys.argv[1]), shell=True)
