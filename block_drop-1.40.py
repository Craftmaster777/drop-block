import pygameimport sysimport randomimport timefrom pygame.locals import *pygame.init()gray = (150,150,150)blue = (0,0,255)green = (0,225,0)red = (255,0,0)back_color = (75,75,75)game = (550, 550)count = 0player_y = 300player_x = 250player_size = 25enemy_size = 30boss_size = (60, 30)boss_size2 = (75, 30)enemy_x1 = 250enemy_x2 = 150enemy_x3 = 350enemy_x4 = 450enemy_x5 = 500enemy_x6 = 100enemy_x7 = 400enemy_x8 = 450enemy_x9 = 400enemy_x10 = 400enemy_x11 = 400enemy_x12 = 400enemy_x13 = 400enemy_y = 0pps = 1block_sp = 0.001screen = pygame.display.set_mode((game[0],game[1]))def text(t,x,y,s): pygame.display.set_caption('Show Text') font = pygame.font.Font('freesansbold.ttf', s) text = font.render(t, True, gray) textRect = text.get_rect() textRect.center = (x, y) screen.blit(text, textRect)def rect(x,y,h,w,c): pygame.draw.rect(screen, c, (x,y,h,w))def player(): rect(player_x,player_y,player_size,player_size,green)def enemy1(x): rect(x,enemy_y,enemy_size,enemy_size,red) time.sleep(block_sp)def boss1(): rect(enemy_x10,enemy_y,boss_size[0],boss_size[1],red) time.sleep(block_sp)def boss2(): rect(enemy_x11,enemy_y,boss_size[0],boss_size[1],red) time.sleep(block_sp)def boss3(): rect(enemy_x12,enemy_y,boss_size[0],boss_size[1],red) time.sleep(block_sp)def boss4(): rect(enemy_x13,enemy_y,boss_size2[0],boss_size2[1],blue) time.sleep(block_sp)def mouse1(x,y,h,w): if event.type == pygame.MOUSEBUTTONDOWN:  mouse_pos = pygame.mouse.get_pos()  rect_pos = pygame.Rect(x,y,h,w)  if rect_pos.collidepoint(mouse_pos):   sys.exit()def detect(a): p_x = player_x p_y = player_y e_y = enemy_y if (a >= p_x and a < (p_x + player_size)) or (p_x >= a and p_x < (a+enemy_size)):  if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):   end()def end(): lvl = (count * 2 // 3) print(lvl, 'points') sys.exit()def enemy_all(): enemy1(enemy_x1) if count >= 1:  enemy1(enemy_x2)  enemy1(enemy_x3) if count >= 2:  enemy1(enemy_x4)  enemy1(enemy_x5) if count > 10:  enemy1(enemy_x6) if count > 15:  enemy1(enemy_x7)  enemy1(enemy_x8) if count > 20:  enemy1(enemy_x9)  boss1() if count > 22:  boss2() if count > 24:  boss3() if count > 25:  boss4()def walls(): rect(0,0,20,550,blue) rect(530,0,20,550,blue)while True: for event in pygame.event.get():  if event.type == pygame.QUIT:   end()  elif event.type == KEYDOWN and event.key == K_RIGHT:   player_x = player_x + 10   if count > 15:    player_x = player_x + 10   if count > 30:    player_x = player_x - 10  elif event.type == KEYDOWN and event.key == K_LEFT:   player_x = player_x - 10   if count > 15:    player_x = player_x - 10   if count > 30:    player_x = player_x + 10  elif event.type == KEYDOWN and event.key == K_d:   player_x = player_x + 10   if count > 15:    player_x = player_x + 10   if count > 30:    player_x = player_x - 10  elif event.type == KEYDOWN and event.key == K_a:   player_x = player_x - 10   if count > 15:    player_x = player_x - 10   if count > 30:    player_x = player_x + 10  elif event.type == KEYDOWN and event.key == K_SPACE:   time.sleep(1)  if player_x <= 20:   player_x = 20  if player_x >= 505:   player_x = 505  if count > 5:   if count > 10:    block_sp = 0.0005   if count > 20:    blobk_sp = 0.0001 screen.fill((60,60,60)) enemy_y = enemy_y + pps if count > 10:  if pps < 2:   pps = pps + 0.5  if count > 15:   if pps < 3:    pps = pps + 0.5  if count > 20:   if pps < 4:    pps = pps + 0.5 if enemy_y > 500:  enemy_y = 0  if count < 25:   enemy_x1 = random.randint(19, game[0] - 40)   enemy_x2 = random.randint(19, game[0] - 40)   enemy_x3 = random.randint(19, game[0] - 40)   enemy_x4 = random.randint(19, game[0] - 40)   enemy_x5 = random.randint(19, game[0] - 40)   enemy_x6 = random.randint(19, game[0] - 40)   enemy_x7 = random.randint(19, game[0] - 40)   enemy_x8 = random.randint(19, game[0] - 40)   enemy_x9 = random.randint(19, game[0] - 40)   enemy_x10 = random.randint(19, game[0] - 40)   enemy_x11 = random.randint(19, game[0] - 40)   enemy_x12 = random.randint(19, game[0] - 40)  count = count + 1  if count > 25:   enemy_x1 = random.randint(20, game[0] - 30)   enemy_x2 = random.randint(20, game[0] - 30)   enemy_x3 = random.randint(20, game[0] - 30)   enemy_x4 = random.randint(20, game[0] - 30)   enemy_x5 = random.randint(20, game[0] - 30)   enemy_x6 = random.randint(20, game[0] - 30)   enemy_x7 = random.randint(20, game[0] - 30)   enemy_x8 = random.randint(20, game[0] - 30)   enemy_x9 = random.randint(20, game[0] - 30)   enemy_x10 = random.randint(20, game[0] - 30)   enemy_x11 = random.randint(20, game[0] - 30)   enemy_x12 = random.randint(20, game[0] - 30)   enemy_x13 = player_x player() enemy_all() detect(enemy_x1) if count >= 1:  detect(enemy_x2)  detect(enemy_x3) if count >= 2:  detect(enemy_x4)  detect(enemy_x5) if count > 10:  detect(enemy_x6) if count > 15:  detect(enemy_x7)  detect(enemy_x8) if count > 20:  detect(enemy_x9)  detect(enemy_x10) if count > 22:  detect(enemy_x11) if count > 24:  detect(enemy_x12) if count > 25:  detect(enemy_x13) walls() if count < 5:  rect(40,475,115,50,red)  text('drop block',100,500,20) pygame.display.update()