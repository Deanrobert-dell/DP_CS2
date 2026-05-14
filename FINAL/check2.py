import pygame
import random
import time
def all():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("checkers")
    font = pygame.font.Font(None, 36)

    # 10 x ten boatd
    board = {}
    for row in range(10):
        for col in range(10):
            if (row + col) % 2 == 1:
                if row < 3:

                    board[(col, row)] = "red"
                elif row > 6:
                    board[(col, row)] = "blue"
    class Color:
        def __init__(self, hex_value): 
            self.hex_value = hex_value

    def draw_board():
        for row in range(10):
            for col in range(10):
                color = Color("#FFFFFF") if (row + col) % 2 == 0 else Color("#000000")  # defines which square is which color
                pygame.draw.rect(screen, color.hex_value, (col * 100, row * 100, 100, 100))

    def draw_pieces():
        for (col, row), color in board.items():
            hex_color = Color("#B30000") if color == "red" else Color("#0600B2") #piece colors
            pygame.draw.circle(screen, hex_color.hex_value, (col * 100 + 50, row * 100 + 50), 40)

    def move1(piece_pos):
        #Returns the two needed lists for move snad attacks
        if piece_pos not in board:
            return [], []
        
        col, row = piece_pos
        color = board[piece_pos]
        standard_moves = []
        jump_moves = {} # 
        
        # =1 -1 for up/donw
        row_direction = 1 if color == "red" else -1
        target_row = row + row_direction
        jump_row = row + (row_direction * 2)
        
        for col_offset in [-1, 1]:
            target_col = col + col_offset
            # Check standard diagonal moves
            if 0 <= target_row <= 9 and 0 <= target_col <= 9:
                if (target_col, target_row) not in board:
                    standard_moves.append((target_col, target_row))

                # Check jump moves if the diagonal contains an enemy piece
                elif board[(target_col, target_row)] != color:
                    landing_col = col + (col_offset * 2) # basically mulkts by 2 to land on spot AFTER the piece
                    if 0 <= jump_row <= 9 and 0 <= landing_col <= 9:
                        if (landing_col, jump_row) not in board:
                            jump_moves[(landing_col, jump_row)] = (target_col, target_row)
                            
        return standard_moves, jump_moves

    def move_piece(start, end, captured_piece=None):
        nonlocal current_turn, message, game_over
        if start in board:
            color = board.pop(start)
            board[end] = color
            
            if captured_piece:
                board.pop(captured_piece)
                message = f"{color. capitalize()} scored at {captured_piece} "
            else:
                message = f"{color.capitalize()} moved from {start} to {end}"
                
            # checks for winner
            if checkwin():
                game_over = True
                return

            # other turn
            current_turn = "red" if current_turn == "blue" else "blue"

    def checkwin():
        nonlocal message
        red_count = sum(1 for color in board.values() if color == "red")
        blue_count = sum(1 for color in board.values() if color == "blue")
        
        if red_count == 0:
            message = "BLUE WON, CLOSE PROGRAM"
            return True
        #
        elif blue_count == 0:
            message = " RED WON, CLOSE PROGRAM"
            return True
        return False

    def ai_move():
        nonlocal message, game_over #fixed
        if game_over:
            return

        movable_pieces = []
        jump_pieces = []
        
        # each red option
        for pos, color in board.items():
            if color == "red":
                standards, jumps = move1(pos)
                if jumps:
                    jump_pieces.append((pos, jumps))
                if standards:
                    movable_pieces.append((pos, standards))
                    
        time.sleep(0.4) #delays and then ai moves
        
        # jumps and attacks if possible always
        if jump_pieces:
            start, jumps_dict = random.choice(jump_pieces)
            end = random.choice(list(jumps_dict.keys()))
            captured = jumps_dict[end]
            move_piece(start, end, captured)
        elif movable_pieces:
            start, possible_ends = random.choice(movable_pieces)
            end = random.choice(possible_ends)
            move_piece(start, end)
        else:
            message = "Ai cant move- blue wins, CLOSE PROGRAM" #say close program because couldnt implement quit
            game_over = True

    # Game Variables
    selected_piece = None
    message = "blue choose"
    current_turn = "blue" 
    game_over = False
    running = True

    while running:
        # ai CLANKER
        if current_turn == "red" and not game_over:
            # render frame firts
            screen.fill("black")
            draw_board()
            draw_pieces()
            text_surf = font.render(message, True, "#00B115") #MAKES IT SEEM LIKE YOU CHOSE CORRECT CHOICE WHEN USING GREEN AFTER RED FOR CONTRAST
            screen.blit(text_surf, (10, 960))
            pygame.display.flip()
            
            ai_move()

        # player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if current_turn == "blue" and not game_over and event.type == pygame.   MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                col = pos[0] // 100
                row = pos[1] // 100
                clicked_square = (col, row)
                
                if selected_piece is None:
                    if board.get(clicked_square) == "blue":
                        selected_piece = clicked_square
                        message = f"selction on  {selected_piece}" #ecognizes chosen pieces, (kept this from prototype because its usefule)
                    else:
                        message = "invalid"
                else:
                    standards, jumps = move1(selected_piece)
                    
                    # cehck valid moves
                    if clicked_square in jumps:
                        captured = jumps[clicked_square]
                        move_piece(selected_piece, clicked_square, captured)
                    # same
                    elif clicked_square in standards:
                        move_piece(selected_piece, clicked_square)
                    else:
                        message = "move not allowed. reset"
                    selected_piece = None

        # fills black 
        screen.fill("black")
        draw_board()
        draw_pieces()
        
        # highlight block
        if selected_piece is not None:
            sel_col, sel_row = selected_piece
            highlight_rect = pygame.Surface((100, 100), pygame.SRCALPHA) #userd in transparent backgrounds (srcalpha)
            highlight_rect.fill((255, 234, 0, 127)) 
            screen.blit(highlight_rect, (sel_col * 100, sel_row * 100))
            
        # displays the text
        if message:
            text_surf = font.render(message, True, "#AE0000" if not game_over else "green")
            screen.blit(text_surf, (10, 960))
            
        pygame.display.flip()

        
    pygame.quit()

