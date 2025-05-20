# Tower of Hanoi

I personally designed and wrote the game_logic file including the Node, Stack, and TowerOfHanoi classes' core logic (move validation, win condition, disk manipulation) to solidify my understanding of linked lists and stack operations. AI tools were only utilized for generating the foundational UI setup in the main.py file

## Description
This project implements the Tower of Hanoi puzzle game with a clean separation between game logic and visualization. The game features:
- User-selectable number of disks (1-10) at game start.
- Interactive disk movement via drag-and-drop.
- Visual representation of towers and disks.
- Move counter.
- Win condition detection.

## Setup
1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the game:
   ```
   python main.py
   ```

## How to Play
- At the start, enter the desired number of disks (1-10) and press Enter.
- Click and drag the top disk from a tower and release it over another tower to move it.
- You can only move one disk at a time.
- You cannot place a larger disk on top of a smaller one.
- The goal is to move all disks to the rightmost tower in the same order.

## Project Structure
- `main.py`: Main game file, user interface, and visualization (including disk number selection and drag-and-drop).
- `game_logic.py`: Core game logic implementation (Tower, Stack, Node classes, move validation, win condition). 