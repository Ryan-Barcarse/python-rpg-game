from entity import Entity
import random

class Hero(Entity):
  """
  Represents the player's character.

  Attributes:
    name: The hero's name.
    hp: The hero's current hit points (starts at 25).
  """
  def __init__(self, name):
    """
    Initializes the hero with a name and default hp.

    Args:
      name: The name entered by the user.

    Returns:
      None.
    """
    super().__init__(name, 25)

  def melee_attack(self, enemy):
    """
    Performs a sword attack dealing 2D6 damage.

    Args:
      enemy: The entity being attacked.

    Returns:
      A string describing the attack.
    """
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    dmg = d1 + d2
    enemy.take_damage(dmg)
    return f"{self.name} slashes a {enemy.name} with a sword for {dmg} damage."

  def ranged_attack(self, enemy):
    """
    Performs an arrow attack dealing 1D12 damage.

    Args:
      enemy: The entity being attacked.

    Returns:
      A string describing the attack.
    """
    dmg = random.randint(1, 12)
    enemy.take_damage(dmg)
    return f"{self.name} pierces a {enemy.name} with an arrow for {dmg} damage."
