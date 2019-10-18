from classes.game import Person, bcolors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 40, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cure", 18, 200, "white")

# Instantiate People
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print("AN ENEMY  ATTACKS!")

while running:
    print("================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attecked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic:")) - 1



        # magic_dmg = player.generate_spell_damage(magic_choice)
        # spell = player.get_spell_name(magic_choice)
        # cost = player.get_spell_mp_cost(magic_choice)

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print("\nNot enough MP\n")
            continue

        if spell.type == "white":
            player.heal(magic_dmg)
            print("\n" + spell.name + " heals for", str(magic_dmg), "HP.")
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
        
        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print("\n" + spell.name, "deals", str(magic_dmg), "points of damage")


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("------------------------")
    print("Enemy HP:", str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + "\n")

    print("Your HP :", str(player.get_hp()), "/" +str(player.get_max_hp()))
    print("Your MP :", str(player.get_mp()), "/" +str(player.get_max_mp()) + "\n")

    if enemy.get_hp() == 0:
        print("You Win!")
        running = False
    elif player.get_hp() == 0:
        print("Your enemy has defeated you!")
        running = False