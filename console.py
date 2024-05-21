#!/usr/bin/python3
"""Entry point of command interpreter"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """creates a new instance of BaseModel
        saves it to JSON file and print the id"""

        if not args:
            print('class name missing')
            return
        class_name = args.split()[0]
        try:
            class_name = globals()[args]
        except KeyError:
            print("class doesn't exist")
            return
        if not issubclass(class_name, BaseModel):
            print("class doesn't exist")
            return
        new_instance = class_name()
        new_instance.save()
        print(new_instance.id)

    def do_show(self):
        pass

    def do_destroy(self):
        pass

    def do_all(self):
        pass

    def do_update(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
