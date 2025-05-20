# Tower of Hanoi

A Python implementation of the classic Tower of Hanoi puzzle game with a graphical interface.

## Description
This project implements the Tower of Hanoi puzzle game with a clean separation between game logic and visualization. The game features:
- Interactive disk movement
- Visual representation of towers and disks
- Move counter
- Win condition detection

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
- Click on a tower to select a disk
- Click on another tower to move the selected disk
- You can only move one disk at a time
- You cannot place a larger disk on top of a smaller one
- The goal is to move all disks to the rightmost tower in the same order

## Project Structure
- `main.py`: Main game file and visualization
- `game_logic.py`: Core game logic implementation 