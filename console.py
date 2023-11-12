#!/usr/bin/python3
""" A console Module
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ console class
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        exit()

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        exit()

    def emptyline(self):
        """ Does not execute anything
        """
        pass

    def do_create(self, class_name):
        """ Create command creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if len(class_name) == 0:
            print('** class name missing **')
        elif class_name in globals():
            my_class = globals()[class_name]
            obj = my_class()
            obj.save()
            print(obj.id)
        else:
            print("** class doesnt exist **")

    def do_show(self, arg):
        """ Prints string representation of an instance
        """
        if len(arg) == 0:
            print("** class name is missing **")
        else:
            arg_list = arg.split()
            if arg_list[0] in globals():
                obj_class = globals()[arg_list[0]]
                if len(arg_list) < 2:
                    print("** instance id missing **")
                else:
                    obj_id = arg_list[1]
                    dict_key = arg_list[0] + "." + obj_id
                    all_objs = storage.all()
                    if dict_key not in all_objs.keys():
                        print("** no instance found **")
                    else:
                        obj = obj_class(**all_objs[dict_key])
                        print(obj)
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Deletes an instance based on class name and id
        """
        if len(arg) == 0:
            print("** class name is missing **")
        else:
            arg_list = arg.split()
            if arg_list[0] in globals():
                obj_class = globals()[arg_list[0]]
                if len(arg_list) < 2:
                    print("** instance id missing **")
                else:
                    obj_id = arg_list[1]
                    dict_key = arg_list[0] + "." + obj_id
                    all_objs = storage.all()
                    if dict_key not in all_objs.keys():
                        print("** no instance found **")
                    else:
                        obj = obj_class(**all_objs[dict_key])
                        del obj
                        del all_objs[dict_key]
                        storage.__objects = all_objs
                        storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """ Prints all string representation of all instances
        based or not on the class name
        """
        dict_objs = storage.all()
        list_str_repr = []
        match_class = None
        if len(line) != 0:
            if line in globals():
                match_class = line
            else:
                print("**class doesn't exist **")
                return
        for key in dict_objs.keys():
            a_class = key.split(".")[0]
            if match_class is not None:
                if a_class == match_class:
                    obj_class = globals()[match_class]
                else:
                    continue
            else:
                obj_class = globals()[a_class]
            obj = obj_class(**dict_objs[key])
            list_str_repr.append(obj.__str__())
        print(list_str_repr)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
