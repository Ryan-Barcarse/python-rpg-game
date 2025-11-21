from enemy_factory import EnemyFactory
from beg_goblin import BegGoblin
from beg_troll import BegTroll
import random

class BeginnerFactory(EnemyFactory):
    """Creates easy enemies for beginner players."""

    def create_random_enemy(self):
        """Randomly selects and returns a beginner enemy"""
        choice = random.choice([BegGoblin, BegTroll])
        return choice()

