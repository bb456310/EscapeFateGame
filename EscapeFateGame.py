import random
game_name = """
                EEEEE  SSS   CCC    A   PPPP  EEEEE    FFFFF   A   TTTTT EEEEE
                E     S   S C   C  A A  P   P E        F      A A    T   E    
                E      S    C     A   A P  P  E        F     A   A   T   E    
                EEEEE   S   C     AAAAA PPP   EEEEE    FFFF  AAAAA   T   EEEEE
                E        S  C     A   A P     E        F     A   A   T   E    
                E     S   S C   C A   A P     E        F     A   A   T   E    
                EEEEE  SSS   CCC  A   A P     EEEEE    F     A   A   T   EEEEE
"""

game_over = """
                 GGG    A   M   M EEEEE     OOO  V   V EEEEE RRRR 
                G      A A  MM MM E        O   O V   V E     R   R 
                G     A   A MM MM E        O   O V   V E     R  R  
                G  GG AAAAA M M M EEEEE    O   O V   V EEEEE RRR   
                G   G A   A M   M E        O   O V   V E     R R   
                G   G A   A M   M E        O   O  V V  E     R  R  
                 GGG  A   A M   M EEEEE     OOO    V   EEEEE R   R"""
print(game_name)

##############################################################################################################
### Character class info here

class Character:
    def __init__(self, name, xp, has_sword = False, has_armor = False, level = 1):
        self.name = name
        self.level = level
        self.health = self.level * 5
        self.max_health = self.level * 5
        self.has_sword = has_sword
        self.has_armor = has_armor
        self.xp = xp
        self.is_dead = False
        self.num_potions = 0
        self.inventory = []

    def __repr__(self):
        return_phrase1 = ""
        if self.name == "Anton":
            print("Anton, the Ukrainian, is built like a brick wall. He uses brute strength to punish his foes. ")
        if self.name == "Gustav":
            print("Gustav is a fighting member of the Swedish Resistance. He tears through his foes with a swift blade. ")
        if self.name == "Chet":
            print("Chet is a red-blooded American. He plays to win, no holds barred. ")
        return_phrase1 += "{name} is a level {level} warrior, with {hp} out of {max_hp} health remaining.".format(name=self.name, level=self.level, hp=self.health, max_hp=self.max_health)
        return return_phrase1

    def die(self):
        self.is_dead = True
        if self.health != 0:
            self.health = 0
        print("{name} has fallen in combat. Fate has won again!".format(name=self.name))
        print(game_over)
        quit()

    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.die()
        else:
            print("{name} now has {health} health remaining.".format(name=self.name, health=self.health))
    
    def gain_health(self, amount):
        if (self.health + amount) > self.max_health:
            self.health = self.max_health
            print("{name} now has {health} health remaining.".format(name=self.name, health=self.health))
            print("{name} is at full health! Go get 'em!".format(name=self.name))
        else:
            self.health += amount
            print("{name} now has {health} health remaining.".format(name=self.name, health=self.health))
    
    def attack(self, enemy_char):
        if self.has_sword == True and enemy_char.has_armor == False:
            print("\n{my_name} has attacked {enemy_name} for {damage} damage!".format(my_name=self.name, enemy_name=enemy_char.name, damage=round(self.level * 2)))
            print("{name}'s sword did exceptional damage against the armorless foe!".format(name=self.name))
            enemy_char.lose_health(round(self.level * 2))
        if self.has_sword == True and enemy_char.has_armor == True:
            print("\n{my_name} has attacked {enemy_name} for {damage} damage!".format(my_name=self.name, enemy_name=enemy_char.name, damage=round(self.level)))
            print("{name}'s sword damaged the foe's armor!".format(name=self.name))
            enemy_char.lose_health(round(self.level))
            enemy_char.has_armor = False
        if self.has_sword == False and enemy_char.has_armor == True:
            print("\n{my_name} has attacked {enemy_name} for {damage} damage!".format(my_name=self.name, enemy_name=enemy_char.name, damage=round(self.level * .5)))
            print("{name}'s bare fists do little damage to the foe's armor.".format(name=self.name))
            enemy_char.lose_health(round(self.level * .5))
        if self.has_sword == False and enemy_char.has_armor == False:
            print("\n{my_name} has attacked {enemy_name} for {damage} damage!".format(my_name=self.name, enemy_name=enemy_char.name, damage=round(self.level * 2)))
            print("The unarmored foe is beaten by {name}'s bare fists.".format(name=self.name))
            enemy_char.lose_health(round(self.level * 2))
        if enemy_char.is_dead == True:
            self.level_up()
            self.xp += 10

    def level_up(self):
        self.level += 1
        print("\n{name} has levelled up! \nHe is now level {level}.".format(name=self.name, level = self.level))
        self.max_health = self.level * 6
        self.health += 4
        print("{name} feels stronger and slightly rejuvenated!".format(name=self.name))
    
    def use_potion(self):
        if self.num_potions <=0:
            print("\nYou have no potions remaining!")
        else:
            self.gain_health(5)
            self.num_potions -= 1

###need to change use potion to use item from inventory <<<< only if more items are added
    
    def use_item(self, Item):
        if Item == "Longsword" and "Longsword" in self.inventory:
           self.has_sword = True
        if Item == "Shield" and "Shield" in self.inventory:
            self.has_armor = True
        if Item == "Potion" and self.num_potions > 0:
            self.use_potion
        if Item == "Magic Mushroom" and "Magic Mushroom" in self.inventory:
            self.level_up
    
    def run(self):
        print("\n{name} bolts from the battle.".format(name=self.name))
        print("His cowardice serves him little, as he trips upon an upturned root. \nHis head finds a jutting stone, which puts him out of his misery. \n {name}'s corpse rots away forever in this Hell.".format(name=self.name))
        print(game_over)
        quit()

    def defend(self, enemy_char):
        enemy_char.strength -= 1
        print("\n{name} braces himself for the upcoming enemy blow!".format(name=self.name))

    def loot_chest(self):
        loot = random.choices(item_list, weights=(3,5,1,3), k=1)
        if loot == ["Potion"]:
            self.num_potions += 1
            print("\nInside is a potion!")
        if loot == ["Longsword"]:
            self.has_sword = True
            self.inventory += "Longsword"
            print("\nInside is a Longsword!")
        if loot == ["Shield"]:
            self.has_armor = True
            self.inventory += "Shield"
            print("\nInside is a Shield!")
        if loot == ["Magic Mushroom"]:
            self.inventory += "Magic Mushroom"
            print("\nInside is a Mysterious Magic Mushroom!")
            shroom_choice = input("Does {name} eat the Mushroom?".format(name=self.name))
            shroom_choice = shroom_choice.lower()
            if shroom_choice == "yes":
                print("\n{name} suddenly feels much stronger!".format(name=self.name))
                self.level_up
            else:
                pass
        print("{name} recovers the loot from the locked chest!".format(name=self.name))

    def spring_trap(self):
        traps = ["False Floor", "Trip Wire", "Poison Darts"]
        trap_choice = random.choice(traps)
        if trap_choice == "False Floor":
            print("\n{name} stumbles across a False Floor, dropping down into hidden spikes below!".format(name=self.name))
        if trap_choice == "Trip Wire":
            print("\n{name} feels his foot catch on a Trip Wire. Suddenly his world is red as a fiery explosion engulfs his body!".format(name=self.name))
        if trap_choice == "Poison Darts":
            print("\n{name} steps cautiously across the floor - but not cautiously enough! A pressure plate triggers a barrage of Poison Darts!".format(name=self.name))
        damage = random.randint(1, 6)
        print("{name} loses {dmg} health.".format(name=character_select.name, dmg=damage))
        self.lose_health(damage)


##############################################################################################################
### Enemies class info here
        
class Enemy:
    def __init__(self, name, hp, has_armor, has_sword, strength = 2):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.is_dead = False
        self.has_armor = has_armor
        self.has_sword = has_sword
        

    def __repr__(self):
        return_phrase = "A {name} stands in the way of the exit and must be vanquished!".format(name=self.name)
        if self.has_armor == True:
            return_phrase += " The {name} is donned in armor. Strike wisely.".format(name=self.name)
        if self.has_sword == True:
            return_phrase += " The {name} wields a longsword. Be ware!".format(name=self.name)
        return return_phrase
        
    def die(self):
        self.is_dead = True
        if self.hp != 0:
            self.hp = 0
        print("{name} has been vanquished. On to your next foe!".format(name=self.name))

    def lose_health(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.die()
        else:
            print("{name} now has {health} health remaining. Fight on!".format(name=self.name, health=self.hp))
    
    def attack(self, user_char):
        if self.hp <= 0:
            return
        if self.has_sword == True and user_char.has_armor == False:
            print("The enemy slashes you with its longsword!")
            print("A {enemy_name} has attacked {user_name} for {damage} damage!".format(enemy_name=self.name, user_name=user_char.name, damage=round(self.strength * 2)))
            user_char.lose_health(round(self.strength * 2))
        if self.has_sword == True and user_char.has_armor == True:
            print("The enemy slashes you with its longsword, but your armor protects you!")
            print("A {enemy_name} has attacked {user_name} for {damage} damage!".format(enemy_name=self.name, user_name=user_char.name, damage=round(self.strength)))
            user_char.lose_health(round(self.strength))
        if self.has_sword == False and user_char.has_armor == False:
            print("The enemy claws at your flesh!")
            print("A {enemy_name} has attacked {user_name} for {damage} damage!".format(enemy_name=self.name, user_name=user_char.name, damage=round(self.strength)))
            user_char.lose_health(round(self.strength))
        if self.has_sword == False and user_char.has_armor == True:
            print("The enemy flails at you, but your armor protects you!")
            print("A {enemy_name} has attacked {user_name} for {damage} damage!".format(enemy_name=self.name, user_name=user_char.name, damage=round(self.strength * .5)))
            user_char.lose_health(round(self.strength * .5))



##############################################################################################################
### Items class info here
            
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return_phrase2 = "The {name} you found ".format(name=self.name)
        if self.name == "Longsword":
            return_phrase2 += "grants you additional attack power!"
        if self.name == "Shield":
            return_phrase2 += "provides defensive protection!"
        if self.name == "Potion":
            return_phrase2 += "heals your wounds!"
        if self.name == "Magic Mushroom":
            return_phrase2 += "provides ultimate power!!"
        return return_phrase2
    
    def has_sword(self, user_char):
        user_char.has_sword == True

    def use_potion(self, user_char):
        user_char.use_potion

    def level_up(self, user_char):
        user_char.level_up

    def has_armor(self, user_char):
        user_char.has_armor    

##############################################################################################################
### starting Characters
        
ant = Character("Anton", 0, False, False, 2)
gus = Character("Gustav", 0, True, False, 1)
chet = Character("Chet", 0, False, True, 1)
god = Character("Matt Damon", 1000, True, True, 100)

##############################################################################################################
### starting Enemies

skel = Enemy("Skeleton", 5, False, False, 1)
black = Enemy("Black Knight", 10, True, True, 4)
band = Enemy("Bandit", 5, False, True, 2)
giant = Enemy("Gargantuan Zombie", 15, False, True, 6)
drag = Enemy("Dragon", 40, True, False, 10)
gard = Enemy("Armored Armory Guard", 12, True, True, 5)
band2 = Enemy("Bandit", 5, False, True, 2)
skel2 = Enemy("Skeleton", 5, False, False, 1)
black2 = Enemy("Black Knight", 10, True, True, 4)
black3 = Enemy("Black Knight", 10, True, True, 4)
black4 = Enemy("Black Knight", 10, True, True, 4)
gard2 = Enemy("Armored Armory Guard", 12, True, True, 5)

##############################################################################################################
### different Items

sword = Item("Longsword")
pot = Item("Potion")
shroom = Item("Magic Mushroom")
shield = Item("Shield")

##############################################################################################################
### other variables?

item_list = ["Longsword", "Potion", "Magic Mushroom", "Shield"]
kill_count = 0
def trap_chance():
    trap_chance = random.randint(1,10)
    if trap_chance > 6:
        character_select.spring_trap()

##############################################################################################################
### Character select    

character_select = input("SELECT YOUR PLAYER: \n ANTON \t\t\t GUSTAV \t\t CHET")
character_select = character_select.lower()
while character_select != "anton" and character_select != "gustav" and character_select != "chet" and character_select != "god":
    character_select = input("You have not chosen your fate. Select 'Anton', 'Gustav', or 'Chet' to continue.")
    character_select = character_select.lower()

if character_select == "anton":
    character_select = ant
if character_select == "gustav":
    character_select = gus
if character_select == "chet":
    character_select = chet
if character_select == "god":
    character_select = god

print("You have chosen {name}.".format(name=character_select.name))
print(character_select)

##############################################################################################################
### intro

print("""\n\n\n\n\n\n\n\n\n\n\n\n ...{name} awakes, alone, in a dark room. 
      \nStripped of his belongings, he finds himself in some sort of jail or dungeon.
      \nYou must decide what to do, where to go. You must Escape Fate!""".format(name=character_select.name))
begin = input("Ready to begin?")
begin = begin.lower()
while begin != "yes":
    begin = input("Tarry Not! Fate waits for no man!\nStart the adventure?")
    begin = begin.lower()
if begin == "yes":
    print("\n{name} looks around the cell.".format(name=character_select.name))
if character_select == gus:
    print("Gustav searches the room and finds a lone dead skeleton in the corner, wielding a small sword.")
    wield_sword_choice = input("Does Gustav wield the skeleton's sword?")
    wield_sword_choice = wield_sword_choice.lower()
    if wield_sword_choice == "no":
        character_select.has_sword = False
    else:
        character_select.has_sword = True
if character_select == chet:
    print("Chet searches the room and finds a lone dead skeleton in the corner. On the skeleton is some worn chain mail.")
    don_armor_choice = input("Does Chet don the armor?")
    don_armor_choice = don_armor_choice.lower()
    if don_armor_choice == "no":
        character_select.has_armor = False
    else:
        character_select.has_armor = True
if character_select == ant:
    print("Anton glances around his surroundings for anything useful. Alas,")

##############################################################################################################
### first branch    
room_choice = input("\nThere's nothing more in this room. It's time to move on.\nThere are seemingly two exits: through the broken cell door, or through a large crevice in the back of the wall. \nWhich do you take: Door or Crevice?")
room_choice = room_choice.lower()
while room_choice != "door" and room_choice != "crevice":
    room_choice = input("That is not a viable option. Choose 'door' or 'crevice' to continue.")
    room_choice = room_choice.lower()
if room_choice == "door":
    print("\n{name} makes his way over to the cell door. The broken door appears to be stuck.".format(name=character_select.name))
    break_choice = input("Do you attempt to break through?")
    break_choice = break_choice.lower()
    if break_choice == "yes":
        print("\nThe door easily gives and falls to the side. {name} steps through, making his way into the next room.".format(name=character_select.name))
        investigate_choice = input("\nThe room is dark, but there is a closed chest in the corner.\nInvestigate? or Move On?")
        investigate_choice = investigate_choice.lower()
        if investigate_choice == "investigate":
            print("\nMoving toward the chest, he sees there is a lock, but it appears to be broken.")
            character_select.spring_trap()
            print("The chest was trapped all along! Proceed with extra caution moving forward!")
            character_select.loot_chest
            input("Ready to move onward?")
            print("\n{name} moves forward, to the other side of the room.".format(name=character_select.name))
        if investigate_choice == "move on":
            print("\nAvoiding the questionable chest, {name} sneaks toward the other side of the room.".format(name=character_select.name))
    if break_choice == "no":
        print("\nDeciding against the door, he moves back to look for the other exit.")
        room_choice = "crevice"
if room_choice == "crevice":
    print("\n{name} makes his way over to the crevice in the wall. \nIt's easy enough to climb through to the other side.".format(name=character_select.name))
    print("As he stumbles through to the adjacent room, a strange clattering immediately pulls his attention.")
    print("\nAn animated Skeleton turns and charges the direction of {name}!".format(name=character_select.name))
    print(skel)
    while skel.hp > 0:
        fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
        fight_choice = fight_choice.lower()
        while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
            fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
            fight_choice = fight_choice.lower()
        if fight_choice == "attack":
            character_select.attack(skel)
        if fight_choice == "use potion":
            character_select.use_potion()
        if fight_choice == "defend":
            character_select.defend(skel)
        if fight_choice == "run":
            character_select.run()
        skel.attack(character_select)
    else:
        kill_count += 1
        print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
        print("Vanquishing the enemy, {name} plunders the room for a boon.".format(name=character_select.name))
        print("A small chest hides lies behind the once again lifeless skeleton.")
        character_select.loot_chest

##############################################################################################################
### second branch
            
print("Across the dungeon room, he spots another door - this one chained shut.")
door_choice = input("There's no other way moving forward, {name} must decide what to do.\nPick Lock or Break Chains?".format(name=character_select.name))
door_choice = door_choice.lower()
while door_choice != "pick lock" and door_choice !="break chains":
    door_choice = input("\nYou have not chosen 'Pick Lock' or 'Break Chains'. Please choose your fate.")
    door_choice = door_choice.lower()
if door_choice == "pick lock":
    print("\nFinding a small shiv on the floor, he uses the scrap to move the locking mechanism around until a quiet 'click' loosens the locked chains.\nDeftly, {name} steps through the entrance.".format(name=character_select.name))
if door_choice == "break chains":
    print("\nUsing naught but sheer strength and will, he charges the wooden door. \nHis shoulder finds contact with wood and the chained door bursts into splinters and scrap.")
    print("Though the door gives, it splinters away, stabbing {name}'s side. \n{name} takes 1 damage.".format(name=character_select.name))
    character_select.lose_health(1)
    print("{name} is through to the next room - but the crash has attracted some unwanted attention... \nA Bandit, waiting around the corner, springs forth to attack!".format(name=character_select.name))
    print(band)
    while band.hp > 0:
        fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
        fight_choice = fight_choice.lower()
        while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
            fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
            fight_choice = fight_choice.lower()
        if fight_choice == "attack":
            character_select.attack(band)
        if fight_choice == "use potion":
            character_select.use_potion()
        if fight_choice == "defend":
            character_select.defend(band)
        if fight_choice == "run":
            character_select.run()
        band.attack(character_select)
    else:
        kill_count += 1
        print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
        equip_sword_choice = input("The Bandit's corpse lies on the ground, sword fallen by his side.\nPick up the weapon?")
        equip_sword_choice = equip_sword_choice.lower()
        if equip_sword_choice == "yes":
            character_select.has_sword = True
            print("\nThe sword feels heavy in your hand, and gleams in the little light there is in the room.")
        if equip_sword_choice == "no":
            print("\nNot trusting the blade, it is left lying beside its stricken owner.")
            print("{name} strides past his fallen foe into the next room.".format(name=character_select.name))
continue_choice = input("Stepping into the dimly lit chamber, he notices an accumulation of junk around the room. Ready to move forward?")
continue_choice = continue_choice.lower()
while continue_choice != "yes":
    input("\nThere is no rest in this place. Move on?")
    continue_choice = "yes"
if continue_choice == "yes":
    print("\n{name} makes his way through the room, climbing over heaps of crates and abandoned boxes.".format(name=character_select.name)) 
    trap_chance()
print("There seems to be two further exits:\nAnother wooden door, unbarred. And a decrepit archway, with vines twisting around and among the pillars.")
door_choice = input("Which exit does {name} take? Door or Arch?".format(name=character_select.name))
door_choice = door_choice.lower()
while door_choice != "door" and door_choice != "arch":
    door_choice = input("\nYou have chosen unwisely. Select 'door' or 'arch'.")
    door_choice = door_choice.lower()
if door_choice == "door":
    booty_choice = input("\nPeaking inside the door, he clearly sees a large chest sitting in the corner of the room.\nPlunder the newly found booty?")
    booty_choice = booty_choice.lower()
    while booty_choice != "yes" and booty_choice != "no":
        booty_choice = input("\nIs he looting the chest?")
        booty_choice = booty_choice.lower()
    if booty_choice == "yes":
        character_select.loot_chest()
        trap_chance()
        print("After looting the chest, {name} is ready to move forward.".format(name=character_select.name))
        ready_choice = input("Are you?")
        ready_choice = ready_choice.lower()
        while ready_choice != "yes":
            print("It matters not! Forward is the only option!")
        else:
            print("And forward he goes...")
    if booty_choice == "no":
        print("\nNot trusting the gilded chest, he leaves the room behind, still searching for a way through.")
if door_choice == "arch":
    print("\nThe arch, overgrown with foliage, promises some sort of pathway to the outside world. \nHowever, after moving into the room, {name} can only see shafts of moonlight splaying through the open ceiling, some 30 feet above.".format(name=character_select.name))
    print("Suddenly, a pair of bright eyes appears out of the darkness! \n\nA swift flash and the moonlight is gleaming off a long, broad sword. \nA Knight, clad in darkness stands before you!")
    print(black)
    while black.hp > 0:
        fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
        fight_choice = fight_choice.lower()
        while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
            fight_choice = input("You did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
            fight_choice = fight_choice.lower()
        if fight_choice == "attack":
            character_select.attack(black)
        if fight_choice == "use potion":
            character_select.use_potion()
        if fight_choice == "defend":
            character_select.defend(black)
        if fight_choice == "run":
            character_select.run()
        black.attack(character_select)
    else:
        kill_count += 1
        print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
        print("{name} stands over the knight's body. His armor may be donned, and his longsword equipped.".format(name=character_select.name))
        don_armor_choice = input("Take armor?")
        don_armor_choice = don_armor_choice.lower()
        if don_armor_choice == "yes":
            character_select.has_armor = True
        equip_sword_choice = input("\nTake sword?")
        equip_sword_choice = equip_sword_choice.lower()
        if equip_sword_choice == "yes":
            character_select.has_sword = True
    print("\nSlaying another foe, {name} grows a taste for the action. He leaves the room behind, in search of more.".format(name=character_select.name))

##############################################################################################################
### third branch

print("\nFrom one dark, damp room into another, {name} takes his time sneaking down a long corridor. \nWhat little light there is comes from failing distant sconces.".format(name=character_select.name))
go_choice = input("Ready to move forward?")
go_choice = go_choice.lower()
while go_choice != "yes":
    go_choice = input("{name} finds no rest in this place. Move on?".format(name=character_select.name))
    go_choice = go_choice.lower()
if go_choice == "yes":
    print("Following the hallway, he takes a turn and is suddenly faced with two ornate doors, one on either side of the hall. \n\nThe door on the left is almost glowing red. There is a small engraving across the top, in an unknown script. \nThe door on the right is blacker than night, and almost seems to suck the light itself in. \nMeanwhile, the path forward seems to lie clear.")
path_choice = input("Which way calls forth? Left, Right, or Forward?")
path_choice = path_choice.lower()
while path_choice != "left" and path_choice != "right" and path_choice != "forward":
    path_choice = input("\nChoose again: left, right, or forward.")
    path_choice = path_choice.lower()
if path_choice == "left":
    print("\nThis door glows with some power unknown.")
    print("There appears to be no handle. Throwing a shoulder into the door does nothing.")
    door_choice = input("{name} feels the need to place his hand against the engraving. Touch it? or Walk away?".format(name=character_select.name))
    door_choice = door_choice.lower()
    while door_choice != "touch it" and door_choice != "walk away" and door_choice != "touch":
        door_choice = input("\nChoose to: Touch It or Walk Away.")
        door_choice = door_choice.lower()
    if door_choice == "touch it" or door_choice == "touch":
        print("\nPressing a hand across the foreign words, {name} feels a warmth surrounding his body. He can't read the words, but he knows what they say. \nThis path is a test. \nIn order to pass through, the correct answer must be given, or dire consequences will fall upon the entrant.".format(name=character_select.name))
        print("Removing the hand from the now hot stone is suddenly impossible. An answer is needed.")
        print("Words swarm round the head of {name} in his native tongue. They speak of challengers who falter and fail. Of mysteries and riddles. Of Answers. \nIn order to move forward, he must answer this riddle:".format(name=character_select.name))
        print("\n\nI have cities, but no houses. I have mountains, but no trees. I have water, but no fish.")
        answer = input("What Am I?")
        answer = answer.lower()
        while answer != "a map":
            print("\nA shock of pain rips through your body, from your fingertips all the way through your toes.")
            character_select.lose_health(5)
            answer = input("You have chosen unwisely. What Am I?")
            answer = answer.lower()
        if answer == "a map" or answer == "map" or answer == "map." or answer == "a map.":
            print("\nA warmth covers {name}'s body, starting from his hand. His vision melts away, and he soon finds himself in a whole new room. \nIt's warm, and bright, and much cleaner than any room encountered thus far. Though there is still but one door ahead.".format(name=character_select.name))
            character_select.level_up()
            character_select.gain_health(10)
            print("\nFeeling rejuvenated, he springs to the door and flings it wide. \nFinally, there is a glimpse of the outside world - moonlight flooding in through the high windows, that spills across a large sarcophagus in the middle of the room. \nIt stands between you and the next door.\n")
            print("Taking cautious steps toward the only exit, {name} finds himself right beside the large sarcophagus before a small quake sends him to his knees.".format(name=character_select.name))
            print("A booming crack splits the crypt in two, and a huge creature begins to emerge from beneath the rubble.")
            print(giant)
            while giant.hp > 0:
                fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
                fight_choice = fight_choice.lower()
                while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
                    fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
                    fight_choice = fight_choice.lower()
                if fight_choice == "attack":
                        character_select.attack(giant)
                if fight_choice == "use potion":
                        character_select.use_potion()
                if fight_choice == "defend":
                        character_select.defend(giant)
                if fight_choice == "run":
                        character_select.run()
                giant.attack(character_select)
            else:
                kill_count += 1
                print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
                print("The giant's lifeless corpse is sprawled across the floor. The path forward appears to be clear.")
                print("Tearing open the door, another long, doorless corridor stares back.")
    if door_choice == "walk away":
        print("\nFearing what danger the door possesses, he turns back to the long corridor.")
if path_choice == "right":
    print("\nThe lifeless void of a door stares back as {name} studies the path to the right. \nThe right decision must be made. He reaches out to open what must surely be the exit.".format(name=character_select.name))
    print("As soon as his hand wraps around the door's handle, {name} loses all sense of direction as his world spins and twists into oblivion. \n All goes black for a moment.... \n\n\n\nAnd then, looking around himself, {name} sees he's not alone. Far from it.".format(name=character_select.name))
    print(skel2)
    print(band2)
    print(black2)
    while skel2.hp > 0:
        fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
        fight_choice = fight_choice.lower()
        while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
            fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
            fight_choice = fight_choice.lower()
        if fight_choice == "attack":
            character_select.attack(skel2)
        if fight_choice == "use potion":
            character_select.use_potion()
        if fight_choice == "defend":
            character_select.defend(skel2)
        if fight_choice == "run":
            character_select.run()
        skel2.attack(character_select)
    else:
        kill_count += 1
        print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
        print("The Skeleton has fallen, but the bandit now takes his place, rushing at you sword first!")
    while band2.hp > 0:
        fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
        fight_choice = fight_choice.lower()
        while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
            fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
            fight_choice = fight_choice.lower()
        if fight_choice == "attack":
            character_select.attack(band2)
        if fight_choice == "use potion":
            character_select.use_potion()
        if fight_choice == "defend":
            character_select.defend(band2)
        if fight_choice == "run":
            character_select.run()
        band2.attack(character_select)
    else:
        kill_count += 1
        print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
        print("He's taken down the Bandit as well! But the Knight is there to bar the path.")
    while black2.hp > 0:
        fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
        fight_choice = fight_choice.lower()
        while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
            fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
            fight_choice = fight_choice.lower()
        if fight_choice == "attack":
            character_select.attack(black2)
        if fight_choice == "use potion":
            character_select.use_potion()
        if fight_choice == "defend":
            character_select.defend(black2)
        if fight_choice == "run":
            character_select.run()
        black2.attack(character_select)
    else:
        kill_count += 1
        print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
    print("Bloodied and beaten, {name} steps over his fallen foes and heads down the adjoining hallway, eager to find his way out of this hell.".format(name=character_select.name))
if path_choice == "forward":
    print("\nNot wanting to stray from the straight path, {name} ignores the two doors and heads down the long, empty corridor.".format(name=character_select.name))

##############################################################################################################
### fourth branch

print("The empty hall stretches out, curving away to the left beyond sight. There's only the one way forward. \nHe can sneak down the hallway slowly and carefully, or bound forward to quickly get out of here.")
speed_choice = input("Should he Sneak or Hurry?")
speed_choice = speed_choice.lower()
while speed_choice != "sneak" and speed_choice != "hurry":
    speed_choice = input("\nYou did not choose 'Sneak' or 'Hurry'.")
    speed_choice = speed_choice.lower()
if speed_choice == "sneak":
    print("\nTaking his time to avoid any more potential traps or snags, {name} glides across the space deftly and with care. \n However, taking his time seems to have its drawbacks. {name} hears something clanging faintly behind as he slowly moves down the hall.".format(name=character_select.name))
    speed_choice2 = input("Hearing the noise behind, should he move faster or continue along? Select 'Faster' or 'Continue'.")
    speed_choice2 = speed_choice2.lower()
    if speed_choice2 == "faster":
        print("\nHe takes the necessary risk and pushes forward with a burst of speed.")
        trap_chance
    if speed_choice2 == "continue":
        print("\nAlmost to the other side, the faint clanging has turned to solid footsteps. They're not far behind, but the end of the hall is still a piece off.")
        speed_choice3 = input("Does he run to the end of the hall or continue slowly? Choose 'Run' or 'Slow'.")
        speed_choice3 = speed_choice3.lower()
        if speed_choice3 == "run":
            print("\nWith the end in sight, {name} breaks for the door.".format(name=character_select.name))
            trap_chance
        if speed_choice3 == "slow":
            print("\nSlow and sure wins the race, is what {name} always said. \n Unfortunately going so slowly comes with a price - an enemy Knight has rushed you!".format(name=character_select.name))
            print(black3)
            while black3.hp > 0:
                fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
                fight_choice = fight_choice.lower()
                while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
                    fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
                    fight_choice = fight_choice.lower()
                if fight_choice == "attack":
                    character_select.attack(black3)
                if fight_choice == "use potion":
                    character_select.use_potion()
                if fight_choice == "defend":
                    character_select.defend(black3)
                if fight_choice == "run":
                    character_select.run()
                black3.attack(character_select)
            else:
                kill_count += 1
                print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
                print("The Knight has no power over {name}. Stepping over its corpse, he heads for the end of the hall.".format(name=character_select.name))
if speed_choice == "hurry":
    print("\nWanting to get out of this hell hole, {name} springs forward to the other end of the hall, heedless of danger or trap!".format(name=character_select.name))
    character_select.spring_trap()
print("Finally making it across the trapped corridor, there is but one door to go through.")
door_choice = input("Pick the lock or break the door down?")
door_choice = door_choice.lower()
while door_choice != "pick the lock" and door_choice != "break the door" and door_choice != "break the door down":
    door_choice = input("\nSelect: 'Pick the Lock' or 'Break the Door'.")
    door_choice = door_choice.lower()
if door_choice == "pick the lock":
    print("\nUsing a makeshift pick found along the dungeon, he deftly opens the rudimentary door lock without problem.")
if door_choice == "break the door" or door_choice == "break the door down":
    print("\nSmashing through the wooden door, he remains unscathed save for a cut across the arm - taking 1 damage.")
    character_select.lose_health(1)
print("\n{name} certainly did not expect this scene on the other side of that simple door. \nAbout 20 meters away rests a large, dark wooden desk. \nA tiny curious creature, deep in thought and count, sits very still, besides its curling fingers that quickly count a large sum of gold coins. \nOn all sides of the petite creature, flowing down from the desk and filling the spacious room around us, lies innumerable gold pieces. \nWithout paying {name} the slightest mind, the creature snaps his grotesque fingers. \nSuddenly, the floor drops out from below him and {name} plummets down, taking 3 points of falling damage.".format(name=character_select.name))
character_select.lose_health(3)
print("\nForcibly brought to his knees from the drop, {name} must quickly decide his next action. He knew the small creature must've been close to the exit! But where to go? \nThere are a few options to try: Climb back up to the Goblinoid creature, Sprint out of this Room and on toward the Exit, or Investigate this room and Prepare for what is coming.".format(name=character_select.name))
choice_select = input("What will it be? Climb, Sprint, or Investigate?")
choice_select = choice_select.lower()
while choice_select != "climb" and choice_select != "sprint" and choice_select != "investigate":
    choice_select = input("\nChoose 'Climb', 'Sprint', or 'Investigate'.")
    choice_select = choice_select.lower()
if choice_select == "climb":
    print("\nThe walls up to the drop floor are old and cavernous, with some footholds along the way. It may be possible to climb.")
    print("{name} attempts the journey up!".format(name=character_select.name))
    climb_chance = random.randint(1, 10)
    if climb_chance > 6:
        print("\nUsing his athletic prowess, he takes a running leap up toward the gaping ceiling. \nAfter a great first jump and a few frantic handholds, {name} amazingly reaches the bottom of the trap door and grasps hold tightly. \n Ever so carefully, he pulls himself up to the edge.".format(name=character_select.name))
        print("By the time he regained his position in the room above, the Goblinoid creature was nowhere to be seen. \nThere are pools of coins everywhere around the room, but gold is all but useless in here.")
        print("Behind the desk, another door stands slightly ajar, guiding the way forward.")
        input("Head into the doorway?")
        print("\nYou step through the door into a strangely open, barren room.")
    else:
        print("\nUsing his athletic prowess, he takes a running leap up toward the gaping ceiling. After a great first jump and a few frantic handholds, {name} slips and goes plummeting back to the earth.".format(name=character_select.name))
        character_select.lose_health(4)
        print("After coming back to consciousness, he slowly gets to his feet and regains his bearing.")
if choice_select == "sprint":
    print("\nNot waiting for whatever traps and dangers were being sent down upon him, {name} took to fleeing the room. \nThere must be another way out. He sprints to the edge of the room, towards what looks like an open crevice in the wall.".format(name=character_select.name))
    crevice_choice = input("Attempt to squeeze through the crevice?")
    crevice_choice = crevice_choice.lower()
    if crevice_choice == "yes":
        print("\nUsing every effort to push himself through the narrow opening, he rights himself on the other side. \nIt's another large room, but there are some crates gathered in one area and a ladder going through a hole in the ceiling.")
        room_choice = input("Go for the Crates or the Ladder?")
        room_choice = room_choice.lower()
        while room_choice != "crates" and room_choice != "ladder":
            room_choice = input("\nTry again, Crates or Ladder?")
            room_choice = room_choice.lower()
        if room_choice == "crates":
            print("\n{name} heads to the crates to see what lies inside.".format(name=character_select.name))
            trap_chance()
            print("Investigating the crates, he finds 2 potions!")
            character_select.num_potions += 2
            print("Gathering the potions, he heads over to the ladder!")
            room_choice = "ladder"
        if room_choice == "ladder":
            print("\nMaking his way over to the ladder, {name} finds the rungs and hauls himself up through the hole in the ceiling into the room above.".format(name=character_select.name))
            print("The new room he finds himself in is strangely barren as he looks around.")
    else:
        print("\nThe crevice looks too narrow and unsafe. He turns back to the open room.")
        choice_select == "investigate"
if choice_select == "investigate":
    print("\nAlthough he realizes this room must be some sort of trap, {name} believes there must be more here than meets the eye. \nBesides the trap door above and the crevice in the far wall, there are 3 pillars in the middle of the room.".format(name=character_select.name))
    print("On the first pillar rests a button. On the second, a large dial. On the third, there is a vial of liquid.")
    pillar_choice = input("What does he do?")
    pillar_choice = pillar_choice.lower()
    while pillar_choice != "press the button" and pillar_choice != "turn the dial" and pillar_choice != "drink the vial":
        pillar_choice = input("\nPlease choose: 'Press the Button', 'Turn the Dial', or 'Drink the Vial'.")
        pillar_choice = pillar_choice.lower()
    if pillar_choice == "press the button":
        print("\nTempted by the gratification of pressing a small button, {name} reaches forward. As soon as it is depressed, hell rains down. \nMolten fire quickly engulfs his body.".format(name=character_select.name))
        character_select.lose_health(random.randint(4,10))
        print("He drops to the floor to extinguish the flames.")
        pillar_choice = input("That didn't work. What next? Turn the Dial or Drink the Vial?")
        pillar_choice.lower()
    if pillar_choice == "drink the vial":
        print("\nHolding the vial under his nose, {name} gets a sweet flowery scent before he throws it back. \nAs he drains the last drops, he notices a message on the underside of the vial: \n'You should have Turned the Dial'.".format(name=character_select.name))
        print("The room disappears from around {name}, and darkness takes over.".format(name=character_select.name))
        character_select.lose_health(10)
        print("\n\n\n\n\n\n\n\n\n\nAfter an unknown length of time, he wakes up, in a barren room.")
    if pillar_choice == "turn the dial":
        print("\nAs he forces the dial to turn clockwise, it causes some sort of contraption to unwind - revealing a twisting staircase to another room below.")
        print("Following the stairs down in the unknown, {name} finds himself in a strangely barren room.".format(name=character_select.name))

##############################################################################################################
### fifth branch
        
print("\nLooking around the barren room, he sees naught but the way he came in. \nBut something calls out, there seems something peculiar about this room.")
continue_choice = input("Carry forward?")
continue_choice = continue_choice.lower()
while continue_choice != "yes":
    continue_choice = input("There's no time to waste. Ready to move?")
    continue_choice = continue_choice.lower()
if continue_choice == "yes":
    print("Stepping into the room, {name} searches for whatever is giving him this off feeling.".format(name=character_select.name))
search_choice = input("He can look along the wall or search for trap doors in the floor. Which to explore - Wall or Floor?")
search_choice = search_choice.lower()
while search_choice != "wall" and search_choice != "floor":
    search_choice = input("\nChoose 'Wall' or 'Floor'.")
    search_choice = search_choice.lower()
if search_choice == "wall":
    print("\n{name} begins to look for secrets by pressing his hand against the wall closest, then slowly circles the perimeter.".format(name=character_select.name))
    print("Suddenly, his hand gives way, through the wall! \nThe wall looks solid, the same as the rest of the room, but he can pass straight through!")
    step_choice = input("Step through the passage?")
    step_choice = step_choice.lower()
    while step_choice != "yes" and step_choice != "no":
        step_choice = input("\nChoose Yes or No")
        step_choice = step_choice.lower()
    if step_choice == "yes":
        print("\nStarting with his hand, then arm, then shoulder - he watches his body disappear into the next room. \nDipping his head through, he sees what looks like an armory. Best to fully stock up.")
        print("Unfortunately, just as {name} reaches for a shiny new sword, two guards spring out of the darkness!".format(name=character_select.name))
        print("The first Guard immediately charges, blade lowered!")
        while gard.hp > 0:
            fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
            fight_choice = fight_choice.lower()
            while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
                fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
                fight_choice = fight_choice.lower()
            if fight_choice == "attack":
                character_select.attack(gard)
            if fight_choice == "use potion":
                character_select.use_potion()
            if fight_choice == "defend":
                character_select.defend(gard)
            if fight_choice == "run":
                character_select.run()
            gard.attack(character_select)
        else:
            kill_count += 1
            print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
        print("The second guard rears his head back in a warcry, then springs forward!")
        while gard2.hp > 0:
            fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
            fight_choice = fight_choice.lower()
            while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
                fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
                fight_choice = fight_choice.lower()
            if fight_choice == "attack":
                character_select.attack(gard2)
            if fight_choice == "use potion":
                character_select.use_potion()
            if fight_choice == "defend":
                character_select.defend(gard2)
            if fight_choice == "run":
                character_select.run()
            gard2.attack(character_select)
        else:
            kill_count += 1
            print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
        print("Having already relieved the guards of their duties, he relieves them of their assets as well.")
        character_select.has_armor = True
        character_select.has_sword = True
        character_select.num_potions += 2
    if step_choice == "no":
        print("\nFearing the mysterious mirage, he heads back to search for another option.")
        search_choice = "floor"
if search_choice == "floor":
    print("\nSearching for some crack or crease in the tile, {name} crawls on his hands and knees along the floor.".format(name=character_select.name))
    print("He manages to find a floorboard that doesn't quite line up with the others. \nShoving the tip of his sword into the edge, he pries up a board and reveals a secret compartment, with a small button inside.")
    input("Press the button?")
    print("\nA wall slides away, revealing an adjacent room. It appears to be an armory. Best to fully stock up.")
    print("Unfortunately, just as {name} reaches for a shiny new sword, two guards spring out of the darkness!".format(name=character_select.name))
    print("The first Guard immediately charges, blade lowered!")
    while gard.hp > 0:
        fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
        fight_choice = fight_choice.lower()
        while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
            fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
            fight_choice = fight_choice.lower()
        if fight_choice == "attack":
            character_select.attack(gard)
        if fight_choice == "use potion":
            character_select.use_potion()
        if fight_choice == "defend":
            character_select.defend(gard)
        if fight_choice == "run":
            character_select.run()
        gard.attack(character_select)
    else:
        kill_count += 1
        print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
    print("The second guard rears his head back in a warcry, then springs forward!")
    while gard2.hp > 0:
        fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
        fight_choice = fight_choice.lower()
        while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
            fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
            fight_choice = fight_choice.lower()
        if fight_choice == "attack":
            character_select.attack(gard2)
        if fight_choice == "use potion":
            character_select.use_potion()
        if fight_choice == "defend":
            character_select.defend(gard2)
        if fight_choice == "run":
            character_select.run()
        gard2.attack(character_select)
    else:
        kill_count += 1
        print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
    print("Having already relieved the guards of their duties, he relieves them of their assets as well.")
    character_select.has_armor = True
    character_select.has_sword = True
    character_select.num_potions += 2
print("Replacing his worn mail for a new plate, and his notched sword for a fresh blade, {name} feels he is ready to face whatever demon bars his exit from this place.".format(name=character_select.name))
print("On the far side of the armory, thick double doors beckon. The path out surely must be ahead.")
print("Pulling on the double doors, he reveals a huge new room.")
go_choice = input("Does {name} venture forth into this vast room?".format(name=character_select.name))
go_choice = go_choice.lower()
while go_choice != "yes" and go_choice != "no":
    go_choice = input("Simply, Yes or No.")
    go_choice = go_choice.lower()
if go_choice == "no":
    print("\nThere is no other way forward. He must face his fate!")
    print("\nHe inches forward into the great room, anxiety rippling through his body.")
if go_choice == "yes":
    print("\nHe strides forward with confidence into the great room unknown.")
print("This is no ordinary room, and it is far unlike any of the others encountered. \nThe vast circular chamber, with its bare dirt floor, lies completely empty - save from the doors you came through, and a similar but much larger set on the opposite wall.")
print("A large dome of a cage covers the entirety of the space.\nAnd then it hits him.\n\n\n\n")
print("Behind the bars of this cage sat hundreds of bodies, not unlike the Goblinoid creature encountered counting coin.")
print("These creatures screeched, hollered, and rasped out in their wicked tongue in excitement - over {name}!".format(name=character_select.name))

##############################################################################################################
### sixth branch

run_choice = input("The time for action is now, if ever. Does he: Run Back, Walk Forward, or Yell?")
run_choice = run_choice.lower()
while run_choice != "run back" and run_choice != "walk forward" and run_choice != "yell":
    run_choice = input("\nChoose 'Run Back', 'Walk Forward', or 'Yell'.")
    run_choice = run_choice.lower()
    print("As the reality of the situation dawns on him, the doors slam shut tight behind.")
if run_choice == "run back":
    print("\n{name} turns just in time to see the doors seal. The crowd cheers and jeers once more.".format(name=character_select.name))
    print("There is no way back, only toward his fate. \nHe reaches within himself to find the strength to turn around and face this doom.")
if run_choice == "walk forward":
    print("\n{name} walks boldly forward toward the center of the room, glancing around at the masses gathered. Many creatures hiss at his chutzpah.".format(name=character_select.name))
if run_choice == "yell":
    print("\nEchoing their chaos, {name} leaps forward and throws his head back in a wild war cry! The mass of Goblinoids goes wild in return.".format(name=character_select.name))
print("The army of creatures greedily peering down upon him cackle and roar constantly, and the echoes of their voices invade every inch of space in this colossal chamber. \nIt permeates through to his mind.")
print("They are ready for a fight.")
continue_choice = input("Is {name} ready?".format(name=character_select.name))
continue_choice = continue_choice.lower()
while continue_choice != "yes":
    print("\nThat's too bad. The time has come for battle.")
    continue_choice == "yes"
if continue_choice == "yes":
    print("\n{name} grits his teeth and bares his knuckles over the hilt of his sword. Not knowing what threat lies ahead, his fear begins to grow.".format(name=character_select.name))
print("Finally, the massive double doors opposite the room creak and begin to swing open.")
print("A shimmering red dragon stands in the empty doorway, ready to bear down on its new prey!")
print(drag)
while drag.hp > 0:
    fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
    fight_choice = fight_choice.lower()
    while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
        fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
        fight_choice = fight_choice.lower()
    if fight_choice == "attack":
        character_select.attack(drag)
    if fight_choice == "use potion":
        character_select.use_potion()
    if fight_choice == "defend":
        character_select.defend(drag)
    if fight_choice == "run":
        character_select.run()
    drag.attack(character_select)
else:
    kill_count += 1
    print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
    print("At long last, the dragon stands wide and reveals a weak spot in his scales.")
    print("{name} charges forward in one last attempt and, dodging the dragon's claws, thrusts his sword deep into the fatal flaw.".format(name=character_select.name))
print("\nThe army of Goblinoids is baffled. The cacophony ceases for a moment as the dragon's body falls lifeless.")
print("Then pure chaos erupts once more, but it seems as though they are not cries of disgust - but cheers of victory.")
cheer_choice = input("Should he join in the revelry and throw his arms up in cheer, or rather take off toward the open double doors? \nCheer or Run?")
cheer_choice = cheer_choice.lower()
while cheer_choice != "cheer" and cheer_choice != "run":
    cheer_choice = input("\nSelect 'Cheer' or 'Run'.")
    cheer_choice = cheer_choice.lower()
if cheer_choice == "cheer":
    print("\n{name} throws his head back and releases a guttural cry, reflecting those from the crowd. \nHe thrusts his sword high in the air and absorbs the ecstasy of the moment.".format(name=character_select.name))
    print("The cackling crowd spills from the stands, filtering down to the arena floor below.")
    print("Drunk from the victory, {name} hears his name being chanted over and over. \n\n{yelled}! {yelled}! {yelled}!".format(name=character_select.name, yelled=character_select.name.upper()))
    print("As the throngs of Goblinoids scutter around the battle victor, he starts to feel their hands moving around him, over his body.")
    print("Before he realizes it, their spindly fingers grasp onto his wrists, ankles, arms, until he's being overwhelmed.")
    fight_choice = input("Now is {name}'s last chance - fight or run?".format(name=character_select.name))
    fight_choice = fight_choice.lower()
    if fight_choice == "fight":
        print("\n{name} grips his longsword and swings it wildly about, in an attempt to free himself from the swarm of creatures.".format(name=character_select.name))
        print("Though he cuts through these small, grotesque creatures with ease, with each kill there in pours thrice as many foes.")
        print("{name} is quickly overrun and falls, gasping for air as the hundreds of hands twise and grip his life away.".format(name=character_select.name))
        character_select.die()
    else:
        print("\n{name} furiously erupts in a final attempt to flee.".format(name=character_select.name))
        print("Long, twisted fingers begin to grasp at him, in attempt to pull him down to his fate. \nBut his sudden burst of speed pushes him forward as adrenaline courses through his veins once more.")
        print("Clambering past a wave of Goblinoids, {name} darts through the gargantuan doors from whence the Dragon came.".format(name=character_select.name))
if cheer_choice == "run":
    print("\nNot missing a beat, {name} bolts past the dragon's crimson corpse, through the gargantuan double doors from whence the beast came.".format(name=character_select.name))
    print("No other thought now crossed his mind but to escape!")
print("Sprinting past the doors into a charred, empty chamber, there appears to be another room or hall off to the right.")
which_choice = input("Does he go toward the hall to the right or search around for another way? Select: 'Go to Hall' or 'Search the Room'.")
which_choice = which_choice.lower()
while which_choice != "go to hall" and which_choice != "search the room":
    which_choice = input("\nSelect: 'Go to Hall' or 'Search the Room'.")
    which_choice = which_choice.lower()
if which_choice == "search the room":
    print("\n{name} glances quickly around the chamber, and finds it void of much of interest. \nA sole metal cylindrical container stands by the doors.".format(name=character_select.name))
    final_chance_to_die = input("He sees the clambering of the Goblinoids fiercely coming his direction. \nDoes he Open the Container or Run?")
    final_chance_to_die = final_chance_to_die.lower()
    while final_chance_to_die != "open the container" and final_chance_to_die != "run":
        final_chance_to_die = input("\nSelect: 'Open the Container' or 'Run'.")
        final_chance_to_die = final_chance_to_die.lower()
    if final_chance_to_die == "open the container":
        print("With the enemy closing in, he rushes to the metal cylinder, searching for redemption within. \nThrowing back the clasp and open the lid, he pulls out a spherical crystal flask, within it an orange gelatinous liquid.")
        throw_choice = input("The Goblinoids nearly reaching him, {name} must use the special flask to protect himself. \nDoes he fling the amber liquid at his impending opponents or open the flask to consume the contents? \nSelect: Throw it or Drink it.".format(name=character_select.name))
        throw_choice = throw_choice.lower()
        while throw_choice != "throw it" and throw_choice != "drink it":
            throw_choice = input("Please choose: 'Throw It' or 'Drink It'.")
            throw_choice = throw_choice.lower()
        if throw_choice == "throw it":
            print("\nGlancing back over his shoulder at the incoming horde, he lobs the crystal flask into the thick of it all. \nHe doesn't stay to watch, but he can feel an infernal wave wash over his body and the force of what sounds like a large cannon.")
            print("{name} dashes for the door.".format(name=character_select.name))
        if throw_choice == "drink it":
            print("\nHoping for the best, he pops open the flask's cork and throws back the contents down his gullet.")
            print("A wave of infernal heat rips through {name}'s body and he immediately regrets his decision. \n{name} stumbles toward the door to escape the pain, but scorching nausea fills his existence.".format(name=character_select.name))
            print("Turning to take one last look at his foes, he can no longer hold in the torment! \nHe throws his head back to scream but fire and doom spew forth upon and around his foes.")
            print("A pool of flesh and flame impede the enemy creatures, so {name} makes for the door once more!".format(name=character_select.name))
        which_choice = "go to hall"
    if final_chance_to_die == "run":
        print("\nImpending doom spurns on his decision as he turns his back to the container.")
        which_choice = "go to hall"
if which_choice == "go to hall":
    print("\n{name} now sprints through the doorway, toward what he realizes may be the exit, as moonlight pours through a windowed door at the wall opposite".format(name=character_select.name))
print("Hope now filled his entirety as freedom was nearly a reality.")
print("Alas, a single foe stands in your way as another Black Knight bursts in front of you!")
print(black4)
while black4.hp > 0:
    fight_choice = input("\nChoose your action: \n Attack \t Use Potion \t Defend \t Run")
    fight_choice = fight_choice.lower()
    while fight_choice != "attack" and fight_choice != "use potion" and fight_choice != "defend" and fight_choice != "run":
        fight_choice = input("\nYou did not select 'Attack', 'Use Potion', 'Defend', or 'Run'. Choose your action:")
        fight_choice = fight_choice.lower()
    if fight_choice == "attack":
        character_select.attack(black4)
    if fight_choice == "use potion":
        character_select.use_potion()
    if fight_choice == "defend":
        character_select.defend(black4)
    if fight_choice == "run":
        character_select.run()
    black4.attack(character_select)
else:
    kill_count += 1
    print("{name} has defeated {killcount} foes.\n".format(name=character_select.name, killcount = kill_count))
print("\nThe final foe falls freely forward, flinching and flailing freakily.")
print("Freedom awaits, as {name} has eluded Fate.".format(name=character_select.name))
input("Step through the door?")
print(game_name)