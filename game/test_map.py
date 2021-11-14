
import pgzrun
import random

ok=2
WIDTH = 800
HEIGHT = 600
SIZE_TANK=25
walls,walls_2,walls_3=[],[],[]
river_full,river_full_2,river_full_3=[],[],[]
bullets=[]
stone_walls,stone_walls_2,stone_walls_3=[],[],[]
cau,cau_2,cau_3=[],[],[]
enemies_1=[]
enemies_2=[]
enemies_3=[]
enemy_bullets=[]
bullet_holdoff_ally=0
bullet_holdoff_enemies=0
game_over=False
enemy_move_count=0
speed_bullet=5
check_map_2=5
check_map_3=5
start_game=False
background_begin=Actor('begin')
background_finish=Actor('begin')
chedo1=Actor('one_player_1')
chedo1.pos=(443,320)
start_game=False
play_again=Actor('multi_players')
#home
home=Actor('cong1')
home.pos=(WIDTH/2,35)
background=Actor('grass')
walls_img=[[1, 15], [1, 0], [2, 15], [2, 0], [3, 15], [3, 14], [3, 13], [3, 12], [3, 11], [3, 10], [3, 5], [3, 4],
 [3, 3], [3, 2], [3, 1], [3, 0],[7, 15], [7, 14], [7, 13], [7, 12], [7, 9], [7, 8], [7, 7], [7, 6], [7, 3], [7, 2],
[7, 1], [7, 0], [8, 15], [8, 12], [8, 9],[8, 6], [8, 3], [8, 0], [9, 15], [9, 12], [9, 9], [9, 6], [9, 3], [9, 0]
,[11,6],[10,6],[9,7],[9,8],[10,9],[11,9],
[0,6],[1,6],[2,6],[2,7],[2,8],[2,9],[1,9],[0,9]
]

#map2

for i in walls_img:
    wall=Actor('wall')
    wall.y=i[0]*50+SIZE_TANK
    wall.x=i[1]*50+SIZE_TANK
    walls.append(wall) 

def draw():
    background.draw()
    home.draw()
    for wall in walls:
        wall.draw()






pgzrun.go()
