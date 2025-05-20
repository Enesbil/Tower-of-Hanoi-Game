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
    (128, 0, 128),  # Purple
    (0, 128, 128),  # Teal
    (128, 128, 0)   # Olive
]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
LIGHT_GREY = (200, 200, 200)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tower of Hanoi")
font = pygame.font.Font(None, 36)
input_font = pygame.font.Font(None, 50)

def get_disk_rect(tower_x_center, visual_stack_pos_from_bottom, disk_value):
    disk_width = disk_value * 30 + 20 
    disk_x = tower_x_center - disk_width // 2
    disk_y = (WINDOW_HEIGHT - 50 - TOWER_HEIGHT) + TOWER_HEIGHT - (visual_stack_pos_from_bottom + 1) * DISK_HEIGHT
    return pygame.Rect(disk_x, disk_y, disk_width, DISK_HEIGHT)

def draw_tower(x_center, tower_top_y, disks_logically_ordered, selected=False, disk_to_visually_skip=None):
    pygame.draw.rect(screen, BASE_COLOR, (x_center - 100, tower_top_y + TOWER_HEIGHT, 200, 20))
    pygame.draw.rect(screen, TOWER_COLOR, (x_center - TOWER_WIDTH // 2, tower_top_y, TOWER_WIDTH, TOWER_HEIGHT))

    drawable_disks_list = []
    if disks_logically_ordered:
        if disk_to_visually_skip is not None and disks_logically_ordered[0] == disk_to_visually_skip:
            drawable_disks_list = disks_logically_ordered[1:]
        else:
            drawable_disks_list = list(disks_logically_ordered)
    
    num_drawable_disks = len(drawable_disks_list)
    for k, disk_value in enumerate(drawable_disks_list):
        disk_width = disk_value * 30 + 20
        disk_rect_x = x_center - disk_width // 2
        
        visual_pos_from_bottom = (num_drawable_disks - 1) - k
        disk_rect_y = tower_top_y + TOWER_HEIGHT - (visual_pos_from_bottom + 1) * DISK_HEIGHT
        
        color_idx = (disk_value - 1) % len(DISK_COLORS)
        pygame.draw.rect(screen, DISK_COLORS[color_idx], (disk_rect_x, disk_rect_y, disk_width, DISK_HEIGHT))

    if selected:
        pygame.draw.rect(screen, YELLOW, (x_center - 100, tower_top_y + TOWER_HEIGHT, 200, 20), 3)

def draw_dragged_disk(disk_value, pos):
    if disk_value is None:
        return
    disk_width = disk_value * 30 + 20
    color_index = (disk_value - 1) % len(DISK_COLORS)
    color = DISK_COLORS[color_index]
    pygame.draw.rect(screen, color, (pos[0] - disk_width // 2, pos[1] - DISK_HEIGHT // 2, disk_width, DISK_HEIGHT))

def get_tower_under_mouse(pos):
    for i in range(3):
        tower_x = WINDOW_WIDTH * (i + 1) // 4
        tower_rect = pygame.Rect(tower_x - 50, WINDOW_HEIGHT - 50 - TOWER_HEIGHT, 100, TOWER_HEIGHT + 20)
        if tower_rect.collidepoint(pos):
            return i
    return None

def get_num_disks_screen():
    input_text = ""
    error_message = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        num_disks = int(input_text)
                        if num_disks > 0 and num_disks <= 10:
                            return num_disks
                        elif num_disks > 10:
                            error_message = "Max 10 disks allowed."
                            input_text = ""
                        else:
                            error_message = "Number must be greater than 0."
                            input_text = ""
                    except ValueError:
                        error_message = "Invalid input. Enter a number."
                        input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                    error_message = ""
                elif event.unicode.isdigit():
                    input_text += event.unicode
                    error_message = ""

        screen.fill(WHITE)
        prompt_surf = input_font.render("Enter number of disks (1-10):", True, BLACK)
        screen.blit(prompt_surf, (WINDOW_WIDTH // 2 - prompt_surf.get_width() // 2, WINDOW_HEIGHT // 3))

        input_surf = input_font.render(input_text, True, BLACK)
        input_rect = input_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        pygame.draw.rect(screen, LIGHT_GREY, input_rect.inflate(20, 20))
        screen.blit(input_surf, input_rect)

        if error_message:
            error_surf = font.render(error_message, True, (255,0,0))
            screen.blit(error_surf, (WINDOW_WIDTH // 2 - error_surf.get_width() // 2, WINDOW_HEIGHT // 2 + 50))
        
        pygame.display.flip()

def main():
    num_disks = get_num_disks_screen()
    game = TowerOfHanoi(num_disks=num_disks)
    
    selected_tower_idx = None 
    
    dragging_disk_value = None
    dragging_disk_origin_tower_idx = None
    
    tower_xs = [WINDOW_WIDTH * (i + 1) // 4 for i in range(3)]
    tower_top_render_y = WINDOW_HEIGHT - 50 - TOWER_HEIGHT

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    clicked_tower_idx = get_tower_under_mouse(mouse_pos)
                    
                    if clicked_tower_idx is not None:
                        top_disk_val = game.towers[clicked_tower_idx].peek()
                        if top_disk_val is not None:
                            dragging_disk_value = top_disk_val
                            dragging_disk_origin_tower_idx = clicked_tower_idx
                            selected_tower_idx = None 
                        else: 
                            if selected_tower_idx is not None: 
                                if game.move_disk(selected_tower_idx, clicked_tower_idx):
                                    pass 
                                selected_tower_idx = None
                            else: 
                                pass
                    else: 
                        selected_tower_idx = None 
                        
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and dragging_disk_value is not None:
                    target_tower_idx = get_tower_under_mouse(mouse_pos)
                    
                    if target_tower_idx is not None and target_tower_idx != dragging_disk_origin_tower_idx:
                        game.move_disk(dragging_disk_origin_tower_idx, target_tower_idx)
                    
                    dragging_disk_value = None
                    dragging_disk_origin_tower_idx = None

        screen.fill(WHITE)
        
        for i in range(3):
            tower_x = tower_xs[i]
            disks_on_tower = game.get_tower_state(i) 
            
            current_disk_to_skip = None
            if dragging_disk_value is not None and i == dragging_disk_origin_tower_idx:
                if disks_on_tower and disks_on_tower[0] == dragging_disk_value:
                    current_disk_to_skip = dragging_disk_value
            
            draw_tower(tower_x, tower_top_render_y, disks_on_tower, 
                       selected=(i == selected_tower_idx and dragging_disk_value is None), 
                       disk_to_visually_skip=current_disk_to_skip)

        if dragging_disk_value is not None:
            draw_dragged_disk(dragging_disk_value, mouse_pos)

        moves_text = font.render(f"Moves: {game.get_move_count()}", True, BLACK)
        screen.blit(moves_text, (10, 10))

        if game.is_game_won():
            win_text = font.render("You Win!", True, (0,128,0))
            screen.blit(win_text, (WINDOW_WIDTH // 2 - win_text.get_width() // 2, 50))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False 
            
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 