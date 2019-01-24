

class Map():
    def __init__(self, rows: int, columns: int):
        """instantiate a map object with 5x5 grid

        PARAM: self, object instance of the Map class. rows is a int.
        columns is a  int.
        PRECONDITION: rows and columns have to be positive non-zero ints of the same value
        POSTCONDITION: Map object instantiated
        RETURN: None
        """
        self.rows = rows
        self.columns = columns
        self.grid = [["?" for j in range(rows)] for i in range(columns)]

    def get_rows(self)->int:
        """ get number of rows

        PARAM: self, object instance of the map class
        PRECONDITION: None
        POSTCONDITION: None
        RETURN: self.rows as a positive int.

        >>> test_map =  Map(6, 7)
        >>> test_map.get_rows()
        6
        """
        return self.rows

    def get_columns(self)-> int:
        """ get number of columns

        PARAM: self, object instance of the map class
        PRECONDITION: None
        POSTCONDITION: None
        RETURN: self.columns as a positive int.

        >>> test_map =  Map(6, 7)
        >>> test_map.get_columns()
        7
        """
        return self.columns

    def update_character_position_on_map(self, character_x_position: int, character_y_position: int)->None:
        """ Set character position on map to 'x'

        PARAM: self, object instance of the map class. character_x_position, positive int.
        character_y_position, positive int.
        PRECONDITION: character_y_position and character_x_position are positive ints within the map
        boundaries.
        POSTCONDITION: self.grid[character_y_position][character_x_position] is set to 'x'
        RETURN: None

        >>> test_map = Map(7,7)
        >>> test_map.update_character_position_on_map(0,0)
        >>> test_map.grid[0][0]
        'x'
        """
        self.grid[character_y_position][character_x_position] = 'x'

    def update_character_path_taken(self)->None:
        """ update character path on map with '.'

        PARAM: self, object instance of the map class.
        PRECONDITION: None
        POSTCONDITION: Updated map with the path a character has taken, with current position being 'x'.
        And path taken being '.'
        RETURN: None
        """
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] == "x":
                    self.grid[i][j] = "."

    def display_map(self)->None:
        """ print map to screen

        PARAM: self, object instance of the map class.
        PRECONDITION: None
        POSTCONDITION: Map is printed to screen
        RETURN: None
        """
        for i in range(self.rows):
            for j in range(self.columns):
                print("[", self.grid[i][j], "]", end=" ")

            print("\n")

