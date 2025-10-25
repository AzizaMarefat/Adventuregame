import random

# ---------------- PLAYER CLASS ----------------
class Player:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.inventory = []

    def show_status(self):
        print(f"{self.name} - HP: {self.hp}, Inventory: {self.inventory}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} added to inventory!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")
            return True
        return False


# ---------------- MONSTER CLASS ----------------
class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack  # fixed typo

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")
            return True
        return False


# ---------------- ROOM CLASS ----------------
class Room:
    def __init__(self, description, items=None, monster=None):
        self.description = description
        self.items = items if items else []
        self.monster = monster

    def enter(self, player):
        print(f"\n{self.description}")
        for item in self.items:
            player.add_item(item)
        self.items = []  # remove items after taking

        if self.monster:
            print(f"A wild {self.monster.name} appears!")


# ---------------- FIGHT FUNCTION ----------------
def fight(player, monster):
    while player.hp > 0 and monster.hp > 0:
        action = input("Do you want to (a)ttack or (r)un? ").lower()

        if action == 'a':
            # Player attacks monster
            damage = random.randint(10, 30)
            print(f"You attack {monster.name} for {damage} damage!")
            if monster.take_damage(damage):
                break  # Monster defeated

            # Monster attacks player
            monster_damage = random.randint(5, monster.attack)
            print(f"{monster.name} attacks you for {monster_damage} damage!")
            if player.take_damage(monster_damage):
                break  # Player defeated

        elif action == 'r':
            print("You ran away!")
            break
        else:
            print("Invalid choice! Please type 'a' or 'r'.")


# ---------------- MAIN GAME LOOP ----------------
goblin = Monster("Goblin", 40, 15)
troll = Monster("Troll", 70, 20)

room1 = Room("You are in a dark cave.", items=["Sword"], monster=goblin)
room2 = Room("You enter a forest full of light.", items=["Potion"])
room3 = Room("You reach a misty mountain path.", items=["Shield"], monster=troll)

rooms = [room1, room2, room3]
player = Player("Hero")

print("Welcome to the Adventure Game!")
player.show_status()

for room in rooms:
    room.enter(player)
    if room.monster:
        fight(player, room.monster)
    if player.hp <= 0:
        print("💀 Game Over!")
        break
else:
    print("\n🎉 You finished all rooms and survived the adventure!")
    player.show_status()
##