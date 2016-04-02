import sys
from .MigrateCommand import migrate_command


class Manager(object):
    def __init__(self):
        self.commands = dict()

    def register_command(self, command, func):
        self.commands[command] = func

    def run(self):
        arg_cmd = sys.argv[1]

        if arg_cmd in self.commands:
            self.commands[arg_cmd]()
        else:
            print("Command '{cmd}' is not found.\nAvailable commands :\n".format(cmd=arg_cmd))
            for cmd in self.commands:
                print("\t- {cmd} : {doc}\n".format(cmd=cmd, doc=self.commands[cmd].__doc__))