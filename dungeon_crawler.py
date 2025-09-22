import random

class Adventurer:
    """This class represents the user in the game.
    
    The Adventurer moves through the Cave system going Room to Room trying to slay Monsters.
    
    Attributes:
        name: Display name of the character.
        dexterity: Dexterity, on a scale of 1-18.
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
        self.hit_points: int = self.constitution + random.randint(1, 8)
        self.bag: list[Item] = []

class Item:
    """ An item which can be held by an Adventurer.
    
    Items are weapons in this game, and may have a range of possible damages.
    
    Attributes:
        name: The display name of the item.
        min_dmg: The minimum damage an item can inflict, cannot be negative.
        max_dmg: The maximum damage an item can inflict, cannot be negative.
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
    """A Monster which the Adventurer may encounter in a Room.
    
    Attributes:
        name: The display name of the monster.
        min_dmg: An integer, the minimum damage the monster can inflict.
        max_dmg: An integer, the maximum damage the monster can inflict.
        constitution: Constitution, on a scale of 1-18.
        strength: Strength, on a scale of 1-18.
        hit_points: An integer, when <= 0 the Monster is dead.m,
    """
    
    def __init__(self, name: str, min_damage: int, max_damage: int) -> None:
        """Initializes the Monster with a name and some random stats.
        
        Args:
            name: The name of the Monster.
        """
        self.name: str = name
        self.min_damage: int = min_damage
        self.max_damage: int = max_damage
        self.strength: int = random.randint(3, 18)
        self.constitution: int = random.randint(3, 18)
        self.hit_points: int = self.constitution + random.randint(1, 8)

class Room:
    """A Room in the Cave system.
    
    The Room may contain a Monster, and may have connections to other Rooms.
    
    Attributes:
        treasure: An Item in the room, or None if no item is present.
        description: A description of the room.
        monster: The Monster in the room, or None if no monster is present.
        exits: A dictionary mapping direction strings to other Room objects.
    """
    
    def __init__(self, name: str, description: str) -> None:
        """Initializes the Room with a name and description.
        
        Args:
            name: The name of the Room.
            description: A description of the Room.
        """
        self.name: str = name
        self.treasure: Item | None = None
        self.description: str = description
        self.monster: Monster | None = None
        self.exits: dict[str, Room] = {}


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