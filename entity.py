from abc import ABC, abstractmethod

class Entity(ABC):
  """
  Abstract base class representing any character in the game.

  Attributes:
    _name: The name of the entity.
    _hp: The current hit points of the entity.
  """
  def __init__(self, name, hp):
    """
    Initializes the entity with a name and hit points.

    Args:
      name: The name of the entity.
      hp: The starting hit points of the entity.
    """
    self._name = name
    self._hp = hp

  @property
  def name(self):
    """
    Returns the entity's name.

    Returns:
      The name of the entity.
    """
    return self._name

  @property
  def hp(self):
    """
    Returns the current hit points of the entity.

    Returns:
      The entity's remaining hit points.
    """
    return self._hp

  def take_damage(self, damage):
    """
    Reduces the entity's hit points by a given amount.
    Does not allow hit points to go below zero.

    Args:
      damage: The amount of damage to subtract from hit points.

    Returns:
      None.
    """
    self._hp -= damage
    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    """
    Returns a formatted string representation of the entity.

    Returns:
      A string showing the entity's name and current hp.
    """
    return f"{self._name} HP: {self._hp}"

  @abstractmethod
  def melee_attack(self, enemy):
    """
    Abstract method enforcing that all subclasses implement a melee attack.

    Args:
      enemy: The entity that is being attacked.

    Returns:
      A string describing the attack.
    """
    pass
