from enemy_factory import EnemyFactory
from exp_troll import ExpTroll
from exp_goblin import ExpGoblin
import random

class ExpertFactory(EnemyFactory):
  """
  Factory responsible for creating expert-level enemies.

  Attributes:
    None.
  """
  def create_random_enemy(self):
    """
    Constructs and returns a randomly selected expert enemy.

    Returns:
      An instance of either ExpGoblin or ExpTroll.
    """
    enemy_class = random.choice([ExpGoblin, ExpTroll])
    return enemy_class()
