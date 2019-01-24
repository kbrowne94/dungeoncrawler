
import map
import json
import Character
import Monster
import battle
import random
import doctest


def main():
    doctest.testmod()

    # user prompt whether to make a new character or load game,  if input is not "new" or "load"
    # an error message is printed
    start_screen = True
    while start_screen:
        select = input("new or load?")
        if select == "new" or select == "load":
            start_screen = False
        else:
            print("incorrect selection")

    border_y = 5
    border_x = 5
    game_map = map.Map(border_y, border_x)

    # create a new character
    if select == "new":
        character_name = input("enter your character name:")
        hero = Character.Character(10, character_name)
        game_map.update_character_position_on_map(0, 0)
        game_map.display_map()
    elif select == "load":

        # open a json file to load a character, if no json file is present, prompted to create new character
        try:
            with open("character_data.json") as json_file:
                json_data = json.load(json_file)
                hero = Character.Character(json_data['hp'], json_data['name'])
                hero.set_x_position(json_data['position_x'])
                hero.set_y_position(json_data['position_y'])
                game_map.update_character_position_on_map(hero.get_x_position(), hero.get_y_position())
        except FileNotFoundError:
            character_name = input("no character data was found, enter a name for a new character: ")
            hero = Character.Character(10, character_name)
            game_map.update_character_position_on_map(0, 0)

    play = True
    while play:
        command = input("enter a command, type help for list of commands")
        commands = ['n', 'N', 'e', 'E', 's', 'S', 'w', 'W', 'map', 'q', 'Q', 'help', 'status']

        # check for correct commands
        if command not in commands:
            print("invalid command entered")
        elif command == 'help':
            print("available commands:\nmove: N, E, S, W\ndisplay map: map\n"
                  "quit game: q\ncharacter status: status")

        # if you quit, character is saved to a json file
        elif command == 'q' or command == 'Q':
            character_dict = {'name': hero.get_name(), 'hp': hero.get_hp(), 'position_x': hero.get_x_position(),
                              'position_y': hero.get_y_position()}
            with open('character_data.json', 'w') as outfile:
                json.dump(character_dict, outfile)
            play = False

        # bring up status of your character
        elif command == 'status':
            print("name:", hero.get_name())
            print("hp:", hero.get_hp())

        # bring up game map
        elif command == 'map' or command == 'MAP' or command == 'Map':
            game_map.display_map()

        # entered a movement command
        else:
            hero.move(command, border_x-1, border_y-1)

            # update the map with current position of your character
            game_map.update_character_position_on_map(hero.get_x_position(), hero.get_y_position())

            # chance spawn of an enemy monster when character moves or attempts to move
            # enter a battle phase with monster
            enemy_spawn = random.randint(1, 3)
            if enemy_spawn == 2:
                print("suprise attack from a monster!")
                monster = Monster.Monster(5, "goblin")
                battle.battle(hero, monster)

                if hero.get_alive() is False:
                    print("game over, you died")
                    play = False

                game_map.update_character_path_taken()
                game_map.update_character_position_on_map(hero.get_x_position(), hero.get_y_position())
            else:
                hero.set_hp(hero.get_hp()+1)
                game_map.update_character_path_taken()
                game_map.update_character_position_on_map(hero.get_x_position(), hero.get_y_position())


if __name__ == "__main__":
    main()