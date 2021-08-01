import pygame


game_screen = pygame.display.set_mode((700, 700))

def show_pieces(image,x,y):
    game_screen.blit(image,(x,y))

def show_pair_pieces(array,x_arr,y_arr):
    for i in range(2):
        game_screen.blit(array[i],(x_arr[i],y_arr[i]))

def show_pawn(array,x_arr,y_arr):
    for i in range(8):
        game_screen.blit(array[i],(x_arr[i],y_arr[i]))


#White chess pieces
white_pawn=[]
white_pawn_x=[]
white_pawn_y=[525]*8
white_pawn_x_ini=28
for i in range(8):
    white_pawn.append(pygame.image.load("pieces/w_pawn.png"))
    white_pawn_x.append(white_pawn_x_ini)
    white_pawn_x_ini+=83

w_rook=[pygame.image.load("pieces/w_rook.png"),pygame.image.load("pieces/w_rook.png")]
w_rook_x=[26,610]
w_rook_y=[612,612]

w_knight=[pygame.image.load("pieces/w_knight.png"),pygame.image.load("pieces/w_knight.png")]
w_knight_x=[109,527]
w_knight_y=[612,612]

w_bishop=[pygame.image.load("pieces/w_bishop.png"),pygame.image.load("pieces/w_bishop.png")]
w_bishop_x=[192,447]
w_bishop_y=[612,612]

w_king=pygame.image.load("pieces/w_king.png")
w_king_x=358
w_king_y=612

w_queen=pygame.image.load("pieces/w_queen.png")
w_queen_x=275
w_queen_y=612

def show_white_pieces():
    show_pawn(white_pawn,white_pawn_x,white_pawn_y)
    show_pair_pieces(w_rook,w_rook_x,w_rook_y)
    show_pair_pieces(w_knight,w_knight_x,w_knight_y)
    show_pair_pieces(w_bishop,w_bishop_x,w_bishop_y)
    show_pieces(w_queen,w_queen_x,w_queen_y)
    show_pieces(w_king,w_king_x,w_king_y)

#Black chess piesces
Black_pawn=[]
Black_pawn_x=[]
Black_pawn_y=[112]*8
Black_pawn_x_ini=28
for i in range(8):
    Black_pawn.append(pygame.image.load("pieces/b_pawn.png"))
    Black_pawn_x.append(Black_pawn_x_ini)
    Black_pawn_x_ini+=83

b_rook=[pygame.image.load("pieces/b_rook.png"),pygame.image.load("pieces/b_rook.png")]
b_rook_x=[26,610]
b_rook_y=[26,26]

b_knight=[pygame.image.load("pieces/b_knight.png"),pygame.image.load("pieces/b_knight.png")]
b_knight_x=[109,527]
b_knight_y=[26,26]

b_bishop=[pygame.image.load("pieces/b_bishop.png"),pygame.image.load("pieces/b_bishop.png")]
b_bishop_x=[192,447]
b_bishop_y=[26,26]

b_king=pygame.image.load("pieces/b_king.png")
b_king_x=358
b_king_y=26

b_queen=pygame.image.load("pieces/b_queen.png")
b_queen_x=275
b_queen_y=26

def show_black_pieces():
    show_pawn(Black_pawn,Black_pawn_x,Black_pawn_y)
    show_pair_pieces(b_rook,b_rook_x,b_rook_y)
    show_pair_pieces(b_knight,b_knight_x,b_knight_y)
    show_pair_pieces(b_bishop,b_bishop_x,b_bishop_y)
    show_pieces(b_queen,b_queen_x,b_queen_y)
    show_pieces(b_king,b_king_x,b_king_y)
