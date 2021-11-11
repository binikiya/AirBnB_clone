#!/usr/bin/python3

"""

"""

import cmd
from models.user import User

class HBNBCommand(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb)"
        

    def help(self):
        pass

    def quitcmd(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
