#!/usr/bin/python3
"""Entry point of command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
