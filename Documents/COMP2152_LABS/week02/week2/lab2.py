weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
import random


def choose_Weapon():
    try:
        weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
        weaponRoll = random.randint(1, 6)

        print(f"You rolled a {weaponRoll}.")

        weaponIndex = weaponRoll - 1
        heroWeapon = weapons[weaponIndex]

        print(f"Your weapon is: {heroWeapon}")

        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend.")
        elif weaponRoll <= 4:
            print("Your weapon is meh.")
        else:
            print("Nice weapon, friend!")

        if heroWeapon != "Fist":
            print("Thank goodness you didn't roll the Fist...")

    except Exception as e:
        print(f"An error occurred: {e}")


choose_Weapon()