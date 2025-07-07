#WIZARD DUEL!
#Each Wizard 

VERSION = 1

class Wizard:

    def __init__(self, name="Wilbo", health=5):
        self.name = name
        self.health = health

    def receive_spell_damage(self, spell_damage = 1):
        self.health -= spell_damage

    
def main():

    print(f"Hello! Welcome to Wizard Duel! V{VERSION}")

    player_name = input("Player 1, Input your name!")
    
    player_1 = Wizard(player_name)

    player_name = input("Player 2, Input your name!")

    player_2 = Wizard(player_name)

    print(f"Player 1 name: {player_1.name} Player 2 name: {player_2.name}")

main()
