import math

class Pokemon:
    def __init__(self, name, type, level=1):
        
        #Constructor

        self.name = name
        self.type = type
        self.level = level
        self.is_knocked_out = False
        self.max_health = 10*(self.level**2)
        self.health = self.max_health
        
        print("New Pokemon: " + name)

    def status(self):

        #Report current Status of Pokemon

        print("")
        print("---------------")
        print(self.name)
        print(" "+ self.type + " Type")
        print(" Level: " + str(self.level))
        if self.is_knocked_out == True:
            print("***KNOCKED OUT***")
        else:            
            print(" Health: " + str(self.health))
        print("")
        print("---------------")
        print("")
        input("Press Enter to continue.")

    def lose_health(self, damage):

        #Method to lower health from Pokemon and check for Knock Out. 
        
        self.health -= damage
        
        print(self.name + " lost " + str(damage) + " health.")
        if self.health < 0:
            print(self.name + " has 0 health left.")
        else:
            print(self.name + " has " + str(self.health) + " health left.")

        if self.health <= 0:
            self.is_knocked_out = True
            print(self.name + " is Knocked Out!")

    def attack(self, target):

        #Method to calculate an attack, the effectiveness based on the Pokemons Type.

        print("")    
        print(self.name + " attacked " + target.name +"!")
        
    
        standard_damage = self.level*3

        super_effective = False
        not_effective = False

        
        #Change to own function/matrix - Especially when more types are added
        if self.type == "Fire":
            if target.type == "Grass":
                super_effective = True
            else:
                not_effective = True
        elif self.type == "Grass":
            if target.type == "Water":
                super_effective = True
            else:
                not_effective = True
        elif self.type == "Water":
            if target.type == "Fire":
                super_effective = True
            else:
                not_effective = True
            

        if super_effective == True :
            standard_damage *= 2
            print("It's Super Effective!")
        elif not_effective == True:
            print("It's not very Effective...")
            standard_damage = math.floor(standard_damage*0.5)

        target.lose_health(standard_damage)
        print("")
        input("Press Enter to continue.")

    def revive(self):

        #Method to Revive a Pokemon when used.
        print("")
        if self.is_knocked_out == False:
            print(self.name + " is not knocked Out, Revive cannot be used")
            
        else: 
            print(self.name + " used Revive!")
            print(self.name + " is no longer Knocked Out.")
            self.is_knocked_out = False
            self.health = self.max_health
            print("")
            input("Press Enter to continue.")

    def heal(self, amount):

        #Method to heal a pokemon, checking that it is not at max health already, and that it cannot go over the maximum.
        print("")
        if self.health == self.max_health:
            print(self.name + " is at maximum health already!")
            return

        self.health += amount

        if self.health > self.max_health:
            self.health = self.max_health
        print(self.name + " was healed for " + str(amount) + ".")
        print(self.name + " has " + str(self.health) + " health left.")
        print("")
        input("Press Enter to continue.")


class Trainer:
    def __init__ (self, trainer):

        #Constructor Method for a new Trainer with name and and generate a blank party.

        self.trainer = trainer
        self.activePokemon = 0
        self.party = []
        self.potions = 2
    
    def party_members (self):

        #Method to return the current party list.
        
        print("")
        print(self.trainer + "'s Pokemon are ")
        i = 0
        for pokemon in self.party:
            print(self.party[i].name)
            i += 1
        
        print("")
        input("Press Enter to continue.")

    def use_potion(self):

        #Method to use a potion, checking if there are any to use and invoking the heal method in Pokemon class

        if self.potions == 0:
            print(self.trainer + " has no Potions Left!")
            return
        else:
            self.party[0].heal(10)
            ash.potions -= 1
     
    def change_active(self, new_active):

        #Method to change active pokemon by name, checking it is not knocked out first.  Index is found then entry is moved to index 0.
        
        if self.party[self.party.index(new_active)].is_knocked_out == True:
            print(self.party[self.party.index(new_active)].name + " is Knocked Out and cannot be switched!")
            return
        else:
            self.party.insert(0, self.party.pop(self.party.index(new_active)))
            print("")
            print(self.party[0].name + " is " + self.trainer + "'s new Active Pokemon")
        
    def attack_trainer(self, opponent):

        #Method to active an attack between trainers by name.  Invokes Attack Method in Pokemon Class.

        print("")
        print(self.trainer + " attacks " + opponent.trainer + "!")
        self.party[0].attack(opponent.party[0])



#Tests/Calls

#Set Up Pokemon
charmander = Pokemon("Charmander", "Fire")
bulbasaur = Pokemon("Bulbasaur", "Grass")
squirtle = Pokemon("Squirtle", "Water")
charmander2 = Pokemon("Charmander", "Fire")

#Set Up Trainers 
ash = Trainer("Ash")
brock = Trainer("Brock")

#Set up and report Parties

ash.party = [charmander, bulbasaur]
brock.party = [squirtle, charmander2]

ash.party_members()
brock.party_members()

#Attack Round 1

ash.attack_trainer(brock)
brock.attack_trainer(ash)

#Attack Round 2

ash.attack_trainer(brock)
brock.attack_trainer(ash)

#Round 3 - Ash Switches, Brock Heals

ash.change_active(bulbasaur)
brock.use_potion()

#Round 4

ash.attack_trainer(brock)
brock.attack_trainer(ash)

#Status Check and Use Revive
ash.party[1].status()
ash.party[1].revive()