from abc import ABC, abstractmethod

class EnemyFactory(ABC):
  """
  Abstract factory used to create enemy objects.
  """
  @abstractmethod
  def create_random_enemy(self):
    """
    Creates and returns an enemy object.

    Returns:
      A new enemy instance.
    """
    pass
