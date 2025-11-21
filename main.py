"""
November 5, 2025
Student 2: Ryan Barcarse

This game prompts the user to attack 1 of 3 potential monsters that can vary in strength. The user rolls die to determine
the power output of their weapon, winning the game if all monsters are slain.
"""
from beg_factory import BeginnerFactory
from exp_factory import ExpertFactory
from hero import Hero
from check_input import get_int_range


def main():
    print("Monster Trials")

    # Gets hero name from user
    name = input("What is your name? ")
    print()
    hero = Hero(name)

    # Creates the factories
    beg_factory = BeginnerFactory()
    exp_factory = ExpertFactory()

    # Create 2 beginner enemies and 1 expert enemy
    monsters = [
        beg_factory.create_random_enemy(),
        beg_factory.create_random_enemy(),
        exp_factory.create_random_enemy()
    ]

    print(f"You will face a series of 3 monsters, {hero.name}.\nDefeat them all to win.")

    # Main loop of the game
    while hero.hp > 0 and monsters:
        print("\nChoose an enemy to attack:")
        for i, monster in enumerate(monsters, start=1):
            print(f"{i}. {monster}")

        #User selects a monster
        monster_choice = get_int_range("Enter your choice: ", 1, len(monsters))
        monster = monsters[monster_choice - 1]

        #Choose attack type
        print(f"\n{hero}")
        print("1. Sword Attack\n2. Arrow Attack")
        atk_choice = get_int_range("Enter your choice: ", 1, 2)

        #Hero potential attacks
        if atk_choice == 1:
            print(hero.melee_attack(monster))
        else:
            print(hero.ranged_attack(monster))

        #Monster only responds if alive
        if monster.hp > 0:
            print(monster.melee_attack(hero))
        else:
            print(f"You have slain the {monster.name}")
            monsters.remove(monster)

    if hero.hp <= 0:
        print("\nYou have been slain!\nGame over.")
    else:
        print("\nCongratulations! You defeated all three monsters!\nGame over.")


if __name__ == "__main__":
    main()