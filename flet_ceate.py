import os
import sys
from flet_component import FletCreateComponent

args = sys.argv


def check_if_app_exist(appname):
    if os.path.exists(appname):
        return True


if len(args) < 2:
    print("Please provide a valid app name.")
    sys.exit(1)

appname = args[1]
if not check_if_app_exist(appname):
    print("App does not exist.")
    sys.exit(1)

if len(args) < 3:
    print("Please provide a command (model, view, controller)")
    sys.exit(1)

if len(args) < 4:
    print("Please provide a name for your component.")
    sys.exit(1)

command = args[2]
componentname = args[3]

FletCreateComponent(command, appname, componentname)
