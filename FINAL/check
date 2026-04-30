import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("checkers")
font = pygame.font.Font(None, 36)

# Create the checkerboard
def draw_board():
    for row in range(10):
        for col in range(10):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, "white", (col * 100, row * 100, 100, 100))  # white squares
            else:
                pygame.draw.rect(screen, "black", (col * 100, row * 100, 100, 100))  # black squares

def draw_pieces():  # overlays board wit pieces
    for row in range(10):  # 10x10 grid
        for col in range(10):
            if (row + col) % 2 == 1:
                if row < 3:  # only on bottom rows
                    pygame.draw.circle(screen, "#B30000", (col * 100 + 50, row * 100 + 50), 40)  # red pieces
                elif row > 6:  # only on the top rows
                    pygame.draw.circle(screen, "#0600B2", (col * 100 + 50, row * 100 + 50), 40)  # blue pieces

def user_move(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = event.pos  # Better to use the event's exact click position
        col = pos[0] // 100
        row = pos[1] // 100
        print(f"clicked on row {row}, column {col}")
        
############################################################################################
# based on two sides
def valid_moves_red(piece_pos):
    col, row = piece_pos
    moves = []
    new_row = row + 1
    if 0 <= new_row <= 9:
        if col - 1 >= 0:
            moves.append((col - 1, new_row))
        if col + 1 <= 9:
            moves.append((col + 1, new_row))
    return moves

def valid_moves_blue(piece_pos):
    col, row = piece_pos
    moves = []
    new_row = row - 1
    if 0 <= new_row <= 9:
        if col - 1 >= 0:
            moves.append((col - 1, new_row))
        if col + 1 <= 9:
            moves.append((col + 1, new_row))
    return moves

# finds which func to use
def valid_moves(piece_pos):
    col, row = piece_pos
    # based oni top and last 3 rows
    if row < 3:
        return valid_moves_red(piece_pos)
    elif row > 6:
        return valid_moves_blue(piece_pos)
    # for pieces not in the initial zones (e.g. moved pieces), allow both forward directions
    # (could use color
    moves = []
    moves.extend(valid_moves_red(piece_pos))
    moves.extend(valid_moves_blue(piece_pos))
    #no dupes
    return list(dict.fromkeys(moves))
############################################################################################


# Selection state and message to display
selected_piece = None  # (col, row) of selected piece or None
message = ""  # feedback message shown on screen

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keep the original debug print
        user_move(event)

        # handle clicks for selecting a piece and then a destination
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            col = pos[0] // 100
            row = pos[1] // 100

            if selected_piece is None:
                # select only if there's a piece on that square (dark squares with pieces in initial layout)
                if (row + col) % 2 == 1 and (row < 3 or row > 6):
                    selected_piece = (col, row)
                    message = f"selected piece at {selected_piece}"
                else:
                    message = "no selecteable piece"
            else:
                dest = (col, row)
                moves = valid_moves(selected_piece)
                if dest in moves:
                    message = f"move possible from {selected_piece} to {dest}"
                    # Here you could update the board state to actually move the piece.
                else:
                    message = f"move NOT allowed from {selected_piece} to {dest}"
                selected_piece = None

    # Draw your game here
    screen.fill("black")  # Fill background with color
    draw_board()
    draw_pieces()

    # highlight selected square if any
    if selected_piece is not None:
        sel_col, sel_row = selected_piece
        highlight_rect = pygame.Surface((100, 100), pygame.SRCALPHA)
        highlight_rect.fill(("#FFEA007F"))  # translucent yellow
        
        screen.blit(highlight_rect, (sel_col * 100, sel_row * 100))

    # render the message text
    if message:
        text_surf = font.render(message, True, "yellow")
        screen.blit(text_surf, (10, 960))

    # Update the display
    pygame.display.flip()
