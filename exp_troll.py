from entity import Entity
import random

class ExpTroll(Entity):
  """
  Expert-level troll enemy.

  Attributes:
    name: Entity name.
    hp: Starting hit point range: 15-18.
  """
  def __init__(self):
    """
    Initializes the expert troll with a randomized hp.
    """
    super().__init__("Angry Troll", random.randint(15, 18))

  def melee_attack(self, enemy):
    """
    Performs a melee stomp attack on the enemy.

    Args:
      enemy: The entity being attacked.

    Returns:
      A string describing the attack.
    """
    dmg = random.randint(8, 12)
    enemy.take_damage(dmg)
    return f"{self.name} stomps {enemy.name} for {dmg} damage."
