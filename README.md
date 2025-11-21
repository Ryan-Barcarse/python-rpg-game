# Python RPG Combat Engine

A text-based RPG combat game built using Object Oriented Programming, inheritance, and the Factory design pattern.  
This game prompts the user to attack 1 of 3 potential monsters that can vary in strength. The user rolls die to determine
the power output of their weapon, winning the game if all monsters are slain.

## Features

**Object-Oriented Architecture:**
  - Abstract Entity class for all characters
  - Inheritance for Hero, beginner enemies, and expert enemies
  - Encapsulated HP, names, and attack behaviors

**Enemy Factory System:**  
  - Beginner Factory generates easy goblins and trolls
  - Expert Factory generates harder goblins and trolls
  - Uses the Factory Design Pattern to scale enemy types

**Combat System:**
  - Melee attacks, ranged attacks 
  - Enemy attacks with random damage ranges
  - HP tracking and damage handling
  - Randomized stats for replayability

**Input Validation:**
  - Uses check_input.py for robust user inputs

## Technologies Used

- **Python 3**
- Object-Oriented Programming (OOP)
- Inheritance & Abstraction
- Factory Design Pattern
- Randomized game logic

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rpg-combat-engine.git
   cd rpg-combat-engine


