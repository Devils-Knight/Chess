# importing the pygame module along with other modules
import pygame
import random
from pygame import mixer
from pieces import *

pygame.init()
# game_screen = pygame.display.set_mode((700, 700)) # creating a gamescreen of 900 * 700 pixels
game_state = "running"

pygame.display.set_caption("Chess")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

background_image=pygame.image.load("board.jpg")


player=1
#white pawn,rook,knight,bishop,queen,king
w_pieces_loc_x=[*white_pawn_x,*w_rook_x,*w_knight_x,*w_bishop_x,w_queen_x,w_king_x]
w_pieces_loc_y=[*white_pawn_y,*w_rook_y,*w_knight_y,*w_bishop_y,w_queen_y,w_king_y]

# black pawn,rook,knight,bishop,queen,king
b_pieces_loc_x=[*Black_pawn_x,*b_rook_x,*b_knight_x,*b_bishop_x,b_queen_x,b_king_x]
b_pieces_loc_y=[*Black_pawn_y,*b_rook_y,*b_knight_y,*b_bishop_y,b_queen_y,b_king_y]


path=pygame.image.load("path.png")
show_path_flag=0

def show_pawn_movement(player,x,y):
    y-=80*(player)
    game_screen.blit(path,(x,y))
    x_lis=[x]
    y_lis=[y]
    mov_x=0
    mov_y=1
    # if player == 1:
    #     for i in range(16):
    #         if x in range(b_pieces_loc_x[i]-40,b_pieces_loc_x[i]+40) and y in range(b_pieces_loc_y[i]-40,b_pieces_loc_y[i]+40):
    #             if x<b_pieces_loc_x[i]:
    #                 x_lis.append(x+80)
    #                 y_lis.append(y)
    #                 mov_x.append(1)
    #                 mov_y.append(1)
    #             else:
    #                 x_lis.append(x-80)
    #                 y_lis.append(y)
    #                 mov_x.append(-1)
    #                 mov_y.append(1)
    return [x,y,mov_x,mov_y]

def move_pawn(player,image,x,y):
    y-=80*(player)
    game_screen.blit(image,(x,y))

def click(player,m_pos,arr_x,arr_y):
    for i in range(8):
        if m_pos[0] in range(arr_x[i]-40,arr_x[i]+40) and m_pos[1] in range(arr_y[i]-40,arr_y[i]+40):
            val=show_pawn_movement(player,arr_x[i],arr_y[i])
            val.append(i)
            return val
    return -1

movement_flag=0
def movement(player,m_pos,mov_pos,x,y,i):
    print("inside mov func")
    if player==1:
        if m_pos[0] in range(mov_pos[0]-40,mov_pos[0]+40) and m_pos[1] in range(mov_pos[1]-40,mov_pos[1]+40):
            print("movement pass")
            x_loc=w_pieces_loc_x[i]-(x*80*player)
            y_loc=w_pieces_loc_y[i]-(y*80*player)
            return [x_loc,y_loc]
    else:
        if m_pos[0] in range(mov_pos[0]-40,mov_pos[0]+40) and m_pos[1] in range(mov_pos[1]-40,mov_pos[1]+40):
            print("movement pass")
            x_loc=b_pieces_loc_x[i]-(x*80*player)
            y_loc=b_pieces_loc_y[i]-(y*80*player)
            return [x_loc,y_loc]
    return -1

def update_location(player,i,x,y):
    print("inside upd func")
    if player == 1:
        if i<8:
            white_pawn_x[i]=x
            white_pawn_y[i]=y
            w_pieces_loc_x[i]=x
            w_pieces_loc_y[i]=y
    else:
        if i<8:
            Black_pawn_x[i]=x
            Black_pawn_y[i]=y
            b_pieces_loc_x[i]=x
            b_pieces_loc_y[i]=y

                

while game_state is "running":
    game_screen.fill((255,255,255))
    game_screen.blit(background_image,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = "stop"
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            global path_loc
            if player == 1:
                path_loc=click(1,mouse_pos,w_pieces_loc_x,w_pieces_loc_y)
                if path_loc==-1:
                    show_path_flag=0
                else:
                    show_path_flag=1
                    temp_loc=path_loc
                
                if movement_flag==1:
                    print("inside movement")
                    move=movement(1,mouse_pos,(temp_loc[0],temp_loc[1]),temp_loc[2],temp_loc[3],temp_loc[4])
                    if move!=-1:
                        print("inside update")
                        update_location(1,temp_loc[4],move[0],move[1])
                        player=-1
                    movement_flag=0
            else:
                path_loc=click(-1,mouse_pos,b_pieces_loc_x,b_pieces_loc_y)
                if path_loc==-1:
                    show_path_flag=0
                else:
                    show_path_flag=1
                    temp_loc=path_loc
                
                if movement_flag==1:
                    print("inside movement")
                    move=movement(-1,mouse_pos,(temp_loc[0],temp_loc[1]),temp_loc[2],temp_loc[3],temp_loc[4])
                    if move!=-1:
                        print("inside update")
                        update_location(-1,temp_loc[4],move[0],move[1])
                        player=1
                    movement_flag=0
                


        if event.type == pygame.MOUSEBUTTONUP:
            pass
                    
    if show_path_flag==1:
        # print(path_loc)
        game_screen.blit(path,(path_loc[0],path_loc[1]))
        movement_flag=1 
    
    show_white_pieces()
    show_black_pieces()
    

    pygame.display.update()