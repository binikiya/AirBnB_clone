# Project Description
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…


# The hbnb commandline Interpreter
The command line interpreter helps you to create, read, update and delete these data models listed below
All these models are subclasses of the BaseModel class

```
-User
-City
-Amenity
-Place
-Review
-State
```

## How to start it
In order to start the console, you run the following command in your terminal

```
$ python ./console.py
(hbnb) $
```

## How to use it
| Command | Description | Syntax |Advanced |
|---------|-------------|---------|---------|
| `create` | Create a new instance of a model | `create <model> <attribute> <value>` |`None`|
| `show` | Show all instances of a model | `show <model>` |`<model>.show(<id>)`|
| `destroy` | Destroy an instance of a model | `destroy <model> <id>` |`<model>.destroy(<id>)`|
| `update` | Update an instance of a model | `update <model> <id> <attribute> <value>` |`<model>.update(<id>, <args> or <dict>)`|
| `all` | Show all instances of a model | `all <model>` |`<model>.all()`|
| `count` | Count all instances of a model | `count <model>` |`<model>.count()`|

# Examples
### Create a User
```
(hbnb) $ create User
850df2af-2e6f-4a42-b0f4-4715535e8471
(hbnb) $
```
### Show a user
```
(hbnb) $ show User 850df2af-2e6f-4a42-b0f4-4715535e8471
[User] (850df2af-2e6f-4a42-b0f4-4715535e8471) {'id': '850df2af-2e6f-4a42-b0f4-4715535e8471', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685854), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685854)}
```

### Update a user
```
(hbnb) $ update User 850df2af-2e6f-4a42-b0f4-4715535e8471 first_name Ikenga
(hbnb) $ show User 850df2af-2e6f-4a42-b0f4-4715535e8471
[User] (850df2af-2e6f-4a42-b0f4-4715535e8471) {'id': '850df2af-2e6f-4a42-b0f4-4715535e8471', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685854), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685854), 'first_name': 'Ikenga'}

(hbnb) $ User.update(850df2af-2e6f-4a42-b0f4-4715535e8471, "first_name", "esther")
(hbnb) show User 850df2af-2e6f-4a42-b0f4-4715535e8471
[User] (850df2af-2e6f-4a42-b0f4-4715535e8471) {'id': '850df2af-2e6f-4a42-b0f4-4715535e8471', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685854), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685854), 'first_name': 'esther'}

(hbnb) User.update(850df2af-2e6f-4a42-b0f4-4715535e8471, {"first_name":"eve"})
(hbnb) show User 850df2af-2e6f-4a42-b0f4-4715535e8471
[User] (850df2af-2e6f-4a42-b0f4-4715535e8471) {'id': '850df2af-2e6f-4a42-b0f4-4715535e8471', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685854), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685854), 'first_name': 'eve'}
```

### Count Users
```
(hbnb) $ count User
27
(hbnb) $
(hbnb) $ User.count()
(hbnb) $ count User
27
```

### Display models
You can also make use of User.all()
To display all models use all
```
(hbnb) $ all User
["[User] (7e1242ac-6a4e-41b7-aebb-94c7ec3c85b4) {'id': '7e1242ac-6a4e-41b7-aebb-94c7ec3c85b4', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685663), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685663)}", "[User] (a6925c8d-61b8-4f73-85ed-f8a9525c1770) {'id': 'a6925c8d-61b8-4f73-85ed-f8a9525c1770', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685727), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685727)}", "[User] (cfa5f2d3-f14a-4068-a7ab-41d237978d85) {'id': 'cfa5f2d3-f14a-4068-a7ab-41d237978d85', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685791), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685791)}", "[User] (850df2af-2e6f-4a42-b0f4-4715535e8471) {'id': '850df2af-2e6f-4a42-b0f4-4715535e8471', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685854), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 685854), 'first_name': 'eve'}", "[User] (123456) {'id': '123456', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688420), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688420)}", "[User] (5bc28f55-79a7-434d-9a62-82687412cacf) {'id': '5bc28f55-79a7-434d-9a62-82687412cacf', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 686003), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 33, 686003)}", "[User] (316c1fd2-70ee-48ae-b469-7ef79d78a47b) {'id': '316c1fd2-70ee-48ae-b469-7ef79d78a47b', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 186595), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 186595)}", "[User] (309b6603-9fad-4d6e-8f21-31409b63d434) {'id': '309b6603-9fad-4d6e-8f21-31409b63d434', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 186758), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 186758)}", "[User] (7d3882b2-fa0c-41c5-8662-74dda58ad6d8) {'id': '7d3882b2-fa0c-41c5-8662-74dda58ad6d8', 'created_at': datetime.datetime(2021, 11, 16, 
1, 9, 34, 687349), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 687349)}", "[User] (05660a07-3a26-40b6-a0a1-9d56c35a5e7c) {'id': '05660a07-3a26-40b6-a0a1-9d56c35a5e7c', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 687697), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 687697)}", "[User] (8c931c0e-cf67-4894-84a7-ef748720fed8) {'id': '8c931c0e-cf67-4894-84a7-ef748720fed8', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 687784), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 687784)}", "[User] (2030f856-c370-4612-ae52-2d5cc8e6916e) {'id': '2030f856-c370-4612-ae52-2d5cc8e6916e', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 687932), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 687932)}", "[User] (2e6a73c8-7575-48fb-8d45-fd36213662c5) {'id': '2e6a73c8-7575-48fb-8d45-fd36213662c5', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 687948), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 687948)}", "[User] (1d73ca95-c7d7-46a3-b1ea-f3f196068d78) {'id': '1d73ca95-c7d7-46a3-b1ea-f3f196068d78', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688013), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688013)}", "[User] (bbe3feab-26a4-4bd5-9394-b7c5cad5f603) {'id': 'bbe3feab-26a4-4bd5-9394-b7c5cad5f603', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688114), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688114)}", "[User] (475eb638-d848-4391-9ec8-f74d1d998b0d) {'id': '475eb638-d848-4391-9ec8-f74d1d998b0d', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688194), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688194), 'middle_name': 'ALX', 'my_number': 88}", "[User] (9321f7ef-7ab7-4044-b0a2-5140c4f54e4c) {'id': '9321f7ef-7ab7-4044-b0a2-5140c4f54e4c', 'created_at': datetime.datetime(2021, 11, 16, 1, 
9, 34, 688276), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688276)}", "[User] (e8dc8e8f-b6c2-4c50-aaab-4bab0e1b248f) {'id': 'e8dc8e8f-b6c2-4c50-aaab-4bab0e1b248f', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688356), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688356)}", "[User] (a374e979-52d3-4bd4-a745-0975fb4d2ea5) {'id': 'a374e979-52d3-4bd4-a745-0975fb4d2ea5', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688514), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688514)}", "[User] (db05aec2-260a-45aa-9ddc-d3c4cbdb6ea1) {'id': 'db05aec2-260a-45aa-9ddc-d3c4cbdb6ea1', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688534), 'updated_at': datetime.datetime(2021, 11, 16, 
1, 9, 34, 688534)}", "[User] (d7a3eddc-5003-487c-98f2-a47ab9f8b7da) {'id': 'd7a3eddc-5003-487c-98f2-a47ab9f8b7da', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688603), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 688603)}", "[User] (25de1bea-933d-428b-93e0-1003c73c6c38) {'id': '25de1bea-933d-428b-93e0-1003c73c6c38', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 34, 689110), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 35, 189653)}", "[User] (ca798972-8253-4f00-afac-3511a9d48ddd) {'id': 'ca798972-8253-4f00-afac-3511a9d48ddd', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 35, 191121), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 35, 191134)}", "[User] (590ce838-8db7-45b9-85f9-188784254ab7) {'id': '590ce838-8db7-45b9-85f9-188784254ab7', 'created_at': datetime.datetime(2021, 11, 16, 1, 9, 35, 192919), 'updated_at': datetime.datetime(2021, 11, 16, 1, 9, 36, 195322)}"]
```

### Destroy a user
```
(hbnb) $ destroy User 850df2af-2e6f-4a42-b0f4-4715535e8471
(hbnb) $
(hbnb) $ show User 850df2af-2e6f-4a42-b0f4-4715535e8471
** no instance found **
```


## Authors
* **Biniyam Tamene** <[binikiya](https://github.com/binikiya)>
* **Elijah Daniel** <[elijahdanie](https://github.com/elijahdanie)>