from entity import Entity
import random

class ExpGoblin(Entity):
  """
  Expert-level goblin enemy.

  Attributes:
    name: Entity name.
    hp: Starting hit point range: 12-15.
  """
  def __init__(self):
    """
    Initializes the expert goblin with a randomized hp.

    Returns:
      None.
    """
    super().__init__("Horrible Goblin", random.randint(12, 15))

  def melee_attack(self, enemy):
    """
    Performs a melee slam attack on the enemy.

    Args:
      enemy: The entity being attacked.

    Returns:
      A string describing the attack.
    """
    dmg = random.randint(5, 8)
    enemy.take_damage(dmg)
    return f"{self.name} slams {enemy.name} for {dmg} damage."
