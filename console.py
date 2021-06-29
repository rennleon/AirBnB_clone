#!/usr/bin/python3
"""
This module defines 'HBNBCommand' class
"""
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    commnad interpreter that manages the AirBnB objects.
    """

    prompt = '(hbnb) '
    __valid_classes = [
        'BaseModel',
        'User',
        'Place',
        'State',
        'City',
        'Amenity',
        'Review'
    ]
    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def do_create(self, cls):
        """Creates a new instance of BaseModel, saves it to a JSON file
        and prints the 'id'
        """
        if not cls:
            print('** class name missing **')
        elif cls not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        else:
            print((eval(cls)()).id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args_arr = split(arg, posix=False)

        if not arg:
            print('** class name missing **')
        elif args_arr[0] not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args_arr[0], args_arr[1])
            if key not in storage.all():
                print('** no instance found **')
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args_arr = split(arg, posix=False)

        if not arg:
            print('** class name missing **')
        elif args_arr[0] not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args_arr[0], args_arr[1])
            if key not in storage.all():
                print('** no instance found **')
            else:
                storage.all().pop(key)
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        objs_dict = storage.all()

        if arg and arg not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        else:
            objs_list = []
            for obj in objs_dict.values():
                if not arg:
                    objs_list.append(obj.__str__())
                elif type(obj).__name__ == arg:
                    objs_list.append(obj.__str__())
            print(objs_list)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
        by adding or updating an attribute
        Usage: update <class name> <id> <attribute name>
         "<attribute value>" """
        args_arr = split(arg, posix=False)

        if not arg:
            print('** class name missing **')
        elif args_arr[0] not in HBNBCommand.__valid_classes:
            print('** class doesn\'t exist **')
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args_arr[0], args_arr[1])
            if key not in storage.all():
                print('** no instance found **')
            elif len(args_arr) == 2:
                print('** attribute name missing **')
            elif len(args_arr) == 3:
                print('** value missing **')
            else:
                forbiden_update = ['id', 'created_at', 'updated_at']
                if args_arr[2] not in forbiden_update:
                    attr, value = args_arr[2], args_arr[3].replace('"', '')
                    obj = storage.all()[key]
                    if attr in obj.__dict__:
                        value = eval(type(obj.__dict__[attr]).__name__)(value)
                    obj.__setattr__(attr, value)
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
