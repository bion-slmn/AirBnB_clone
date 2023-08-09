#!/usr/bin/python3
'''This module defines the entry point of commmand interpeter'''
import cmd
from models import base_model
import models


class HBNBCommand(cmd.Cmd):
    '''This class defines commands for command interpreter
    it iherits Cmd class in cmd module
    '''
    prompt = "(hbnb) "

    def do_quit(self, args):
        ''' Quit command to exit the program
        '''
        return True

    def do_EOF(self, args):
        '''Exit the command interpeter by using ctr + D
        '''
        print()
        return True

    def do_create(self, class_name):
        '''Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id '''
        if class_name:
            class_ = getattr(base_model, class_name, "name")

            if class_ == "name":
                print("** class doesn't exist **")
            else:
                obj = class_()
                obj.save()
                print(f'{obj.id}')
        else:
            print("** class name missing **")

    def do_show(self, args):
        '''Prints the string representation of an instance based on
        the class name and id'''
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name, *para = args.split()
            class_ = getattr(base_model, class_name, "name")

            if class_ == "name":
                print("** class doesn't exist **")
            elif not para:
                print("** instance id missing **")
            else:
                key = f"{class_.__name__}.{para[0]}"
                if key in models.storage.all():
                    obj = models.storage.all()[key]
                    print(obj)
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id and
        save the change into the JSON file.'''
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name, *para = args.split()
            class_ = getattr(base_model, class_name, "name")

            if class_ == "name":
                print("** class doesn't exist **")
            elif not para:
                print("** instance id missing **")
            else:
                key = f"{class_.__name__}.{para[0]}"
                if key in models.storage.all():
                    obj = models.storage.all().pop(key)
                    model.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, args):
        '''Prints all string representation of all instances
        based or not on the class name'''
        comma = False
        class_name = getattr(base_model, args, "name")
        if class_name != "name" or len(args) == 0:
            all_objs = models.storage.all()
            print("[", end="")
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if comma:
                    print(", ", end="")
                print(f'\"{obj}\"', end="")
                comma = True
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        '''Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file'''
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name, *para = args.split()
            class_ = getattr(base_model, class_name, "name")

            if class_ == "name":
                print("** class doesn't exist **")
            elif not para:
                print("** instance id missing **")
            else:
                key = f"{class_.__name__}.{para[0]}"
                if key not in models.storage.all():
                    print("** no instance found **")
                elif len(para) == 1:
                    print("** attribute name missing **")
                elif len(para) == 2:
                    print("** value missing **")
                else:
                    obj = models.storage.all()[key]
                    if hasattr(obj, para[1]):
                        attr_value = obj.para[1]
                        typ = type(attr_value)
                        setattr(obj, para[1], typ(para[2]))
                    else:
                        setattr(obj, para[1], para[2])
                    models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
