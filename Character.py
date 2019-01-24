

class Character():

    def __init__(self, hp: int, name: str):
        """instantiate a Character object with 10 hp at position 0,0 on a map

        PARAM: self, object instance of the Character class. name is a string. hp is an int
        PRECONDITION: hp is set to 10. name has to be a string
        POSTCONDITION: Character object instantiated
        RETURN: None
        """
        self.name = name
        self.hp = hp
        self.alive = True
        self.x_position = 0
        self.y_position = 0

    def set_name(self, new_name: str)-> None:
        """set status of a monster

        PARAM: self, object instance of the Character class. new_name is a string
        PRECONDITION: new_name is a none-empty string
        POSTCONDITION: self.name is set to new name
        RETURN: None

        >>> test_character = Character(10, "Kyle")
        >>> test_character.set_name("Keelay")
        >>> test_character.name
        'Keelay'
        """
        self.name = new_name

    def set_hp(self, new_hp: int)-> None:
        """set status of a monster

        PARAM: self, object instance of the Character class. new_hp is an int
        PRECONDITION: new_hp is a integer
        POSTCONDITION: self.name is set to new_hp. if new_hp >= 0 it is set to zero and self.alive
        is set to False
        RETURN: None

        >>> test_character = Character(10,"Kyle")
        >>> test_character.set_hp(7)
        >>> test_character.hp
        7
        >>> test_character_dead = Character(6, "goblin")
        >>> test_character_dead.set_hp(0)
        >>> test_character_dead.hp
        0
        >>> test_character_dead.alive
        False
        >>> test_character_negative_hp = Character(6, "goblin")
        >>> test_character_negative_hp.set_hp(-3)
        >>> test_character_negative_hp.hp
        0
        >>> test_character_negative_hp.alive
        False
        """
        self.hp = new_hp
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        if self.hp > 10:
            self.hp = 10

    def get_name(self)-> str:
        """return name of character

        PARAM: self, object instance of the Character class.
        PRECONDITION: None
        POSTCONDITION: None
        RETURN: self.name as a string

        >>> test_character = Character(10, "Kyle")
        >>> test_character.get_name()
        'Kyle'
        """
        return self.name


    def get_hp(self)-> int:
        """return hp of character

        PARAM: self, object instance of the Character class.
        PRECONDITION: None
        POSTCONDITION: None
        RETURN: self.hp as a int

        >>> test_character = Character(10, "Kyle")
        >>> test_character.get_hp()
        10
        """
        return self.hp

    def get_x_position(self)-> int:
        """return x position of character

        PARAM: self, object instance of the Character class.
        PRECONDITION: self.x_position has to be within the map
        POSTCONDITION: None
        RETURN: self.x_position as a int

        >>> test_character = Character(10, "Kyle")
        >>> test_character.get_x_position()
        0
        """
        return self.x_position

    def get_y_position(self)-> int:
        """return y position of character

        PARAM: self, object instance of the Character class.
        PRECONDITION: self.y_position has to be within the map
        POSTCONDITION: None
        RETURN: self.y_position as a int

        >>> test_character = Character(10, "Kyle")
        >>> test_character.get_y_position()
        0
        """
        return self.y_position

    def set_x_position(self, new_x_position)-> None:
        """set x position of character

        PARAM: self, object instance of the Character class. new_x_position, positive int
        PRECONDITION: new_x_position is a positive int within map boundaries
        POSTCONDITION: self.x_position is set to new_x_position
        RETURN: None

        >>> test_character = Character(10, "Kyle")
        >>> test_character.set_x_position(1)
        >>> test_character.x_position
        1
        """
        self.x_position = new_x_position

    def set_y_position(self, new_y_position)-> None:
        """set y position of character

        PARAM: self, object instance of the Character class. new_y_position, positive int
        PRECONDITION: new_y_position is a positive int within map boundaries
        POSTCONDITION: self.y_position is set to new_y_position
        RETURN: None

        >>> test_character = Character(10, "Kyle")
        >>> test_character.set_y_position(1)
        >>> test_character.y_position
        1
        """
        self.y_position = new_y_position

    def get_alive(self)-> bool:
        """return status of character

        PARAM: self, object instance of the Character class.
        PRECONDITION: None
        POSTCONDITION: None
        RETURN: self.alive as a bool

        >>> test_character = Character(10, "Kyle")
        >>> test_character.get_alive()
        True
        """
        return self.alive

    def set_alive(self, dead: bool)-> None:
        """ set status of a monster

        PARAM: self, object instance of the Character class. dead is a bool
        PRECONDITION: dead has to be of type bool
        POSTCONDITION: self.alive is set to dead
        RETURN: None

        >>> test_character = Character(6, "kyle")
        >>> dead = False
        >>> test_character.set_alive(dead)
        >>> test_character.alive
        False
        """

        self.alive = False

    def move(self, move: str, x_boundary: int, y_boundary: int)-> None:
        if move == 'N' or move == 'n':
            if self.y_position > 0:
                self.y_position -= 1
                print("you moved north")
            else:
                print("you cant go that way you'll be off the map!")

        if move == 'S' or move == 's':
            if self.y_position < y_boundary:
                self.y_position += 1
                print("you moved south")
            else:
                print("you cant go that way you'll be off the map!")

        if move == 'E' or move == 'e':
            if self.x_position < x_boundary:
                self.x_position += 1
                print("you moved east")
            else:
                print("you cant go that way you'll be off the map!")

        if move == 'W' or move == 'w':
            if self.x_position > 0:
                self.x_position -= 1
                print("you moved west")
            else:
                print("you cant go that way you'll be off the map!")
