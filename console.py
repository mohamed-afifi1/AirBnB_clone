#!/usr/bin/python3
"""this is  Entry point for the command interpreter """
import cmd
from models import storage



class HBNBCommand(cmd.Cmd):
    """Class for the entry point of the command interpreter."""
    prompt = '(hbnb) '
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True
    def default(self, line):
        """Catch commands if nothing else matches then."""
        self._precmd(line)
    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass
    


if __name__ == "__main__":
    HBNBCommand().cmdloop()