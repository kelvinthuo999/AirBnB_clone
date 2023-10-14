#!/usr/bin/python3
"""
The console module for the HBNB project.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class defines the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """
        Exit the program when the end of file (EOF) is reached.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

