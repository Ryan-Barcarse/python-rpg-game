from entity import Entity
import random

class BegGoblin(Entity):
  """
  Beginner-level goblin enemy.

  Attributes:
    name: Entity name.
    hp: Starting hit point range: 7-9.
  """
  def __init__(self):
    """
    Initializes the beginner goblin with a randomized hp.

    Returns:
      None.
    """
    super().__init__("EZ Goblin", random.randint(7, 9))

  def melee_attack(self, enemy):
    """
    Performs a melee bite attack on the enemy.

    Args:
      enemy: The entity being attacked.

    Returns:
      A string describing the attack.
    """
    dmg = random.randint(4, 6)
    enemy.take_damage(dmg)
    return f"{self.name} bites {enemy.name} for {dmg} damage."
