Airbnb Clone Console Documentation

The document will be based on the tasks 3 to task 10

    Description:

AirBnB is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

    Console:

Its command line interpreter that permits management of the backend of AirBnB. It can be used to handle and manipulate all classes utilized by the application.

Console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.

        Example

$ echo "help" | ./console.py

(airbnb)

Documented commands (type help <topic>):

========================================

EOF  all  count  create  destroy  help  quit  show  update

(airbnb)

$



Alternatively, to use the AirBnB console in interactive mode, run the file console.py by itself:

    ./console.py



While running in interactive mode, the console displays a prompt for input:

    $ ./console.py

(airbnb)



To quit the console, enter the command quit, or input an EOF signal (ctrl-D).

    $ ./console.py

    (airbnb) quit

    $

    $ ./console.py

    (airbnb) EOF

    $


    Console Commands

 The AirBnB console supports the following commands:

    create

Usage: create <class>

Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.

    $ ./console.py
    (airbnb) create BaseModel
    119be863-6fe5-437e-a180-b9892e8746b8
    (airbnb) quit
    $ cat file.json ; echo ""
    {"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2019-02-17T2
    1:30:42.215277", "created_at": "2019-02-17T21:30:42.215277", "__class__": "Base
    Model", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}}


    show

Usage: show <class> <id> or <class>.show(<id>)

Prints the string representation of a class instance based on a given id.

    $ ./console.py
    (airbnb) create User
    1e32232d-5a63-4d92-8092-ac3240b29f46
    (airbnb)
    (airbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
    [User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
    c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828),
    'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
    (airbnb)
    (airbnb) User.show(1e32232d-5a63-4d92-8092-ac3240b29f46)
    [User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
    c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828),
    'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
    (airbnb)


    destroy

Usage: destroy <class> <id> or <class>.destroy(<id>)

Deletes a class instance based on a given id. The storage file file.json is updated accordingly.

    $ ./console.py
    (airbnb) create State
    d2d789cd-7427-4920-aaae-88cbcf8bffe2
    (airbnb) create Place
    3e-8329-4f47-9947-dca80c03d3ed
    (airbnb)
    (airbnb) destroy State d2d789cd-7427-4920-aaae-88cbcf8bffe2
    (airbnb) Place.destroy(03486a3e-8329-4f47-9947-dca80c03d3ed)
    (airbnb) quit
    $ cat file.json ; echo ""
    {}


    all

Usage: all or all <class> or <class>.all()

Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.

    $ ./console.py
    (airbnb) create BaseModel
    fce2124c-8537-489b-956e-22da455cbee8
    (airbnb) create BaseModel
    450490fd-344e-47cf-8342-126244c2ba99
    (airbnb) create User
    b742dbc3-f4bf-425e-b1d4-165f52c6ff81
    (airbnb) create User
    8f2d75c8-fb82-48e1-8ae5-2544c909a9fe
    (airbnb)
    (airbnb) all BaseModel
    ["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.da
    tetime(2019, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2
    , 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[Bas
    eModel] (fce2124c-8537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime
    (2019, 2, 17, 21, 43, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17,
    21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
    (airbnb)
    (airbnb) User.all()
    ["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
    e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
    , 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[User]
    (b742dbc3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2
    , 17, 21, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44,
    15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}"]
    (airbnb)
    (airbnb) all
    ["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
    e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
    , 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[BaseMo
    del] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.datetime(20
    19, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2, 17, 21,
    45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[User] (b742db
    c3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2, 17, 2
    1, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 97
    4608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}", "[BaseModel] (fce2124c-8
    537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2019, 2, 17, 21, 4
    3, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348
    ), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
    (airbnb)


    count

Usage: count <class> or <class>.count()

Retrieves the number of instances of a given class.

    $ ./console.py
    (airbnb) create Place
    12c73223-f3d3-4dec-9629-bd19c8fadd8a
    (airbnb) create Place
    aa229cbb-5b19-4c32-8562-f90a3437d301
    (airbnb) create City
    22a51611-17bd-4d8f-ba1b-3bf07d327208
    (airbnb)
    (airbnb) count Place
    2
    (airbnb) city.count()
    1
    (airbnb)


    update

Usage: update <class> <id> <attribute name> "<attribute value>" or <class>.update(<id>, <attribute name>, <attribute value>) or <class>.update( <id>, <attribute dictionary>).

Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at). However, any attribute can be updated by providing a dictionary.

    $ ./console.py
    (airbnb) create User
    6f348019-0499-420f-8eec-ef0fdc863c02
    (airbnb)
    (airbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton"
    (airbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
    [User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(
    2019, 2, 17, 21, 54, 39, 234382), 'first_name': 'Holberton', 'updated_at': date
    time.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id': '6f348019-0499-420f-8eec-
    ef0fdc863c02'}
    (airbnb)
    (airbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02, address, "98 Mission S
    t")
    (airbnb) User.show(6f348019-0499-420f-8eec-ef0fdc863c02)
    [User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(
    2019, 2, 17, 21, 54, 39, 234382), 'address': '98 Mission St', 'first_name': 'Ho
    lberton', 'updated_at': datetime.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id
    ': '6f348019-0499-420f-8eec-ef0fdc863c02'}
    (airbnb)
    (airbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02, {'email': 'holberton@h
    olberton.com', 'last_name': 'School'})
    [User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'email': 'holberton@holberton.co
    m', 'first_name': 'Holberton', 'updated_at': datetime.datetime(2019, 2, 17, 21,
    54, 39, 234382), 'address': '98 Mission St', 'last_name': 'School', 'id': '6f34
    8019-0499-420f-8eec-ef0fdc863c02', 'created_at': datetime.datetime(2019, 2, 17,
    21, 54, 39, 234382)}
    (airbnb)


    Testing :straight_ruler

Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

    python3 unittest -m discover tests


Alternatively, you can specify a single test file to run at a time:

    python3 unittest -m tests/test_console.py


    Concepts

Python packages

AirBnB clone

0x00. AirBnB clone - The console Docs

By - Florence Rotich and Solomon Bion

    TASKS

3.      BaseModel

Write a class BaseModel that defines all common attributes for other classes:

    models/base_model.py

    Public instance attributes:

        id: string - assign with an uuid when an instance is created:

you can use uuid.uuid4() to generate unique id and  convert to a string

goal is to have unique id for each BaseModel

        created_at: datetime - assign with the current datetime when an instance is created

        updated_at: datetime - assign with the current datetime when an instance is created  it will be updated every time you change your object

        __str__: should print: [<class name>] (<self.id>) <self.**dict**>

    Public instance methods:

            save(self):  it updates the public instance attribute updated_at with the current datetime

            to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:

by using self.__dict__, only instance attributes set will be returned

a key __class__ must be added to this dictionary with the class name of the object

created_at and updated_at must be converted to string object in ISO format:

    format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)

you can use isoformat() of datetime object

This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel


root:~/AirBnB$ cat test_base_model.py
    #!/usr/bin/python3
    from models.base_model import BaseModel

    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    root:~/AirBnB$ ./test_base_model.py
    [BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28,    21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
    [BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
    {'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
    JSON of my_model:
        my_number: (<class 'int'>) - 89
        name: (<class 'str'>) - My First Model
        __class__: (<class 'str'>) - BaseModel
        updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
        id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
        created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

root:~/AirBnB$


    Repo:

GitHub repository: AirBnB_clone

File: models/base_model.py, models/__init__.py, tests/

    Solution

class BaseModel:
    """Represents the BaseModel of the airbnb project."""

    def __init__(self):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)


4.      Create BaseModel from dictionary

Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>



    Update models/base_model.py:

            __init__(self, *args, **kwargs):

you will use *args,**kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)

*args won’t be used

            if kwargs is not empty:

each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)

each value of this dictionary is the value of this attribute name


        otherwise:

create id and created_at as you did previously (new instance)

    example

    :~/AirBnB$ cat test_base_model_dict.py
    #!/usr/bin/python3
    from models.base_model import BaseModel

    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)

    root:~/AirBnB$ ./test_base_model_dict.py
    56d43177-cc5f-4d6c-a0c1-e167f8c27337
    [BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
    <class 'datetime.datetime'>
    --
    {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
    JSON of my_model:
        id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
        created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
        __class__: (<class 'str'>) - BaseModel
        my_number: (<class 'int'>) - 89
        updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
        name: (<class 'str'>) - My_First_Model
    --
    56d43177-cc5f-4d6c-a0c1-e167f8c27337
    [BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
    <class 'datetime.datetime'>
    --
    False
    :~/AirBnB$


    Repo:

GitHub repository: AirBnB_clone

    File: models/base_model.py, tests/

    Solution

    class BaseModel:
        """Represents the BaseModel of the airbnb project."""

    def __init__(self, *args, **kwargs):
            """Initialize a new BaseModel.
            Args:
                *args (any): Unused.
                **kwargs (dict): Key/value pairs of attributes.
            """
            tform = "%Y-%m-%dT%H:%M:%S.%f"
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            if len(kwargs) != 0:
                for k, v in kwargs.items():
                            if k == "created_at" or k == "updated_at":
                        self.__dict__[k] = datetime.strptime(v, tform)
                    else:
                        self.__dict__[k] = v
            else:
                models.storage.new(self)

        def save(self):
            """Update updated_at with the current datetime."""
            self.updated_at = datetime.today()
            models.storage.save()

        def to_dict(self):
            """Return the dictionary of the BaseModel instance.
            Includes the key/value pair __class__ representing
            the class name of the object.
            """
            rdict = self.__dict__.copy()
            rdict["created_at"] = self.created_at.isoformat()
            rdict["updated_at"] = self.updated_at.isoformat()
            rdict["__class__"] = self.__class__.__name__
            return rdict

        def __str__(self):
            """Return the print/str representation of the BaseModel instance."""
            clname = self.__class__.__name__
            return "[{}] ({}) {}".format(clname, self.id, self.__dict__)



5.      Store first object

Recreate a BaseModel from another one by using a dictionary representation:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>


It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:

Python doesn’t know how to convert a string to a dictionary (easily)

 NB= It’s not human readable

Using this file with another program in Python or other language will be hard.

So, convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

flow of serialization-deserialization will be:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>


        Terms:

simple Python data structure: Dictionaries, arrays, number and string. ex: { '12': { 'numbers': [1, 2, 3], 'name': "John" } }

JSON string representation: String representing a simple data structure in JSON format. ex: '{ "12": { "numbers": [1, 2, 3], "name": "John" } }'

Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

    models/engine/file_storage.py

        Private class attributes:

* `__file_path:` string - path to the JSON file (ex: `file.json`)
* `__objects`: dictionary - empty but will store all objects by `<class name>.id` (ex: to store a `BaseModel` object with `id=12121212`, the key will be `BaseModel.12121212`)


        Public instance methods

all(self): returns the dictionary __objects

new(self, obj): sets in __objects the obj with key <obj class name>.id

save(self): serializes __objects to the JSON file (path:__file_path)

reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

Update models/**init**.py: to create a unique FileStorage instance for your application

    import file_storage.py

create the variable storage, an instance of FileStorage

call reload() method on this variable

Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage

    import the variable storage

in the method save(self):

call save(self) method of storage

**init**(self, *args, **kwargs):

if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage

root:~/AirBnB$ cat test_save_reload_base_model.py
    #!/usr/bin/python3
    from models import storage
    from models.base_model import BaseModel

    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)

root:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
root:~/AirBnB$
root:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
root:~/AirBnB$
root:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
root:~/AirBnB$
root:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
root:~/AirBnB$
root:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
root:~/AirBnB$
root:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
root:~/AirBnB$


    Repo:

GitHub repository: AirBnB_clone

File: models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/

    Solution

models/engine/file_storage.py

class FileStorage:
    """ Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return


models/**init**.py

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()


models/base_model.py




6.      Console 0.0.1

Write a program called console.py that contains the entry point of the command interpreter:

You must use the module cmd

Your class definition must be: class airbnbCommand(cmd.Cmd):

Your command interpreter should implement: - quit and EOF to exit the program - help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks) - a custom prompt: (airbnb) - an empty line + ENTER shouldn’t execute anything

Your code should not be executed when imported

Warning:

You should end your file with:

if __name__ == '__main__':
    airbnbCommand().cmdloop()


to make your program executable except when imported. Please don’t add anything around - the Checker won’t like it otherwise

root:~/AirBnB$ ./console.py
(airbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(airbnb)
(airbnb) help quit
Quit command to exit the program

(airbnb)
(airbnb)
(airbnb) quit
root:~/AirBnB$



NO UNITTESTS NEEDED

Repo:

GitHub repository: AirBnB_clone

File: console.py

Solution

console.py File

class airbnbCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(airbnb) "
    __classes = {
        "BaseModel",
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

if __name__ == '__main__':
    airbnbCommand().cmdloop()


7. Console 0.1

Update your command interpreter (console.py) to have these commands:

create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel

If the class name is missing, print **class name missing** (ex: $ create)

If the class name doesn’t exist, print **class doesn't exist** (ex: $ create MyModel)

show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.

If the class name is missing, print **class name missing** (ex: $ show)

If the class name doesn’t exist, print **class doesn't exist** (ex: $ show MyModel)

If the id is missing, print **instance id missing** (ex: $ show BaseModel)

If the instance of the class name doesn’t exist for the id, print **no instance found** (ex: $ show BaseModel 121212)

destroy: Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234. - If the class name is missing, print **class name missing** (ex: $ destroy) - If the class name doesn’t exist, print **class doesn't exist** (ex:$ destroy - MyModel) - If the id is missing, print **instance id missing** (ex: $ destroy BaseModel) - If the instance of the class name doesn’t exist for the id, print **no instance found** (ex: $ destroy BaseModel 121212)

all: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all. - The printed result must be a list of strings (like the example below) - If the class name doesn’t exist, print **class doesn't exist** (ex: $ all MyModel)

update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".

Usage: update <class name> <id> <attribute name> "<attribute value>"

Only one attribute can be updated at the time

You can assume the attribute name is valid (exists for this model)

The attribute value must be casted to the attribute type

If the class name is missing, print **class name missing** (ex: $ update)

If the class name doesn’t exist, print **class doesn't exist** (ex: $ update MyModel)

If the id is missing, print **instance id missing** (ex: $ update BaseModel)

If the instance of the class name doesn’t exist for the id, print **no instance found** (ex: $ update BaseModel 121212)

If the attribute name is missing, print **attribute name missing** (ex: $ update BaseModel existing-id)

If the value for the attribute name doesn’t exist, print **value missing** (ex: $ update BaseModel existing-id first_name)

All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")

id, created_at and updated_at can't be updated. You can assume they won’t be passed in the update command

Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime

Let’s add some rules:

You can assume arguments are always in the right order

Each arguments are separated by a space

A string argument with a space must be between double quote

The error management starts from the first argument to the last one

root:~/AirBnB$ ./console.py
(airbnb) all MyModel
** class doesn't exist **
(airbnb) show BaseModel
** instance id missing **
(airbnb) show BaseModel My_First_Model
** no instance found **
(airbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(airbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(airbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(airbnb) destroy
** class name missing **
(airbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(airbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(airbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(airbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(airbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(airbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(airbnb)


Repo:

GitHub repository: AirBnB_clone

File: console.py

Solution

console.py File

def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in airbnbCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in airbnbCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in airbnbCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in airbnbCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in airbnbCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False


8.      First User

Write a class User that inherits from BaseModel:

models/user.py

    Public class attributes:

email: string - empty string

password: string - empty string

first_name: string - empty string

last_name: string - empty string

Update FileStorage to manage correctly serialization and deserialization of User.

Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User.

root:~/AirBnB$ cat test_save_reload_user.py
    #!/usr/bin/python3
    from models import storage
    from models.base_model import BaseModel
    from models.user import User

    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new User --")
    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Bar"
    my_user.email = "airbnb@mail.com"
    my_user.password = "root"
    my_user.save()
    print(my_user)

    print("-- Create a new User 2 --")
    my_user2 = User()
    my_user2.first_name = "John"
    my_user2.email = "airbnb2@mail.com"
    my_user2.password = "root"
    my_user2.save()
    print(my_user2)

root:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049"}}
root:~/AirBnB$
root:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
-- Create a new User --
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@mail.com', 'first_name': 'Betty', 'last_name': 'Bar', 'password': 'root'}
-- Create a new User 2 --
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'email': 'airbnb2@mail.com', 'first_name': 'John', 'password': 'root'}
root:~/AirBnB$
root:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at": "2017-09-28T21:11:42.848279", "updated_at": "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", "first_name": "Betty", "__class__": "User", "last_name": "Bar", "password": "root"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"id": "d0ef8146-4664-4de5-8e89-096d667b728e", "created_at": "2017-09-28T21:11:42.848280", "updated_at": "2017-09-28T21:11:42.848294", "email": "airbnb_2@mail.com", "first_name": "John", "__class__": "User", "password": "root"}}
root:~/AirBnB$
root:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544), 'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862), 'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058), 'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296), 'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287)}
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347), 'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337)}
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'last_name': 'Bar', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'first_name': 'Betty'}
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'first_name': 'John'}
-- Create a new User --
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'last_name': 'Bar', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'first_name': 'Betty'}
-- Create a new User 2 --
[User] (fce12f8a-fdb6-439a-afe8-2881754de71c) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611354), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611368), 'id': 'fce12f8a-fdb6-439a-afe8-2881754de71c', 'first_name': 'John'}
root:~/AirBnB$
root:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"updated_at": "2017-09-28T21:11:12.971544", "__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "created_at": "2017-09-28T21:11:12.971521"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848279", "email": "airbnb@mail.com", "id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "last_name": "Bar", "updated_at": "2017-09-28T21:11:42.848291", "first_name": "Betty", "__class__": "User"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848280", "email": "airbnb_2@mail.com", "id": "d0ef8146-4664-4de5-8e89-096d667b728e", "updated_at": "2017-09-28T21:11:42.848294", "first_name": "John", "__class__": "User"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"updated_at": "2017-09-28T21:11:14.963058", "__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "created_at": "2017-09-28T21:11:14.963049"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"updated_at": "2017-09-28T21:11:15.504296", "__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"updated_at": "2017-09-28T21:11:13.753347", "__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"updated_at": "2017-09-28T21:11:14.333862", "__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "created_at": "2017-09-28T21:11:14.333852"}, "User.246c227a-d5c1-403d-9bc7-6a47bb9f0f68": {"password": "root", "created_at": "2017-09-28T21:12:19.611352", "email": "airbnb@mail.com", "id": "246c227a-d5c1-403d-9bc7-6a47bb9f0f68", "last_name": "Bar", "updated_at": "2017-09-28T21:12:19.611363", "first_name": "Betty", "__class__": "User"}, "User.fce12f8a-fdb6-439a-afe8-2881754de71c": {"password": "root", "created_at": "2017-09-28T21:12:19.611354", "email": "airbnb_2@mail.com", "id": "fce12f8a-fdb6-439a-afe8-2881754de71c", "updated_at": "2017-09-28T21:12:19.611368", "first_name": "John", "__class__": "User"}}
root:~/AirBnB$


No unittests needed for the console

Repo:

GitHub repository: AirBnB_clone

File: console.py

    Solution

models/user.py

    #!/usr/bin/python3
    """This module creates a User class, Defines the User class."""
    from models.base_model import BaseModel


    class User(BaseModel):
        """Class for managing user objects
        Represent a User.
        Attributes:
            email (str): the email of the user.
            password (str): The password of the user.
            first_name (str): The first name of the user.
            last_name (str): the last name of the user.
        """

    email = ""
    password = ""
    first_name = ""
    last_name = ""


models/engine/file_storage.py

from models.user import User


    console.py

class airbnbCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(airbnb) "
    __classes = {
        "BaseModel",
        "User"
    }


9.      More classes

Write all those classes that inherit from BaseModel:

State (models/state.py):

Public class attributes:

name: string - empty string

City (models/city.py):

Public class attributes:

state_id: string - empty string: it will be the State.id

name: string - empty string

Amenity (models/amenity.py):

Public class attributes:

name: string - empty string

Place (models/place.py):

Public class attributes:

city_id: string - empty string: it will be the City.id

user_id: string - empty string: it will be the User.id

name: string - empty string

description: string - empty string

number_rooms: integer - 0

number_bathrooms: integer - 0

max_guest: integer - 0

price_by_night: integer - 0

latitude: float - 0.0

longitude: float - 0.0

amenity_ids: list of string - empty list: it will be the list of Amenity.id later

Review (models/review.py):

Public class attributes:

place_id: string - empty string: it will be the Place.id

user_id: string - empty string: it will be the User.id

text: string - empty string

Repo:

GitHub repository: AirBnB_clone

File: console.py

    Solution

        models/state.py

    #!/usr/bin/python3
    """This module creates a User class, Defines the State class."""
    from models.base_model import BaseModel


    class State(BaseModel):

        """Class for managing state objects
        Represent a state.
        Attributes:
            name (str): The name of the state.
        """

        name = ""


models/city.py

    #!/usr/bin/python3
    """This module creates a City class"""
    from models.base_model import BaseModel


    class City(BaseModel):
        """Class for managing city objects
        Represent a city.
        Attributes:
            state_id (str): the state id.
            name (str): The name of the city.
        """
        state_id = ""
        name = ""


models/amenity.py

    #!/usr/bin/python3
    """This module creates the Amenity class"""
    from models.base_model import BaseModel


    class Amenity(BaseModel):
        """Class for managing amenity objects
        Represent an amenity.
        Attributes:
        name (str): The name of the amenity.
        """
        name = ""


models/place.py

#!/usr/bin/python3
"""This module creates a Place class,Defines the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):

    """Class for managing place objects
    Represent a place.
    Attributes:
        city_id (str): The City id.
        user_id (str): theUser id.
        name (str): The name of the place.
        description (str): the description of the place.
        number_rooms (int): the number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by nght of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []


models/review.py

#!/usr/bin/python3
"""This module creates a Review class, Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):

    """Class for managing review objects
    Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): the User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
