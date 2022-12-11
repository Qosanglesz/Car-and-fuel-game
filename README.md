# Car and fuel game
## OVERVIEW
Concept of this game is to control a-car in X-axis(left or right) on the road and get fuel to increase score. while the car is running. The player must avoid an object such as a road hole, car and dog. a player will have 5 hearts if their hearts decrease to zero.the game will be over.


## Required libraries and tools
- Coding on python V. 3.10
- Python turtle graphic
- random, os and Colection

## File and class description

### 1.GameObject class (GameObject.py)
This class is an inheritance from Turtle.Superclass of all objects in the game that can move. Have 3 attributes is shape, color, position  
**method**  
- **Collide(other)**: check collide

### 2.Car class (Car.py)
This class is a subclass of Gameobject but add more attribute are score: int, heart: int  
**method**  
- **control_left()**: move car to left  
- **control_right()**: move car to right  
- **decrease_hearts(damage)**: decrease car hearts with damage  
- **increase_score()**: increase score when car collide with fuel  

### 3.Fuel class (Fuel.py)
This class is a subclass of Gameobject too.  
**method**  
- **move()**:  move in direction (-y axis)  

### 4.AvoidObject class (AvoidObject.py)  
This class is a subclass of Gameobject too.look like fuel class  
**method**  
- **move()**:  move in direction (-y axis)  

### (5 to 7).Dog, Truck, Hole: class (AvoidObject.py)  
These Classes are subclass of AvoidObject class. I make it a subclass because it is simple and formal to read.  
and an important attribute for this game is damage: int.  

### 8.Screen class (screen.py)  
This class objective is make a screen  
**method**  
- **__init__()** : make a screen with (600 x 600) size. and background picture  

### 9.Road class (road.py)  
This class objective is operation all in screen without previous   
move objects such as show score, show heart, write road border  
with Height and Width, game over screen and top 3 score board  
**method**  
- **make()**: writer parallel road border with 400 length  
- **game_over(obj)**: show game over screen with current score of player name.  
- **see_score(obj) :** show score of player update real time on screen top left.  
- **see_heart(obj)**: show hearts of player update real time on screen top right.  
- **score_board(data_dict)**: show top 3 player scoreboard.  
data_dict input from DatabaseGame method  

### 10.DatabaseGame class (DatabaseGame.py)  
This class objective is save game (score and player name)  
in “Database.json” in format of dictionary type.  
two important of this class is player_name and score  
**method**  
- **write_database()**: Create new “Database.json” and write a save game if there is no file. if not just write only.  
- **sorted_score()**: @staticmethod  
return sorted score of player high to low  

### 11.main.py  
This file use all class and file to make a real game  
