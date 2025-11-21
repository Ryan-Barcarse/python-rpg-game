from entity import Entity
import random

class BegTroll(Entity):
  """
  Beginner-level troll enemy.

  Attributes:
    name: Entity name.
    hp: Starting hit point range: 8-10.
  """
  def __init__(self):
    """
    Initializes the beginner troll with a randomized hp.

    Returns:
      None.
    """
    super().__init__("EZ Troll", random.randint(8, 10))

  def melee_attack(self, enemy):
    """
    Performs a melee punch attack on the enemy.

    Args:
      enemy: The entity being attacked.

    Returns:
      A string describing the attack.
    """
    dmg = random.randint(5, 9)
    enemy.take_damage(dmg)
    return f"{self.name} punches {enemy.name} for {dmg} damage."
