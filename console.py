#!/usr/bin/python3
"""this is  Entry point for the command interpreter """
import cmd
from models import storage
import re


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
    
    def do_create(self, opj_name):
        """Creates a new instance of class, saves it
        and prints the id"""
        if opj_name == "":
            print("** class name missing **")
            return
        if opj_name not in storage.classes():
            print("** class doesn't exist **")
            return
        new_obj = storage.classes()[opj_name]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args)!= 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])
    
    def do_destroy(self, line):
        """ destroy object"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args)!= 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
    def do_all(self, line):
        """Prints all string representation of all instance"""
        if line is None or line == "":
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)
        else:
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_list = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == args[0]]
                print(new_list)
    
    def do_update(self, line):
        if line is None or line == "":
            print("** class name missing **")
        
        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        arr = re.search(regex, line)
        cls_name = arr.group(1)
        cls_id = arr.group(2)
        cls_attr = arr.group(3)
        cls_value = arr.group(4)

        if not arr:
            print("** class name missing **")
        elif cls_name not in storage.classes():
            print("** class doesn't exist **")
        elif cls_id is None:
            print("** instance id missing **")
        else:
            key = cls_name + "." + cls_id
            if key not in storage.all():
                print("** no instance found **")
            else:
                if cls_attr is None:
                    print("** attribute name missing **")
                elif cls_value is None:
                    print("** value missing **")
                else:
                    key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', cls_value):
                    if '.' in cls_value:
                        cast = float
                    else:
                        cast = int
                else:
                    cls_value = cls_value.replace('"', '')
                attrs = storage.attributes()[cls_name]
                if cls_attr in attrs:
                    cls_value = attrs[cls_attr](cls_value)
                elif cast:
                    try:
                        cls_value = cast(cls_value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], cls_attr, cls_value)
                storage.all()[key].save()
    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))
    

    list_classes = ['BaseModel', 'User', 'Amenity',
                    'Place', 'City', 'State', 'Review']

    list_cmds = ['create', 'show', 'update', 'all', 'destroy', 'count']
    
    def precmd(self, arg):
        """parses for command inputs"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.list_classes and cnd[0] in HBNBCommand.list_cmds:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg
    
    


if __name__ == "__main__":
    HBNBCommand().cmdloop()
