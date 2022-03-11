# Airbnb Clone

## General

This project is the first step of the AirBnB clone project. So it's a FullStack project.

With Mickael we create the command interpreter to manage the AirBnB objects.

In first, we implement the BaseModel object. This object define all others object of our project.

In second time, we create the command interpreter. We see how to use it and all exemple for used it under the General section.

And in last, we define all others objects(User, State, Place...), that inherits from BaseModel.

## The command interpreter

To start the command interpreter, you need python3 and you should use in a terminal:
> ./console.py

Example of first use:

    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  create  destroy  help  quit  show  update all

    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $

### Command description

* help
    - Display the documented command.

            (hbnb) help

            Documented commands (type help <topic>):
            ========================================
            EOF  create  destroy  help  quit  show  update all
    - Used in association with a command that display how to use the command.

            (hbnb) help quit
            Quit command to exit the program

* create
    - Creates a new instance of object passes in parameter and save it to a JSON file.

            (hbnb) create User
            e0d60b67-1ba9-4d3f-a336-b239b96a85c5
            (hbnb) 

* show
    - Display the string represantation of an instance based on the class name and id.

            (hbnb) show User e0d60b67-1ba9-4d3f-a336-b239b96a85c5
            [User] (e0d60b67-1ba9-4d3f-a336-b239b96a85c5) {'id': 'e0d60b67-1ba9-4d3f-a336-b239b96a85c5', 'created_at': datetime.datetime(2022, 3, 2, 14, 59, 10, 44658), 'updated_at': datetime.datetime(2022, 3, 2, 14, 59, 10, 44719)}
            (hbnb) 

    - Other example for using 'show' command, \<class name\>.show(\<id\>):
            
            (hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
            [User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
            (hbnb) User.show("Bar")
            ** no instance found **
            (hbnb) 

* all
    - Display all string representation of all instances based or not on the class name.

            (hbnb) all BaseModel
            []
            (hbnb) all Mymodel
            ** class doesn't exist **
            (hbnb) all User
            ["[User] (92cfa8a5-4664-4108-bce9-bb2e2e7f22a2) {'id': '92cfa8a5-4664-4108-bce9-bb2e2e7f22a2', 'created_at': datetime.datetime(2022, 3, 2, 15, 5, 53, 836486), 'updated_at': datetime.datetime(2022, 3, 2, 15, 5, 53, 836673)}"]
            (hbnb) 

    - Other example for using 'all' command, \<class name\>.all():

            (hbnb) User.all()
            [[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
            (hbnb)
 
* update
    - Updated an instance based on the class name and id by adding or updated attribute (save the change into the JSON file)

            (hbnb) update User 92cfa8a5-4664-4108-bce9-bb2e2e7f22a2 first_name "Jean"
            (hbnb) show User 92cfa8a5-4664-4108-bce9-bb2e2e7f22a2
            [User] (92cfa8a5-4664-4108-bce9-bb2e2e7f22a2) {'id': '92cfa8a5-4664-4108-bce9-bb2e2e7f22a2', 'created_at': datetime.datetime(2022, 3, 2, 15, 5, 53, 836486), 'updated_at': datetime.datetime(2022, 3, 2, 15, 5, 53, 836673), 'first_name': '"Jean"'}
            (hbnb) 

    - Other example for using 'update' command, \<class name\>.update(\<id\>, \<attribute name\>, \<attribute value\>)
            
            (hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
            [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
            (hbnb)
            (hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
            (hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
            (hbnb)
            (hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
            [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
            (hbnb) 

    - Third exemple for using 'update' command, \<class name\>.update(\<id\>, \<dictionary representation\>):

            (hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
            [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 23, 'first_name': 'Bob', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
            (hbnb) 
            (hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
            (hbnb) 
            (hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
            [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
            (hbnb) 

* destroy
    - Deletes an instance based on the class name and id (save the change into the JSON file).

            (hbnb) destroy User 92cfa8a5-4664-4108-bce9-bb2e2e7f22a2
            (hbnb) show User 92cfa8a5-4664-4108-bce9-bb2e2e7f22a2
            ** no instance found **
            (hbnb)

    - Other example for using 'destroy' command, \<class name\>.destroy(\<id\>):

            (hbnb) User.count()
            2
            (hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
            (hbnb) User.count()
            1
            (hbnb) User.destroy("Bar")
            ** no instance found **
            (hbnb)

* count
    - Retrieve the number of instances of a class \<class name\>.count():

            (hbnb) User.count()
            2
            (hbnb) 

## The web static

This is the first version of the front-end web page. Each file until the 103-index.html are prototypes. The last one, 103-index.html, is the final version, responsive and also treat the accessibility.
There are no comminication between the console and the web yet.