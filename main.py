#WIZARD DUEL!
#Each Wizard has 3 moves, Fireball, Counterspell, or Wizard Slap!
#Fireball is ineffective against itself, Weak to Counterspell, and effective against Wiz Slap!
#Counterspell is effective against Fireball, Ineffective against Counterspell, Weak to SLAP!
#Wizard Slap perishes to fire, is strong against counterspell, and ineffective to SLAP!

PLAYER_DEFAULT_NAME = "Bilbo"
PLAYER_DEFAULT_HEALTH = 5
VERSION = 1

class GameStates:
    START = 0
    P1TURN = 1
    P2TURN = 2
    PLAY = 3
    END = 4


class Wizard:

    def __init__(self, name=PLAYER_DEFAULT_NAME, health=PLAYER_DEFAULT_HEALTH):
        self.name = name
        self.health = health

    def receive_spell_damage(self, spell_damage = 1):
        self.health -= spell_damage

    
def setup():

    print(f"Hello! Welcome to Wizard Duel! V{VERSION}")

    player_name = input("Player 1, Input your name!").strip() or PLAYER_DEFAULT_NAME
    player_1 = Wizard(player_name)

    player_name = input("Player 2, Input your name!").strip() or PLAYER_DEFAULT_NAME
    player_2 = Wizard(player_name)

    print(f"Player 1 name: {player_1.name} Player 2 name: {player_2.name}")
    print(f"Player 1 health: {player_1.health} Player 2 health: {player_2.health}")

    return player_1, player_2

def main():

    Game = GameStates()
    game_state = Game.START

    player_1 = Wizard()
    player_2 = Wizard()

    match game_state:
        case Game.START:
            player_1, player_2 = setup()
            game_state = Game.P1TURN
        case Game.P1TURN:
            game_state = Game.P2TURN
        case Game.P2TURN:
            game_state = Game.PLAY
        case Game.PLAY:
            game_state = Game.END
        case Game.END:
            pass


main()
