import sys
import os

def filling(service):
    NSSM = "nssm "
    options = ["servicename", "Application", "AppDirectory", "AppParameters", "AppEnvironmentExtra"]
    command = []

    for option in options:

        if config.has_option(service, option):

            if config.get(service, option) == service:
                command.append("nssm install " + config.get(service, option) + " confirm")
            
            elif config.has_option(service, option):
                command.append(NSSM + "set " + service + " " + option + " " + config.get(service, option))



    
    command.append("nssm start " + service)

    return command
    
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0



# instantiate
config = ConfigParser()
config.read(sys.argv[1])

for i in filling("main"):
    print(i)
#     os.system(i + " > null")
#    os.system(i)


#print("service installed")
print("service '"  + sys.argv[1].split('.')[0] + "' installed")
