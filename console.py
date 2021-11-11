#!/usr/bin/python3

"""
This module implements the HBnB console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def emptyline(self) -> bool:
        pass

    def do_quit(self, args):
        """Quit command to exit program
        """
        return True

    def do_EOF(self):
        """Executes EOF signal to quit program
        """
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
