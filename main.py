#WIZARD DUEL!
#Each Wizard has 4 moves, Fireball, Counterspell, Nap, or Slap!
#Fireball is ineffective against itself, Weak to Counterspell, and effective against Slap!
#Counterspell is effective against Fireball, Ineffective against Counterspell, Weak to SLAP!
#Slap perishes to fire, is strong against counterspell, and ineffective to SLAP!
#Nap does nothing, This move is weak to both Fireball and SLAP! But gains you 1 HP
#I hope I dont drop this :') TEST!

PLAYER_DEFAULT_NAME = "Bilbo"
PLAYER_DEFAULT_HEALTH = 5
PLAYER_DEFAULT_COUNT = 2

VERSION = 1

Moveset = ["Fireball", 
           "Counterspell", 
           "Slap!", 
           "Nap"]

class Wizard:

    move = "Nap"
    target = "Bilbo"

    def __init__(self, 
                 number,
                 name=PLAYER_DEFAULT_NAME, 
                 health=PLAYER_DEFAULT_HEALTH):

        self.__number = number
        self.name = name
        self.health = health

    def get_number(self):
        return self.__number

    def receive_spell_damage(self, 
                             spell_damage = 1):

        self.health -= spell_damage


def setup():

    print(f"Hello! Welcome to Wizard Duel! V{VERSION}")
    player_count = int(input("How many wizards are dueling? ").strip() or PLAYER_DEFAULT_COUNT)

    player_list = []

    for i in range(player_count):

        player_number = i + 1
        player_name = input(f"Player {player_number}, Input your name! ").strip() or PLAYER_DEFAULT_NAME
        player = Wizard(player_number, player_name)
        player_list.append(player)

    return player_count, player_list

def print_players(player_list):

    for player in player_list:
        print(f"{player.name}, Player {player.get_number()}")

def prep_phase(player_list):

    for player in player_list:

        waiting_for_move = True #Start the prep turn by correctly waiting for a move

        while(waiting_for_move):

            player_move = input(f"Player {player.get_number()}, {player.name}, What's your move? ").strip()

            if player_move:
                for move in Moveset:
                    if player_move.lower() in move.lower():
                        if input(f"You chose {move}, is this correct? (y/n) ") == "y":
                            player.move = move
                            waiting_for_move = False
            else: #Move not entered, empty input
                print(f"Hey, {player.name}, you have to do SOMETHING!")

        waiting_for_target = True

        while(waiting_for_target):

            if (player.move == "Fireball" or player.move == "Slap!"): 
                print("\n---List of targets---")
                for target in player_list:
                    if target.name is player.name:
                        pass
                    else:
                        print(f"Player {target.get_number()}, {target.name}")

                player_target = input(f"\nPlayer {player.get_number()}, {player.name}, Who do you want to use {player.move} on? ").strip()
                if player_target:
                    for target in player_list:
                        if player_target.lower() in target.name.lower():
                            if input(f"You chose Player {target.get_number()}, {target.name}, is this correct? (y/n) ") == "y":
                                player.target = target.name
                                waiting_for_target = False
                else:
                    print(f"Are you sure that's one of the Wizards here?")

            else:
                player.target = player.name
                waiting_for_target = False

        print(f"Player {player.name} is using {player.move} on {player.target}")


def main():

    player_count, player_list = setup()
    print_players(player_list)

    game_state = "PREPARE"
    
    match game_state:
        case "PREPARE":
            prep_phase(player_list)
            game_state = "FIGHT"
        case "FIGHT":
            game_state = "END TURN"
        case "END TURN":
            game_state = "RESULT"
        case "RESULT":
            pass

main()
