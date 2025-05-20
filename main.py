import pygame
import sys
from game_logic import TowerOfHanoi

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TOWER_WIDTH = 20
TOWER_HEIGHT = 300
DISK_HEIGHT = 30
BASE_COLOR = (139, 69, 19)  # Brown
TOWER_COLOR = (101, 67, 33)  # Dark Brown
DISK_COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
]

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tower of Hanoi")
font = pygame.font.Font(None, 36)

def draw_tower(x, y, disks, selected=False):
    """Draw a tower and its disks at the specified position."""
    # Draw the base
    pygame.draw.rect(screen, BASE_COLOR, (x - 100, y + TOWER_HEIGHT, 200, 20))
    
    # Draw the pole
    pygame.draw.rect(screen, TOWER_COLOR, (x - TOWER_WIDTH//2, y, TOWER_WIDTH, TOWER_HEIGHT))
    
    # Draw the disks
    for i, disk in enumerate(disks):
        disk_width = disk * 40
        disk_x = x - disk_width//2
        disk_y = y + TOWER_HEIGHT - (i + 1) * DISK_HEIGHT
        color = DISK_COLORS[disk - 1]
        pygame.draw.rect(screen, color, (disk_x, disk_y, disk_width, DISK_HEIGHT))
    
    # Highlight selected tower
    if selected:
        pygame.draw.rect(screen, (255, 255, 0), (x - 100, y + TOWER_HEIGHT, 200, 20), 3)

def main():
    game = TowerOfHanoi(num_disks=3)
    selected_tower = None
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Check which tower was clicked
                for i in range(3):
                    tower_x = WINDOW_WIDTH * (i + 1) // 4
                    if abs(x - tower_x) < 100 and y > WINDOW_HEIGHT - TOWER_HEIGHT:
                        if selected_tower is None:
                            selected_tower = i
                        else:
                            if game.move_disk(selected_tower, i):
                                selected_tower = None
                            else:
                                selected_tower = i
        
        # Draw everything
        screen.fill((255, 255, 255))  # White background
        
        # Draw towers
        for i in range(3):
            tower_x = WINDOW_WIDTH * (i + 1) // 4
            tower_y = WINDOW_HEIGHT - TOWER_HEIGHT - 50
            disks = game.get_tower_state(i)
            draw_tower(tower_x, tower_y, disks, i == selected_tower)
        
        # Draw move counter
        moves_text = font.render(f"Moves: {game.get_move_count()}", True, (0, 0, 0))
        screen.blit(moves_text, (10, 10))
        
        # Check for win
        if game.is_game_won():
            win_text = font.render("You Win!", True, (0, 255, 0))
            screen.blit(win_text, (WINDOW_WIDTH//2 - 50, 50))
        
        pygame.display.flip()

if __name__ == "__main__":
    main() 