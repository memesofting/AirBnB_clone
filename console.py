#!/usr/bin/python3
"""Entry point of command interpreter"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

        args = args.strip()
        if not args.split()[0]:
            print('** class name missing **')
            return

        class_name = args.split()[0]
        """try:
            class_name = globals()[args]
        except KeyError:"""
        class_name = globals().get(class_name)
        if class_name is None:
            print("** class doesn't exist **")
            return

        if not issubclass(class_name, BaseModel):
            print("** class doesn't exist **")
            return

        new_instance = class_name()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """prints the string representation of an instance
        based on calss name and id"""

        args = args.strip()
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_id = args[1]
        """class_name = globals().get(class_name)"""
        key = f"{class_name}.{class_id}"
        storage = FileStorage()
        instance = storage.all().get(key)

        if instance:
            print(str(instance))
        else:
            print("**no instance found")
            return

    def do_destroy(self, args):
        """Deletes an instance based on class name and id
        save the changes"""

        args = args.strip()
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_id = args[1]
        key = f"{class_name}.{class_id}"
        storage = FileStorage()
        instance = storage.all().get(key)
        if instance:
            print(str(instance))
            del storage.all()[key]
            storage.save()
            print("deleted")
        else:
            print("**no instance found")
            return

    def do_all(self):
        """prints all string representation of all instances
        base or not on the class name"""

        self.storage = FileStorage()
        all_instances = str(self.storage.all())
        return all_instances

    def do_update(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
