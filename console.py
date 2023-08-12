#!/usr/bin/python3
'''This module defines the entry point of commmand interpeter'''
import cmd
from models import base_model
import models
from models import user
from models import state
from models import city
from models import place
from models import amenity
from models import review


class HBNBCommand(cmd.Cmd):
    '''This class defines commands for command interpreter
    it iherits Cmd class in cmd module
    '''
    prompt = "(hbnb) "

    def parseline(self, line):
        '''
        Parse the line into a command name and a string
        containing the arguments.
        '''
        if line.endswith(")"):
            class_n, args = line.split(".")
            command, para = args.split("(")
            # nothing in the brackets
            if len(para) == 1:
                line = f'{command} {class_n}'
                return super().parseline(line)
            
            else:
                para = para.strip(")")
                para = para.split(", ")
                
                all_item = []                
                for item in para:
                    if item.startswith('"'):
                        item = item.strip('"')
                    all_item.append(item)
                param = " ".join(all_item)
                line = f'{command} {class_n} {param}'
                return super().parseline(line)

        else:
            return super().parseline(line)

    def do_quit(self, args):
        ''' Quit command to exit the program
        '''
        return True

    def do_EOF(self, args):
        '''Exit the command interpeter by using ctr + D
        '''
        print()
        return True

    def emptyline(self):
        '''when an empty line + Enter exeuted doesnt print any'''
        return False

    def do_create(self, class_n):
        '''Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id '''
        if class_n:
            module = [base_model, user, state, city, amenity, place, review]

            for model_name in module:
                class_name = getattr(model_name, class_n, None)
                if class_name:
                    break

            if class_name is None:
                print("** class doesn't exist **")
            else:
                obj = class_name()
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
            class_n, *para = args.split()
            module = [base_model, user]

            for model_name in module:
                class_name = getattr(model_name, class_n, None)
                if class_name:
                    break

            if class_name is None:
                print("** class doesn't exist **")
            elif not para:
                print("** instance id missing **")
            else:
                key = f"{class_name.__name__}.{para[0]}"
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
            class_n, *para = args.split()
            module = [base_model, user, state, city, amenity, place, review]

            for model_name in module:
                class_name = getattr(model_name, class_n, None)
                if class_name:
                    break

            if class_name is None:
                print("** class doesn't exist **")
            elif not para:
                print("** instance id missing **")
            else:
                key = f"{class_name.__name__}.{para[0]}"
                if key in models.storage.all():
                    obj = models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, args):
        '''
        Prints all string representation of all instances
        based or not on the class name
        '''
        model_list = [base_model, user, state, city, amenity, place, review]

        for model_name in model_list:
            class_name = getattr(model_name, args, None)
            if class_name:
                break

        if class_name is not None:
            all_objs = models.storage.all()
            obj_list = []
            for key in all_objs.keys():
                if class_name and key.startswith(class_name.__name__):
                    obj = all_objs[key]
                    obj_list.append(str(obj))

            print(f'{obj_list}')

        elif len(args) == 0:
            all_objs = models.storage.all()
            obj_list = []
            for key in all_objs.keys():
                obj = all_objs[key]
                obj_list.append(str(obj))
            print(f'{obj_list}')

        else:
            print("** class doesn't exist **")

    def do_count(self, args):
        '''count the number of object in the storage'''
        model_list = [base_model, user, state, city, amenity, place, review]

        for model_name in model_list:
            class_name = getattr(model_name, args, None)
            if class_name:
                break
        count = 0
        if class_name is not None:
            all_objs = models.storage.all()
            count = 0
            for key in all_objs.keys():
                if class_name and key.startswith(class_name.__name__):
                    count += 1

        if len(args) == 0:
            all_objs = models.storage.all()
            for key in all_objs.keys():
                count += 1

        print(count)


    def do_update(self, args):
        '''Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file'''
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_n, *para = args.split()
            module = [base_model, user, state, city, amenity, place, review]

            for model_name in module:
                class_name = getattr(model_name, class_n, None)
                if class_name:
                    break

            if class_name is None:
                print("** class doesn't exist **")
            elif not para:
                print("** instance id missing **")
            else:
                key = f"{class_name.__name__}.{para[0]}"
                if key not in models.storage.all():
                    print("** no instance found **")
                elif len(para) == 1:
                    print("** attribute name missing **")
                elif len(para) == 2:
                    print("** value missing **")
                else:

                    obj = models.storage.all()[key]

                    if hasattr(obj, para[1]):
                        typ = type(getattr(obj, para[1]))
                        value = para[2].strip('"')
                        setattr(obj, para[1], typ(value))
                    else:
                        value = para[2].strip('"')
                        obj.__dict__[para[1]] = value
                    models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
