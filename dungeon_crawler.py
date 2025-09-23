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
    def create_monster():
        monsters = ["Ghost", "Goblin", "Python"]
        name = random.choice(monsters)
        
        if name == "Ghost":
            # Teir 1 monster
            return Monster(name, random.randint(0, 1), random.randint(1, 2), 2)
        elif name == "Goblin":
            # Teir 2 monster
            return Monster(name, random.randit(0, 1), random.randint(1, 2), 10)
        elif name == "Python":
            # Teir 3 monster
            return Monster(name, random.randint(3, 6), random.randint(6, 12), 5)

class Room:
    """A Room in the Cave system an Adventurer can enter.
    
    The Room may has a Monster and Item (treasure) when created. In addition the Room has a method called enter.
    Combat is resolved when the Adventurer enters the Room.
    
    Attributes:
        monster: The Monster in the room.
        treasure: An item for the Adventurer when the combat is resolved.
    """
    
    def __init__(self) -> None:
        """Initializes the Room with a random monster and item."""

        self.create_monster_and_treasure()
        
    def create_monster_and_treasure(self) -> None:
        """Creates a random monster and item for the room."""
        
        items = ["Wooden Club 몽둥이", "Iron Shortsword 🗡️", "Steel Longsword ⚔️", "Serrated Flame Blade 🔥", "Dragon's Tooth Greatsword 🐉"]
        
        self.treasure = Item(
            name = random.choice(items),
            min_damage = random.randint(0, 2),
            max_damage = random.randint(4, 8),
        )


class Cave:
    """The Cave system which contains Rooms.
    
    Attributes:
        entrance: The Room which is the entrance to the Cave.
    """
    
    def __init__(self, entrance: Room) -> None:
        """Initializes the Cave with an entrance Room.
        
        Args:
            entrance: The Room which is the entrance to the Cave.
        """
        self.entrance: Room = entrance