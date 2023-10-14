#!/usr/bin/python3
"""
This is the console module for the HBNB project.
"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class defines the command interpreter for the HBNB project.
    """

    prompt = "(hbnb) "

    valid_classes = ["BaseModel"]  # Add other class names as needed

    def do_quit(self, line):
        """
        Quit the command interpreter.
        """
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

    def do_create(self, line):
        """
        Create a new instance, save it to the JSON file, and print the id.
        Usage: create <class name>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Print the string representation of an instance based on class name and id.
        Usage: show <class name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Delete an instance based on class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print all string representations of instances based on the class name or all instances.
        Usage: all [class name]
        """
        args = line.split()
        all_objects = storage.all()
        result = []
        if not args:
            for key in all_objects:
                result.append(str(all_objects[key]))
        elif args[0] in HBNBCommand.valid_classes:
            for key in all_objects:
                if key.split(".")[0] == args[0]:
                    result.append(str(all_objects[key]))
        else:
            print("** class doesn't exist **")
            return
        print(result)

    def do_update(self, line):
        """
        Update an instance based on class name and id by adding or updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key in all_objects:
                obj = all_objects[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
