import random

import random

class Adventurer:
    """This class represents the user in the game.
    
    The Adventurer moves through the Cave system going Room to Room trying to slay Monsters.
    
    Attributes:
        name: Display name of the character.
        strength: Strength, on a scale of 1-18.
        constitution: Constitution, on a scale of 1-18.
        hit_points: An integer, when <=0 the character is dead.
        bag: Holds an unsorted list of Item objects the character has.
    """
    
    def __init__(self, name: str) -> None:
        """Initializes the Adventurer with a name and some random stats.
        
        Args:
            name: The name of the Adventurer.
        """
        self.name: str = name
        self.strength: int = random.randint(3, 18)
        self.constitution: int = random.randint(3, 18)
        self.hit_points: int = self.constitution + random.randint(10, 30)
        self.bag: list[Item] = [Item("Butter Knife", 0, 2)]

class Item:
    """ An item which can be held by an Adventurer.
    
    Items are weapons in this game, and may have a range of possible damages.
    
    Attributes:
        name: The display name of the item.
        min_damage: The minimum damage an item can inflict, cannot be negative.
        max_damage: The maximum damage an item can inflict, cannot be negative.
    """
    def __init__(self, name: str, min_damage: int, max_damage: int) -> None:
        """Initializes the Item and it's minimum and maximum damage.
        
        Args:
            name: The name of the Item.
        """
        if name != None:
            self.name: str = name
        else:
            self.name: str = "Unknown Item"
        
        self.min_damage: int = min_damage
        self.max_damage: int = max_damage

class Monster:
    """A Monster which the Adventurer may encounter in a room within the cave system.
    
    There are 10 different monsters, one for each room in the cave system.
    To create a random monster call the function create_monster().
    
    Attributes:
        name: The display name of the monster.
        min_damage: The minimum damage the monster can inflict. Cannot be negative.
        max_damage: The maximum damage the monster can inflict. Cannot be negative.
        hit_points: Total number of hit_points a monster has. Cannot be negative.
    """
    
    def __init__(self, name: str, min_damage: int, max_damage: int, hit_points: int) -> None:
        """Initializes the Monster with a name and attributes.
        
        Args:
            name: The name of the Monster.
            min_damage: The minimum damage a monster might cause.
            max_damage: The maximum damage a monster might cause.
            hit_points: The total number of hit points a monster has.
        """
        # TODO: Add input validation
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.hit_points = hit_points
    
    # class function, not a method. Used to create a random monster.
    @staticmethod
    def create_monster():
        monsters = ["Ghost 👻", "Goblin 👹", "Python 🐍"]
        name = random.choice(monsters)
        
        if name == "Ghost 👻":
            # Teir 1 monster
            return Monster(name, random.randint(0, 1), random.randint(1, 2), 2)
        elif name == "Goblin 👹":
            # Teir 2 monster
            return Monster(name, random.randint(0, 1), random.randint(1, 2), 10)
        elif name == "Python 🐍":
            # Teir 3 monster
            return Monster(name, random.randint(3, 6), random.randint(6, 12), 5)

class Room:
    """A Room in the Cave system an Adventurer can enter."""
    
    def __init__(self) -> None:
        """Initializes the Room with a random monster and item."""
        self.create_monster_and_treasure()
        
    def create_monster_and_treasure(self) -> None:
        """Creates a random monster and item for the room."""
        items = ["Wooden Club 몽둥이", "Iron Shortsword 🗡️", "Steel Longsword ⚔️", "Serrated Flame Blade 🔥", "Dragon's Tooth Greatsword 🐉"]
        self.treasure = Item(
            name=random.choice(items),
            min_damage=random.randint(0, 2),
            max_damage=random.randint(4, 8),
        )
        self.monster = Monster.create_monster()

    @staticmethod
    def calculate_damage(attacker, defender) -> bool:
        """Calculates damage and returns True if the defender is defeated."""
        # Note: We use attacker's name for flavor, but the damage comes from the object
        attacker_name = attacker.name
        
        # When the hero attacks, the attacker object is an Item, but we want the hero's name
        if isinstance(attacker, Item):
             attacker_name = "Hero" # A placeholder, you can pass the hero's name in for more detail

        damage_done = random.randint(attacker.min_damage, attacker.max_damage)
        defender.hit_points -= damage_done
        
        print(f"{attacker_name} hits {defender.name} for {damage_done} damage! {defender.name} has {max(0, defender.hit_points)} HP left.")
        
        if defender.hit_points <= 0:
            print(f"{defender.name} has been defeated!")
            return True
        return False

    def enter(self, hero: Adventurer) -> str:
        """A method which pits a hero against the monster in the room."""
        print(f"{hero.name} enters the room and encounters a {self.monster.name}!")
        
        # --- COMBAT LOOP ---
        while hero.hit_points > 0 and self.monster.hit_points > 0:
            # Hero's turn
            print("\n--- Hero's Turn ---")
            weapon = hero.bag[0] # For now, just use the first weapon
            monster_defeated = Room.calculate_damage(weapon, self.monster)
            if monster_defeated:
                break # Exit loop if monster is defeated
            
            # Monster's turn
            print("\n--- Monster's Turn ---")
            hero_defeated = Room.calculate_damage(self.monster, hero)
            if hero_defeated:
                break # Exit loop if hero is defeated

        # --- AFTER COMBAT ---
        if hero.hit_points > 0:
            print(f"\n{hero.name} is victorious!")
            hero.bag.append(self.treasure)
            print(f"{hero.name} found a {self.treasure.name} and added it to their bag.")
            return "win"
        else:
            return "lose"


class Cave:
    """The Caves contain 10 Rooms.   """
    
    def __init__(self) -> None:
        """Initializes the Cave with 10 Rooms."""
        self.rooms: Room = []
        for i in range(0, 10):
            self.rooms.append(Room())

    def explore(self, hero: Adventurer) -> str:
        """The Adventurer explores the Cave going from Room to Room.
        
        If the Adventurer dies in a Room the return value is 'lose'.
        If the Adventurer clears all 10 Rooms the return value is 'win'.
        
        Args:
            hero: The Adventurer exploring the Cave.
        """
        for room in self.rooms:
            result = room.enter(hero)
            if result == "lose":
                print(f"{hero.name} has perished in the Cave.")
                return
            else:
                print(f"{hero.name} has cleared the room! You now have {hero.hit_points} hit points left and {len(hero.bag)} items in your bag.")

        print(f"{hero.name} has cleared the Cave!")

hero = Adventurer("Conan the Barbarian")
cave = Cave()
cave.explore(hero)
