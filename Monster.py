

class Monster():
    def __init__(self, hp: int, name: str):
        """instantiate a monster object

        PARAM: self, object instance of the Monster class. name is a string. hp is an int
        PRECONDITION: hp is set to 6. name has to be a string and is automatically set to goblin
        POSTCONDITION: Monster object instantiated
        RETURN: None
        """

        self.type = name
        self.hp = hp
        self.alive = True

    def set_hp(self, new_hp: int)-> None:
        """set hp of monster

        PARAM: self, object instance of the Monster class. new_hp is a int
        PRECONDITION: new_hp is a integer
        POSTCONDITION: self.hp is set to new_hp. if new_hp >= 0 it is set to zero and self.alive
        is set to False
        RETURN: None

        >>> test_monster = Monster(6,"goblin")
        >>> test_monster.set_hp(7)
        >>> test_monster.hp
        7
        >>> test_monster_dead = Monster(6, "goblin")
        >>> test_monster_dead.set_hp(0)
        >>> test_monster_dead.hp
        0
        >>> test_monster_dead.alive
        False
        >>> test_monster_negative_hp = Monster(6, "goblin")
        >>> test_monster_negative_hp.set_hp(-3)
        >>> test_monster_negative_hp.hp
        0
        >>> test_monster_negative_hp.alive
        False

        """
        self.hp = new_hp
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def get_hp(self)-> int:
        """return hp of monster

        PARAM: self, object instance of the Monster class.
        PRECONDITION: None
        POSTCONDITION: None
        RETURN: self.hp as a int

        >>> test_monster = Monster(6, "goblin")
        >>> test_monster.get_hp()
        6
        """
        return self.hp

    def get_alive(self)-> bool:
        """return status of monster

        PARAM: self, object instance of the Monster class.
        PRECONDITION: None
        POSTCONDITION: None
        RETURN: self.alive as a bool

        >>> test_monster = Monster(6, "goblin")
        >>> test_monster.get_alive()
        True
        """
        return self.alive

    def get_type(self)-> str:
        """return type of monster

        PARAM: self, object instance of the Monster class.
        PRECONDITION: None
        POSTCONDITION: None
        RETURN: self.type as a string

        >>> test_monster = Monster(6, "goblin")
        >>> test_monster.get_type()
        'goblin'
        """
        return self.type

    def set_alive(self, dead: bool)->None:
        """ set status of a monster

        PARAM: self, object instance of the Monster class. dead is a bool
        PRECONDITION: dead has to be of type bool
        POSTCONDITION: self.alive is set to dead
        RETURN: None

        >>> test_monster = Monster(6, "goblin")
        >>> dead = False
        >>> test_monster.set_alive(dead)
        >>> test_monster.alive
        False
        """
        self.alive = dead

