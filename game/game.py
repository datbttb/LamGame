import pgzrun
import random

# Cài đặt chiều dài và rộng của màn hình
WIDTH = 800
HEIGHT = 600

# Độ lớn mặc định của tank(dùng để sep up các chướng ngại vật trong map không bị thừa)
SIZE_TANK=25

# Khởi tạo các mảng chứa các vật thể tạo map
map=1
walls,walls_2,walls_3=[],[],[]
river_full,river_full_2,river_full_3=[],[],[]
bullets=[]
stone_walls,stone_walls_2,stone_walls_3=[],[],[]
cau,cau_2,cau_3=[],[],[]

# Khởi tạo mảng chứa quân địch
enemies_1=[]
enemies_2=[]
enemies_3=[]

# Các biến chứa các thông tin của đạn
bullet_holdoff_ally=0
bullet_holdoff_enemies=0
enemy_bullets=[]
enemy_move_count=0
speed_bullet=5

# Điều kiện để đưa các vị ví các vật thể của từng map vào trong map
check_map_2=5
check_map_3=5

# Điều kiện để im ra màn hình bắt đầu, kết thúc và chiến thắng 
game_over=False
start_game=False
game_win=False

# Đưa các background vào trong game
background=Actor('grass')
background_begin=Actor('dinhdoclap')
background_finish=Actor('chienthang')

# cổng dinh
cong_dinh=Actor('cong1')
cong_dinh.pos=(WIDTH/2,35)
huc_cong=[]
huc_cong.append(cong_dinh)

# nút chơi lại
play_again=Actor('again')
play_again.pos=(400,200)

# nút menu
main_menu=Actor('menu')
main_menu.pos=(400,350)

# các chế độ
che_do_1=Actor('one_player_1')
che_do_1.pos=(403,320)
che_do_2=Actor('multi_players')
che_do_2.pos=(403,370)

# Số lượng tank
number_tank_ally=0
tank_ally_alive=0

# Nhà chính
home=Actor('home')
home.pos=(WIDTH/2,HEIGHT-35)
home1=[]
home1.append(home)
#tank ally
tank=Actor('tank_vn_2')
tank.pos=(WIDTH/2+200,HEIGHT-25)
tank.angle=90
#yank ally 2
tank_2=Actor('tank_vn')
tank_2.pos=(WIDTH/2-200,HEIGHT-25)
tank_2.angle=90

# Vị trí các vật thể map 1
walls_img=[[1, 15], [1, 0], [2, 15], [2, 0], [3, 15], [3, 14], [3, 13], [3, 12], [3, 11], [3, 10], [3, 5], [3, 4],
 [3, 3], [3, 2], [3, 1], [3, 0],[7, 15], [7, 14], [7, 13], [7, 12], [7, 9], [7, 8], [7, 7], [7, 6], [7, 3], [7, 2],
[7, 1], [7, 0], [8, 15], [8, 12], [8, 9],[8, 6], [8, 3], [8, 0], [9, 15], [9, 12], [9, 9], [9, 6], [9, 3], [9, 0], 
 [11,6], [10,6], [9,7], [9,8], [10,9], [11,9]]

bridges_img=[[5,12],[5,3]]
rivers_img=[[5,15],[5,14],[5,13],[5,11],[5,10],[5,9],[5,8],[5,7],[5,6],[5,5],[5,4],[5,2],[5,1],[5,0]]
stones_wall_img=[[3, 9], [3, 8], [3, 7], [3, 6], [6,9],[6,8],[6,7],[6,6]]

# Cài đặt map 1
def set_map_1():
    global check_map_2,check_map_3
    check_map_3=5
    check_map_2=5
    enemies_1.clear()
    walls.clear()
    river_full.clear()
    stone_walls.clear()
    cau.clear()
    for i in range(2):
        enemy=Actor('tank_red')
        enemy.x=i*100+100
        enemy.y=SIZE_TANK
        enemy.angle=270
        enemies_1.append(enemy)
    for i in rivers_img:
        part_river=Actor('river')
        part_river.y=i[0]*50+SIZE_TANK
        part_river.x=i[1]*50+SIZE_TANK
        river_full.append(part_river)

    for i in bridges_img:
        cau1phan=Actor('brigde')
        cau1phan.y=i[0]*50+SIZE_TANK
        cau1phan.x=i[1]*50+SIZE_TANK
        cau.append(cau1phan)

    for i in walls_img:
        wall=Actor('wall')
        wall.y=i[0]*50+SIZE_TANK
        wall.x=i[1]*50+SIZE_TANK
        walls.append(wall)   

    for i in stones_wall_img:
        stone_wall=Actor('stone')
        stone_wall.y=i[0]*50+SIZE_TANK
        stone_wall.x=i[1]*50+SIZE_TANK
        stone_walls.append(stone_wall)
set_map_1()

# Vị trí các vật thể của map 2
walls_img_2=[[2, 15], [2, 14], [2, 13], [2, 11], [2, 9], [2, 8], [2, 7], [2, 6], [2, 4], [2, 2], [2, 1], [2, 0],
            [1, 9], [1, 6], [3, 13], [3, 11], [3, 9], [3, 6], [3, 4], [3, 2], [4, 13], [4, 11], [4, 4], [4, 2],
            [5, 13], [5, 11], [5, 4], [5, 2], [6, 13], [6, 11], [6, 9], [6, 6], [6, 4], [6, 2], [7, 13], [7, 11],
            [7, 9], [7, 8], [7, 7], [7, 6], [7, 4], [7, 2], [8, 15],[8, 14], [8, 13], [8, 11], [8, 9], [8, 6],
            [8, 4], [8, 2], [8, 1], [8, 0],[9, 9], [9, 6], [10, 14], [10, 13], [10, 12], [10, 11], [10, 4], [10, 3], 
            [10, 2], [10, 1], [11,6], [10,6], [9,7], [9,8], [10,9], [11,9]]
walls_2=[]

# cài đặt map 2
def set_map_2():
    for i in walls_img_2:
        wall=Actor('wall')
        wall.y=i[0]*50+SIZE_TANK
        wall.x=i[1]*50+SIZE_TANK
        walls_2.append(wall) 
    for i in range(2):

        enemy=Actor('tank_red')
        enemy.x=i*100+100
        enemy.y=SIZE_TANK
        enemy.angle=270
        enemies_2.append(enemy)


# các vị trí vật thể trong map 3
walls_img_3=[[5, 13], [5, 2], [6, 14], [6, 12], [6, 3], [6, 2], [6, 1], [7, 14], [7, 13], [7, 12], [7, 3], [7, 2], [7, 1],
            [8, 10], [8, 9], [8, 8], [8, 7], [8, 6], [8, 5],[9, 10], [9, 5], [10, 10], [10, 5], [11, 10], [11, 5],[6,13]
            ,[11,6],[10,6],[9,7],[9,8],[10,9],[11,9],[0,6],[1,6],[2,6],[2,7],[2,8],[2,9],[1,9],[0,9]]
bridges_img_3=[]
rivers_img_3=[]
stones_wall_img_3=[[3, 15], [3, 12], [3, 11], [3, 8], [3, 7], [3, 4], [3, 3], [3, 0], [4, 15], [4, 12], [4, 11], [4, 8], [4, 7],
                [4, 4], [4, 3], [4, 0],[9, 15],[9, 0],[10, 0],[10, 15],[11, 0],[11, 15]]

# cài đặt map 3
def set_map_3():
    for i in range(2):

        enemy=Actor('tank_red')
        enemy.x=i*100+100
        enemy.y=SIZE_TANK
        enemy.angle=270
        enemies_3.append(enemy)    
    for i in rivers_img_3:
        part_river=Actor('river')
        part_river.y=i[0]*50+SIZE_TANK
        part_river.x=i[1]*50+SIZE_TANK
        river_full_3.append(part_river)

    for i in bridges_img_3:
        cau1phan=Actor('brigde')
        cau1phan.y=i[0]*50+SIZE_TANK
        cau1phan.x=i[1]*50+SIZE_TANK
        cau_3.append(cau1phan)

    for i in walls_img_3:
        wall=Actor('wall')
        wall.y=i[0]*50+SIZE_TANK
        wall.x=i[1]*50+SIZE_TANK
        walls_3.append(wall)   

    for i in stones_wall_img_3:
        stone_wall=Actor('stone')
        stone_wall.y=i[0]*50+SIZE_TANK
        stone_wall.x=i[1]*50+SIZE_TANK
        stone_walls_3.append(stone_wall)    


# Cài đặt tank1
def tank_set(tank): 
    global game_win
    original_x=tank.x
    original_y=tank.y
    if keyboard.left : # nhấn mũi tên sang trái để đi sang trái
        tank.x-=2
        tank.angle=180
    if keyboard.right: # nhấn mũi tên sang phải để đi sang phải
        tank.x+=2
        tank.angle=0

    if keyboard.up: # nhấn mũi tên lên để đi thẳng
        tank.y-=2
        tank.angle=90

    if keyboard.down: # nhấn mũi tên xuống để đi lùi
        tank.y+=2
        tank.angle=270 

    if tank.collidelist(home1)!=-1: # không cho đi qua nhà
        tank.x=original_x
        tank.y=original_y

    if tank.collidelist(huc_cong)!=-1 and map==3: # khi húc vào cổng thì sẽ thắng
        game_win=True

    if tank.collidelist(walls or walls_2 or walls_3)!=-1: # không cho đi qua tường
        tank.x=original_x
        tank.y=original_y

    if tank.collidelist(stone_walls or stone_walls_2 or stone_walls_3)!=-1: # không cho đi qua tường đá
        tank.x=original_x
        tank.y=original_y   

    if tank.collidelist(river_full or river_full_2 or river_full_3)!=-1: # không cho đi qua sông
        tank.x=original_x
        tank.y=original_y

    if tank.x>(WIDTH-SIZE_TANK) or tank.x<SIZE_TANK or tank.y>(HEIGHT-SIZE_TANK) or tank.y<SIZE_TANK: # không cho ra khỏi map
        tank.x=original_x
        tank.y=original_y

# Cài đặt tank 2
def tank_set_2(tank): 
    original_x=tank.x
    original_y=tank.y
    if keyboard.a : # nhấn a để đi sang trái
        tank.x-=2
        tank.angle=180
    if keyboard.d: # nhấn d để đi sang phải 
        tank.x+=2
        tank.angle=0

    if keyboard.w: # nhấn w để tiến lên
        tank.y-=2
        tank.angle=90

    if keyboard.s: # nhấn s để lùi xuống
        tank.y+=2
        tank.angle=270 
    if tank.collidelist(home1)!=-1: # chạm vào nhà thì không đi được
        tank.x=original_x
        tank.y=original_y

    if tank.collidelist(walls or walls_2 or walls_3)!=-1: # không cho đi xuyên tường
        tank.x=original_x
        tank.y=original_y

    if tank.collidelist(stone_walls or stone_walls_2 or stone_walls_3)!=-1: # không cho đi qua tường đá
        tank.x=original_x
        tank.y=original_y   

    if tank.collidelist(river_full or river_full_2 or river_full_3)!=-1: # không cho tank đi qua sông
        tank.x=original_x
        tank.y=original_y

    if tank.x>(WIDTH-SIZE_TANK) or tank.x<SIZE_TANK or tank.y>(HEIGHT-SIZE_TANK) or tank.y<SIZE_TANK: # không cho tank đi ra khỏi map
        tank.x=original_x
        tank.y=original_y

# Cài đặt đạn tank1 mình
def tank_bullets_set(tank):
    global bullet_holdoff_ally,game_over
    if bullet_holdoff_ally==0:
        if keyboard.space:
            bullet=Actor('bulletblue2')
            bullet.angle=tank.angle
            if bullet.angle==0:
                bullet.pos= (tank.x+SIZE_TANK,tank.y)
            if bullet.angle==180:
                bullet.pos= (tank.x-SIZE_TANK,tank.y)
            if bullet.angle==90:
                bullet.pos= (tank.x,tank.y-SIZE_TANK)
            if bullet.angle==270: 
                bullet.pos= (tank.x,tank.y+SIZE_TANK)
            bullets.append(bullet)
            bullet_holdoff_ally=20
    else: 
        bullet_holdoff_ally-=1

# Cài đặt đạn tank2 mình
def tank_2_bullets_set(tank):
    global bullet_holdoff_ally,game_over
    if bullet_holdoff_ally==0:
        if keyboard.c:
            bullet=Actor('bulletgreen2')
            bullet.angle=tank.angle
            if bullet.angle==0:
                bullet.pos= (tank.x+SIZE_TANK,tank.y)
            if bullet.angle==180:
                bullet.pos= (tank.x-SIZE_TANK,tank.y)
            if bullet.angle==90:
                bullet.pos= (tank.x,tank.y-SIZE_TANK)
            if bullet.angle==270: 
                bullet.pos= (tank.x,tank.y+SIZE_TANK)
            bullets.append(bullet)
            bullet_holdoff_ally=20
    else: 
        bullet_holdoff_ally-=1

# Cài đặt tốc độ di chuyển của đạn và khi va chạm với vật thể khác
def tank_bullet():
    global game_over
    for bullet in bullets:
        if bullet.angle==0:
            bullet.x+=5
        if bullet.angle==180:
            bullet.x-=5
        if bullet.angle==90:
            bullet.y-=5
        if bullet.angle==270:
            bullet.y+=5

    for bullet in bullets:
        # khi đạn chạm vào gạch sẽ biến mất và xóa gạch
        walls_index=bullet.collidelist(walls) 
        if walls_index!=-1:
            sounds.gun9.play()
            del walls[walls_index]
            bullets.remove(bullet)

        walls_index=bullet.collidelist(walls_2) 
        if walls_index!=-1:
            sounds.gun9.play()
            del walls_2[walls_index]
            bullets.remove(bullet)
        
        walls_index=bullet.collidelist(walls_3)
        if walls_index!=-1:
            sounds.gun9.play()
            del walls_3[walls_index]
            bullets.remove(bullet)

        # Khi đạn chạm vào nhà sẽ xóa nhà và thua
        if bullet.collidelist(home1)!=-1:
            game_over=True

        # Khi chạm vào đá sẽ biến mất
        stone_walls_index=bullet.collidelist(stone_walls or stone_walls_2 or stone_walls_3)
        if stone_walls_index!=-1:
            bullets.remove(bullet)

        # khi đạn ra ngoài màn hình sẽ xóa đạn
        if bullet.x<0 or bullet.x>WIDTH or bullet.y<0 or bullet.y>HEIGHT:
            bullets.remove(bullet)

        # Khi đạn chạn vào địch sẽ xóa đạn và địch
        bullet_index= bullet.collidelist(enemies_1 )
        if bullet_index!=-1:
            sounds.exp.play()
            bullets.remove(bullet)
            del enemies_1[bullet_index]
        bullet_index= bullet.collidelist(enemies_2)
        if bullet_index!=-1:
            sounds.exp.play()
            bullets.remove(bullet)
            del enemies_2[bullet_index]
        bullet_index= bullet.collidelist(enemies_3)
        if bullet_index!=-1:
            sounds.exp.play()
            bullets.remove(bullet)
            del enemies_3[bullet_index]

# Cài đặt xe tank địch
def enemy_set(enemies_1):
    global enemy_move_count,bullet_holdoff_enemies,game_over,tank_ally_alive
    
    for enemy in enemies_1:
        original_x=enemy.x
        original_y=enemy.y
        choice=random.randint(0,2)
        if enemy_move_count>0:
            enemy_move_count-=1
            if enemy.angle==0:
                enemy.x+=2
            elif enemy.angle==180:
                enemy.x-=2
            elif enemy.angle==90:
                enemy.y-=2
            elif enemy.angle==270:
                enemy.y+=2

            if enemy.x<SIZE_TANK or enemy.x>(WIDTH-SIZE_TANK) or enemy.y<SIZE_TANK or enemy.y>(HEIGHT-SIZE_TANK): # không cho tank địch đi qua map 
                enemy.x=original_x
                enemy.y=original_y
                enemy_move_count=0
                
            if enemy.collidelist(walls or walls_2 or walls_3)!=-1: # không cho tank địch đi qua tường 
                enemy.x=original_x
                enemy.y=original_y
                enemy_move_count=0

            if enemy.collidelist(stone_walls or stone_walls_2 or stone_walls_3)!=-1: # không cho tank địch đi qua tường đá
                enemy.x=original_x
                enemy.y=original_y
                enemy_move_count=0

            if enemy.collidelist(river_full or river_full_2 or river_full_3)!=-1: # không cho tank địch đi qua sông
                enemy.x=original_x
                enemy.y=original_y
                enemy_move_count=0

        # sử dụng random để tạo di chuyển cho tank địch và bắn đạn
        elif choice==0:
            enemy_move_count=30
        elif choice==1:
            enemy.angle=random.randint(0,3)*90
        else:
            if bullet_holdoff_enemies==0:
                bullet=Actor('bulletred2')
                bullet.angle=enemy.angle
                bullet.pos=enemy.pos
                enemy_bullets.append(bullet )
                bullet_holdoff_enemies=10
            else:
                bullet_holdoff_enemies-=1

        # khi va chạm vs tank mình, tank mình sẽ biến mất
        if enemy.colliderect(tank):
            tank.pos=(-100,-100)
            tank_ally_alive-=1
        if enemy.colliderect(tank_2):
            tank_2.pos=(-100,-100)
            tank_ally_alive-=1            
        if tank_ally_alive==0:
            game_over=True

# Cài đặt đạn xe tăng địch
def enemy_bullets_set():
    global game_over,tank_ally_alive
    for bullet in enemy_bullets:
        if bullet.angle==0:
            bullet.x+=speed_bullet
        if bullet.angle==180:
            bullet.x-=speed_bullet
        if bullet.angle==90:
            bullet.y-=speed_bullet
        if bullet.angle==270:
            bullet.y+=speed_bullet
        for bullet in enemy_bullets:

            wall_index=bullet.collidelist(walls)
            if wall_index!=-1:
                sounds.gun10.play()
                del walls[wall_index]
                enemy_bullets.remove(bullet)

            wall_index=bullet.collidelist(walls_2)
            if wall_index!=-1:
                sounds.gun10.play()
                del walls_2[wall_index]
                enemy_bullets.remove(bullet)

            wall_index=bullet.collidelist(walls_3)
            if wall_index!=-1:
                sounds.gun10.play()
                del walls_3[wall_index]
                enemy_bullets.remove(bullet)

            if bullet.collidelist(home1)!=-1:
                game_over=True

            stone_walls_index=bullet.collidelist(stone_walls or stone_walls_2 or stone_walls_3)
            if stone_walls_index!=-1:
                enemy_bullets.remove(bullet)

            if bullet.x<0 or bullet.x>WIDTH or bullet.y<0 or bullet.y>HEIGHT:
                enemy_bullets.remove(bullet)

            if bullet.colliderect(tank):
                tank.pos=(-100,-100)
                tank_ally_alive-=1

            if bullet.colliderect(tank_2):
                tank_2.pos=(-100,-100)
                tank_ally_alive-=1

            if tank_ally_alive==0:
                game_over=True

# Cài đặt chuột khi di chuyển vào sự kiện
def on_mouse_move(pos):
    if che_do_1.collidepoint(pos):
        che_do_1.image='one_player_2'
    else:
        che_do_1.image='one_player_1'

    if che_do_2.collidepoint(pos):
        che_do_2.image='multi_players_2'
    else:
        che_do_2.image='multi_players'

# Cài đặt chuột khi nhấp vào sự kiện
def on_mouse_down(pos):
    global number_tank_ally,start_game,tank_ally_alive,choose,check
    if che_do_1.collidepoint(pos):
        start_game=True
        number_tank_ally=1
        tank_ally_alive=1
        
    if che_do_2.collidepoint(pos):
        start_game=True
        number_tank_ally=2 
        tank_ally_alive=2       

# cài đặt các thay đổi khi tao tác
def update():
    global start_game,game_over,walls_2,walls,walls_3,river_full,river_full_2,river_full_3,bullets
    global stone_walls,stone_walls_2,stone_walls_3,cau,cau_2,cau_3,enemy_bullets
    global check_map_2,check_map_3,map,number_tank_ally,tank_ally_alive
    if start_game==True: # Khi bắt đầu game bắt đầu tạo thêm các tank và bot
        tank_set(tank)
        if number_tank_ally==2: # khi chọn chế độ 2 người các thao tác của tank 2 sẽ được thêm vào
            tank_set_2(tank_2)
            tank_2_bullets_set(tank_2)
        tank_bullets_set(tank)
        tank_bullet()
        enemy_set(enemies_1)
        enemy_set(enemies_2)
        enemy_set(enemies_3)
        enemy_bullets_set()
    if (keyboard.m or keyboard.p) and game_over==True: # khi thua nhấn m để trở lai màn hình chính và nhấn p để chơi lại
        if keyboard.m:
            start_game=False
        elif keyboard.p:
            start_game=True
        game_over=False
        tank.pos=(WIDTH/2+200,HEIGHT-25)
        tank.angle=90
        tank_2.pos=(WIDTH/2-200,HEIGHT-25)
        tank_2.angle=90
        tank_ally_alive=number_tank_ally
        walls.clear()
        walls_2.clear()
        walls_3.clear()
        river_full,river_full_2,river_full_3=[],[],[]
        bullets=[]
        stone_walls.clear()
        stone_walls_2.clear()
        stone_walls_3.clear()
        cau,cau_2,cau_3=[],[],[]
        enemy_bullets=[]  
        check_map_2=5
        check_map_3=5      
        map=1
        set_map_1()


# vẽ 
def draw():
    global map,bullet_holdoff_ally,check_map_2,check_map_3,start_game,game_over,speed_bullet
    if start_game==False : # vẽ màn hình bắt đầu game
        background_begin.draw()
        screen.draw.text('Game 1975',(9,10) ,color='white',fontsize=40)
        che_do_1.draw()
        che_do_2.draw()
    else:
        background.draw()
        tank.draw()
        if game_over: # nếu cái này đúng ta sẽ kết thúc game 
            enemies_1.clear()
            enemies_2.clear()
            enemies_3.clear()
            background_finish.draw()
            screen.fill((0,0,0))
            screen.draw.text('You lose',(300,100) ,color='white',fontsize=70)
            play_again.draw()
            main_menu.draw()
        elif len(enemies_1)==0: # nếu đúng chuyển sang map2
            if check_map_2==0:           
                if check_map_3==0 and game_win: # nếu thắng 
                    background_finish.draw() # in ra màn hình thắng
                    sounds.tuyenngondoclap1.play() # phát nhạc nền chiến thắng
                    #screen.draw.text('WINER',(260,250) ,color=(255,255,255),fontsize=150)      
                    
                else:
                    if map==2:
                        set_map_3()
                        speed_bullet=15
                        enemy_bullets_set()
                        walls_2.clear()
                        if tank.pos!=(-100,-100):
                            tank.pos=(WIDTH/2+200,HEIGHT-25)
                            tank.angle=90
                        if number_tank_ally==2:
                            if tank_2.pos!=(-100,-100):
                                tank_2.pos=(WIDTH/2-200,HEIGHT-25)
                                tank_2.angle=90
                        map=3
                    # vẽ map 3
                    background.draw()
                    home.draw()
                    cong_dinh.draw()
                    for stone_wall in stone_walls_3:
                        stone_wall.draw()                
                    for wall in walls_3:
                        wall.draw()
                    for bullet in bullets:
                        bullet.draw() 
                    for enemy in enemies_3:
                        enemy.draw()
                    for bullet in enemy_bullets:
                        bullet.draw()
                    tank.draw()  
                    if number_tank_ally==2:
                        tank_2.draw()
                    check_map_3=len(enemies_3)               
            else: # vẽ map 2 
                if map==1:
                    set_map_2()
                    speed_bullet=10
                    enemy_bullets_set()
                    if tank.pos!=(-100,-100):
                        tank.pos=(WIDTH/2+200,HEIGHT-25)
                        tank.angle=90
                    if number_tank_ally==2:
                        if tank_2.pos!=(-100,-100):
                            tank_2.pos=(WIDTH/2-200,HEIGHT-25)
                            tank_2.angle=90
                    map=2
                    walls.clear()
                    stone_walls.clear()
                    river_full.clear()
                    cau.clear()
                background.draw()
                home.draw()
                for wall in walls_2:
                    wall.draw()
                for bullet in bullets:
                    bullet.draw() 
                for enemy in enemies_2:
                    enemy.draw()
                for bullet in enemy_bullets:
                    bullet.draw()
                tank.draw() 
                if number_tank_ally==2:
                    tank_2.draw() 
                check_map_2=len(enemies_2)   
        else:# vẽ map 1   
            background.draw()
            home.draw()
            
            for wall in walls:
                wall.draw()
            for stone_wall in stone_walls:
                stone_wall.draw()
            for part_river in river_full:
                part_river.draw()
            for cau1phann in cau:
                cau1phann.draw()
            for bullet in bullets:
                bullet.draw() 
            for enemy in enemies_1:
                enemy.draw()
            for bullet in enemy_bullets:
                bullet.draw()  
            tank.draw()
            if number_tank_ally==2:
                tank_2.draw()




pgzrun.go()
