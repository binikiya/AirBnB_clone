#!/usr/bin/python3

"""
This module implements the HBnB console
"""

import cmd
from models import storage
from models.base_model import BaseModel

from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):

    classnames = [
        'BaseModel',
        'User',
        'Amenity',
        'Place',
        'Review',
        'State',
        'City'
    ]

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Quit command to exit program
        """
        return True

    def do_EOF(self):
        """ Executes EOF signal to quit program
        """
        print("")
        return True

    def do_all(self, args):
        """ Prints all string representation of all
        instances based or not on the class name.
        Usage: all Classname or all
        """
        filtered_obj = []
        all_instance = storage.all()
        parsed_args = args.split()
        if len(parsed_args) == 0:
            for i in all_instance.values():
                filtered_obj.append(i.__str__())
        elif len(parsed_args) == 1:
            if parsed_args[0] in self.classnames:
                for i in all_instance.values():
                    if i.__class__.__name__ == parsed_args[0]:
                        filtered_obj.append(i.__str__())
            else:
                print("** class doesn't exist **")
                return
        print(filtered_obj)

    def do_show(self, args):
        """ Prints the string representation of an instance
        based on the class name and id
        Example : show classname id
        """
        parsedargs = args.split()
        all_instance = storage.all()
        class_name = ""
        arg_len = len(parsedargs)
        if arg_len > 1:
            class_name, class_id = parsedargs
            id_formatted = '{}.{}'.format(class_name, class_id)
            if class_name in self.classnames:
                if id_formatted not in all_instance:
                    print("** no instance found ** ")
                else:
                    print(all_instance[id_formatted])
            elif class_name not in self.classnames:
                print("** class does'nt exist ** ")
        elif arg_len == 1 and parsedargs[0] not in self.classnames:
            print("** class does'nt exist ** ")
        elif arg_len == 1 and parsedargs[0] in self.classnames:
            print("** instance id missing ** ")
        if arg_len == 0:
            print("** class name missing ** ")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name 
        and id (save the change into the JSON file)
        Usage : destroy classname id
        """
        parsedargs = args.split()
        all_instance = storage.all()
        class_name = ""
        arg_len = len(parsedargs)
        if arg_len > 1:
            class_name, class_id = parsedargs
            id_formatted = '{}.{}'.format(class_name, class_id)
            if class_name in self.classnames:
                if id_formatted not in all_instance:
                    print("** no instance found ** ")
                else:
                    del all_instance[id_formatted]
                    storage.save()
            elif class_name not in self.classnames:
                print("** class does'nt exist ** ")
        elif arg_len == 1 and parsedargs[0] not in self.classnames:
            print("** class does'nt exist ** ")
        elif arg_len == 1 and parsedargs[0] in self.classnames:
            print("** instance id missing ** ")
        if arg_len == 0:
            print("** class name missing ** ")

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        parsed_args = args.split()
        if len(parsed_args) == 0:
            print("** class name missing **")
        if len(parsed_args) >= 4:
            class_name, class_id, attr_name, attr_val, *tmp = parsed_args
            if class_name not in self.classnames:
                print("** class doesn't exist **")
            else:
                all_instance = storage.all()
                id_formated = "{}.{}".format(class_name, class_id)
                if id_formated not in all_instance:
                    print("** no instance found **")
                else:
                    obj_trgt = all_instance[id_formated]
                    attr_type = type(obj_trgt.__class__.__dict__[attr_name])
                    if attr_name in obj_trgt.__class__.__dict__.keys():
                        obj_trgt.__dict__[attr_name] = attr_type(attr_val)
                    else:
                        obj_trgt.__dict__[attr_name] = attr_val
        elif len(parsed_args) == 3:
            print("** value missing **")
        elif len(parsed_args) == 2:
            print("** attribute name missing **")
        elif len(parsed_args) == 1:
            print("** instance id missing **")

    def do_create(self, args):
        """ Creates a new instance of BaseModel and saves it to JSON file
        Usage: create classname
        """
        parsed_args = args.split()
        if len(parsed_args) == 0:
            print("** class name missing ** ")
        elif parsed_args[0] in self.classnames:
                new_obj = eval(parsed_args[0])()
                print(new_obj.id)
                storage.new(new_obj)
                storage.save()
        elif args not in self.classnames:
            print("** class does'nt exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
