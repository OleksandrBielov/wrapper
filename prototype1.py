import sys
import os

service = sys.argv[1].split('.')[0]
# print(service) 

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

command = []

# instantiate
config = ConfigParser()

# parse existing file
config.read(sys.argv[1])

# read values from a section
if config.has_option(service, 'servicename'):
    string_servicename = config.get(service, 'servicename')
    command.append("nssm install " + string_servicename + " confirm")

if config.has_option(service, 'Application'):
    string_application = config.get(service, 'Application')
    command.append("nssm set " + string_servicename + " Application " + string_application)

if config.has_option(service, 'AppDirectory'):
    string_appdirectory = config.get(service, 'AppDirectory')
    command.append("nssm set " + string_servicename + " AppDirectory " + string_appdirectory)

if config.has_option(service, 'AppParameters'):
    string_appparameters = config.get(service, 'AppParameters')
    command.append("nssm set " + string_servicename + " AppParameters " + string_appparameters)

if config.has_option(service, 'AppEnvironmentExtra'):
    string_appenvironmentExtra = config.get(service, 'AppEnvironmentExtra')
    command.append("nssm set " + string_servicename + " AppEnvironmentExtra " + string_appenvironmentExtra )

command.append("nssm start " + string_servicename)

for i in command:
#    print(i)
    os.system(i)

print(string_servicename + " started")
