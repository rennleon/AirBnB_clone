#!/usr/bin/env python3
"""
This module defines 'HBNBCommand' class
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    commnad interpreter that manages the AirBnB objects.
    """

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, args):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
