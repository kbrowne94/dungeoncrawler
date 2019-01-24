import random


class Die():

    def __init__(self, sides: int, face_value: int):
        """initialize die object"""
        self.sides = sides
        self.face_value = face_value

    def get_number_of_sides(self)-> int:
        """ get number of die sides

        PARAM: self, object instance of the die class
        PRECONDITION: None
        POSTCONDITION: None
        RETURN: self.sides as an int

        >>> test_die = Die(7, 6)
        >>> test_die.get_number_of_sides()
        7
        """
        return self.sides

    def set_number_of_sides(self, number_of_sides: int)->None:
        """ set number of die sides

        PARAM: self, object instance of the die class. number_of_sides is a positive int
        PRECONDITION: number_of_sides is a positive int
        POSTCONDITION: modifies self.sides to number_of_sides
        RETURN: None

        >>> test_die = Die(7, 6)
        >>> test_die.set_number_of_sides(10)
        >>> test_die.sides
        10
        """
        self.sides = number_of_sides

    def get_face_value(self)-> int:
        """ get face value of die

        PARAM: self, object instance of the die class
        PRECONDITION: None
        POSTCONDITION: None
        RETURN: self.sides as a positive int

        >>> test_die = Die(7, 6)
        >>> test_die.get_number_of_sides()
        7
        """
        return self.face_value

    def set_face_value(self, new_value: int)-> None:
        """ set face value of die

        PARAM: self, object instance of the die class. new_value is a positive int
        PRECONDITION: number_of_sides is a positive int
        POSTCONDITION: modifies self.face_value to new_value
        RETURN: None

        >>> test_die = Die(6, 6)
        >>> test_die.set_face_value(10)
        >>> test_die.face_value
        10
        """
        self.face_value = new_value

    def roll_die(self)-> int:
        """ roll die

        PARAM: self, object instance of the die class.
        PRECONDITION: self is properly instantiated
        POSTCONDITION: None
        RETURN: random positive int from 1 to self.sides

        >>> test_die = Die(6, 6)
        >>> test_roll =test_die.roll_die()
        >>> test_roll in range(1,7)
        True
        """
        self.face_value = random.randint(1, self.sides)
        return self.face_value






