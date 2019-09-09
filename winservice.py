import argparse
import sys
import os
import subprocess


ALL_COMMANDS = ("start", "stop", "remove","restart","status","pause","continue","rotate")

class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith('L|'):
            return text[2:].splitlines()  
        return argparse.HelpFormatter._split_lines(self, text, width)

class Service():

    INSTALL = "nssm install"
    SET = "nssm set"
    RUN = "nssm start"
    BLOCK = "main"
    SERVICE_NAME = "servicename"
    OPTIONS = ("servicename", "Application", "AppDirectory", "AppParameters", 
    "DisplayName", "Description", "Start","DependOnService","AppStdout",
    "AppStderr","AppEnvironmentExtra")

    def __init__(self, path_to_config_file, run):
        try:
            from configparser import ConfigParser
        except ImportError:            
            from ConfigParser import ConfigParser  # ver. < 3.0  
        self.config = ConfigParser()
        print(path_to_config_file)
        self.config.read(path_to_config_file)
        self.set_service(run)
     
    def filling(self, run):
        command = []        
        for option in self.OPTIONS:            
            if self.config.has_option(self.BLOCK, option):                
                if option == self.SERVICE_NAME:
                    command.append('{} {} {}'.format(self.INSTALL, self.config.get(self.BLOCK, option), 'confirm'))
                    self.service = self.config.get(self.BLOCK, self.SERVICE_NAME)                 
                elif self.config.has_option(self.BLOCK, option):
                    command.append('{} {} {} {}'.format(self.SET, self.service, option, self.config.get(self.BLOCK, option)))  
        if run:
            command.append('{} {}'.format(self.RUN,self.service))
        return command 
    

    def set_service(self,run):
        for i in self.filling(run):
            cmd(i)
    
    def get_service_name(self):
        return self.service

def cmd(command):
    cmdCommand = command   #specify your cmd command
    return subprocess.Popen(cmdCommand.split(), shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()

def autostart_service(mode,service):
    if mode == "enable":
        print(cmd('{} {} {}'.format(Service.SET, service, 'Start SERVICE_AUTO_START')))
#        print(cmd(Service.SET + " " + service + " Start SERVICE_AUTO_START"))
    else:
        print(cmd('{} {} {}'.format(Service.SET, service, 'Start SERVICE_DISABLED')))
 #       print(cmd(Service.SET + " "  + service + " Start SERVICE_DISABLED"))            

def transfer_command_to_nssm(command,service):
    command_str = "nssm " + command + " " + service + " confirm"
    print(cmd(command_str))
    

def msg(name=None):   
    return '''winservice.py [-h]
       winservice.py setup <confuration file>
       winservice.py COMMAND <service>
        '''

def start(command,service):
        if command in ALL_COMMANDS:
            transfer_command_to_nssm(command, service)
        elif command == "enable" or command == "disable":
            autostart_service(command, service)
        elif command == "setup":
            srv = Service(service,False)
            print("service '" + srv.get_service_name() + "' installed!")
        elif command == "install":
            srv = Service(service,True)
            print("service '" + srv.get_service_name() + "' installed and run!")
        else:
            print("winservice: '" + command + "' is not a winservice command. See 'winservice.py -h'.")

def main(*args, **kwargs):
    parser = argparse.ArgumentParser(description='Wrapper for nssm.exe', formatter_class=SmartFormatter, usage=msg())
    parser.add_argument("COMMAND", type=str,
                        help="L|management command to execute.\nChoices: start, stop, restart,\nstatus, remove, enable, disable")
    parser.add_argument("service", type=str,
                        help="L|service name or path to\nconfiguration file for setup service")
    args = parser.parse_args()
    start(args.COMMAND,args.service)

if __name__ == '__main__':
        main()
