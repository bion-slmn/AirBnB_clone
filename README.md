This project is about Writing the storage engine for Airbnb web platform, it uses files mainly
basically it involves about writing a class and storing it in a file as a json and then converting back to Class

Like in the example below
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>

This project aslo involves writing a console which resemble shell in C. but with our own commands for testing our code

This main in volves using the cmd module.
the console works both interactively and in non interactive mode

Tho start the console in interctive mode simply run the file containng the code like in the example
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 

(hbnb) is the prompt

Non-interactive mode
echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
