#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 23:02:32 2021

@author: Bard
"""
import pygame
pygame.init()
screen_lengde= 1300
screen_høyde = 700
tile_size = 50
win = pygame.display.set_mode((screen_lengde,screen_høyde))
pygame.display.set_caption("Spill")
bg = pygame.image.load('bg.png')
clock = pygame.time.Clock()
while True:
    #start skjerm 
    christine = False
    andre = False
    åsmund = False
    endre = False
    karakter_valg=True
    boks1 = (screen_lengde/2-40,200)
    boks2 = (screen_lengde/2-40,300)
    boks3 = (screen_lengde/2-40,400)
    end_it = False
    while (end_it==False):
        win.fill((102,204,255))
        smallfont = pygame.font.SysFont('Britannic Bold',40) 
        text = smallfont.render('Velkommen til Bårds hjemme mekka spill' , True , (255,255,255)) 
        text1 = smallfont.render('Start' , True , (255,255,255)) 
        text2 = smallfont.render('Karakter' , True , (255,255,255)) 
        text3 = smallfont.render('Avslutt' , True , (255,255,255))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos() 
                if boks1[0] <= mouse[0] <= (boks1[0]+50) and boks1[1] <= mouse[1] <= (boks1[1]+40): 
    
                    end_it = True
                if boks2[0] <= mouse[0] <= (boks2[0]+50) and boks2[1] <= mouse[1] <= (boks2[1]+40): 
                    karkater_boks1 = (200-20,150, 40,74)
                    karkater_boks2 = (400-20,150, 45, 73)
                    karkater_boks3 = (600-20,150, 40, 74)
                    karkater_boks4 = (200-20,300, 40 ,74)
                    karkater_boks5 = (400-20,300, 40, 74)
                    karakter_valg=False
                    while (karakter_valg==False):
                        win.fill((102,204,255))
                        smallfont = pygame.font.SysFont('Britannic Bold',40) 
                        text = smallfont.render('Velgkarakter' , True , (255,255,255)) 
                        karakter1 = pygame.image.load('sprite_00.png') 
                        karakter2 = pygame.image.load('sprite_06.png')
                        karakter3 = pygame.image.load('sprite_12.png')
                        karakter4 = pygame.image.load('sprite_18.png')
                        karakter5 = pygame.image.load('sprite_24.png')
                        for event in pygame.event.get():
                            if event.type==pygame.MOUSEBUTTONDOWN:
                                mouse = pygame.mouse.get_pos()
                                if karkater_boks1[0] <= mouse[0] <= karkater_boks1[0]+karkater_boks1[2] and karkater_boks1[1] <= mouse[1] <= karkater_boks1[1]+karkater_boks1[3]: 
                                    print('Bård')
                                    christine = False
                                    andre = False
                                    åsmund = False
                                    endre = False
                                    karakter_valg=True
                                    end_it = True
                                if karkater_boks2[0] <= mouse[0] <= karkater_boks2[0]+karkater_boks2[2] and karkater_boks2[1] <= mouse[1] <= karkater_boks2[1]+karkater_boks2[3]: 
                                    print('Christine')
                                    christine = True
                                    andre = False
                                    åsmund = False
                                    endre = False
                                    karakter_valg=True
                                    end_it = True
                                if karkater_boks3[0] <= mouse[0] <= karkater_boks3[0]+karkater_boks3[2] and karkater_boks3[1] <= mouse[1] <= karkater_boks3[1]+karkater_boks3[3]: 
                                    print('André')
                                    christine = False
                                    andre = True
                                    åsmund = False
                                    endre = False
                                    karakter_valg=True
                                    end_it = True
                                if karkater_boks4[0] <= mouse[0] <= karkater_boks4[0]+karkater_boks4[2] and karkater_boks4[1] <= mouse[1] <= karkater_boks4[1]+karkater_boks4[3]: 
                                    print('Åsmund')
                                    christine = False
                                    andre = False
                                    åsmund = True
                                    endre = False
                                    karakter_valg=True
                                    end_it = True
                                if karkater_boks5[0] <= mouse[0] <= karkater_boks5[0]+karkater_boks5[2] and karkater_boks5[1] <= mouse[1] <= karkater_boks5[1]+karkater_boks5[3]: 
                                    print('Endre')
                                    christine = False
                                    andre = False
                                    åsmund = False
                                    endre = True
                                    karakter_valg=True
                                    end_it = True
                            win.blit(text,(screen_lengde/2-75,50))
                            win.blit(karakter1,karkater_boks1) 
                            win.blit(karakter2,karkater_boks2)
                            win.blit(karakter3,karkater_boks3) 
                            win.blit(karakter4,karkater_boks4)
                            win.blit(karakter5,karkater_boks5)
                            pygame.display.update()
                                         
                if boks3[0] <= mouse[0] <= (boks3[0]+50) and boks3[1] <= mouse[1] <= (boks3[1]+40): 
                    pygame.quit()
                
        win.blit(text,(150,100))
        win.blit(text1,boks1) 
        win.blit(text2,boks2)
        win.blit(text3,boks3)
        pygame.display.update()
        
    if christine == True:
        walkRight = [pygame.image.load('sprite_06.png'), pygame.image.load('sprite_07.png'), pygame.image.load('sprite_08.png')]
        walkLeft = [pygame.image.load('sprite_09.png'), pygame.image.load('sprite_10.png'), pygame.image.load('sprite_11.png')]
    elif andre == True:
        walkRight = [pygame.image.load('sprite_12.png'), pygame.image.load('sprite_13.png'), pygame.image.load('sprite_14.png')]
        walkLeft = [pygame.image.load('sprite_15.png'), pygame.image.load('sprite_16.png'), pygame.image.load('sprite_17.png')]
    elif åsmund == True:
        walkRight = [pygame.image.load('sprite_18.png'), pygame.image.load('sprite_19.png'), pygame.image.load('sprite_20.png')]
        walkLeft = [pygame.image.load('sprite_21.png'), pygame.image.load('sprite_22.png'), pygame.image.load('sprite_23.png')]
    elif endre == True:
        walkRight = [pygame.image.load('sprite_24.png'), pygame.image.load('sprite_25.png'), pygame.image.load('sprite_26.png')]
        walkLeft = [pygame.image.load('sprite_27.png'), pygame.image.load('sprite_28.png'), pygame.image.load('sprite_29.png')]
    else:
        walkRight = [pygame.image.load('sprite_00.png'), pygame.image.load('sprite_01.png'), pygame.image.load('sprite_02.png')]
        walkLeft = [pygame.image.load('sprite_03.png'), pygame.image.load('sprite_04.png'), pygame.image.load('sprite_05.png')]
        
    class World():
    	def __init__(self, data):
    		self.tile_list = []
    
    		#load images
    		dirt_img = pygame.image.load('murstein.png')
    		grass_img = pygame.image.load('murstein.png')
    
    		row_count = 0
    		for row in data:
    			col_count = 0
    			for tile in row:
    				if tile == 1:
    					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
    					img_rect = img.get_rect()
    					img_rect.x = col_count * tile_size
    					img_rect.y = row_count * tile_size
    					tile = (img, img_rect)
    					self.tile_list.append(tile)
    				if tile == 2:
    					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
    					img_rect = img.get_rect()
    					img_rect.x = col_count * tile_size
    					img_rect.y = row_count * tile_size
    					tile = (img, img_rect)
    					self.tile_list.append(tile)
    				col_count += 1
    			row_count += 1
    
    	def draw(self):
    		for tile in self.tile_list:
    			win.blit(tile[0], tile[1])
          
    world_data = [ 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    ]
    
    world = World(world_data)
    
    #player 1
    class player(object):
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 10
            self.isJump = False
            self.left = False
            self.right = False
            self.walkCount = 0
            self.jumpCount = 10
            self.standing = True
            self.hitbox = (self.x, self.y, 40, 74)
            self.vel_y = 0
    
        def draw(self, win):
            if self.walkCount + 1 >= 12:
                self.walkCount = 0
            if not(self.standing):
                if self.left:
                    win.blit(walkLeft[self.walkCount//4], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount//4], (self.x,self.y))
                    self.walkCount +=1
            else:
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkLeft[0], (self.x, self.y))
            self.hitbox = (self.x, self.y, 40, 74)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                 
        def hit(self):
            print('tapte')
            
        def blokker(self):
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            self.y += self.vel_y    
            
            for tile in world.tile_list:
                if tile[1].colliderect(self.x+self.vel,self.y,self.width,self.height):
                    self.right = False
                if tile[1].colliderect(self.x,self.y+self.vel_y,self.width,self.height):
                    if self.vel_y < 0:
                        self.y=tile[1].bottom-self.hitbox[1]
                        self.vel_y=0
                    elif self.vel_y >= 0:
                        self.y =tile[1].top-self.hitbox[3]
                        self.vel_y=0
    
    #Skudd
    class projectile(object):
        def __init__(self,x,y,radius,color,facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 8 * facing
    
        def draw(self,win):
            pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
    
    #fiende
    class enemy(object):
        walkRight = [pygame.image.load('sprite_30.png')]
        walkLeft = [pygame.image.load('sprite_30.png')]
    
        def __init__(self, x, y, width, height, end):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.path = [self.x, self.end]
            self.walkCount = 0
            self.vel = 5
            self.hitbox = (self.x, self.y, 40, 64)
            self.visible = True
            self.vel_y = 0
    
        def draw(self,win):
            self.move()
            if self.visible:
                if self.walkCount + 1 >= 32:
                    self.walkCount = 0
                if self.vel > 0:
                    win.blit(self.walkRight[self.walkCount //32], (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkLeft[self.walkCount //32], (self.x, self.y))
                    self.walkCount += 1
                    
                self.hitbox = (self.x, self.y, 40, 64)
            else:
                self.hitbox = (0,0,0,0)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    
        def move(self):
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
                    
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            self.y += self.vel_y   
            
            for tile in world.tile_list:
                if tile[1].colliderect(self.x,self.y+self.vel_y,self.width,self.height):
                    if self.vel_y < 0:
                        self.y=tile[1].bottom-self.hitbox[1]
                    if self.vel_y >= 0:
                        self.y =tile[1].top-self.hitbox[3]
    
        def hit(self):
            self.visible = False
            print('hit')
    
    #tegner
    def redrawGameWindow():
        win.blit(bg, (0 ,0))
        world.draw()
        man.draw(win)
        cactus.draw(win)
        for bullet in bullets:
            bullet.draw(win)
        pygame.display.update()
        
    #mainloop
    man = player(10, (screen_høyde-tile_size-75), 40,74)
    cactus = enemy(200,(screen_høyde-tile_size-75), 40, 64, 450)
    shootLoop = 0
    bullets = []
    run = True
    while run==True:
        clock.tick(100)
        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        #fiende drept av kuler
        for bullet in bullets:
            if bullet.y - bullet.radius < cactus.hitbox[1] + cactus.hitbox[3] and bullet.y + bullet.radius > cactus.hitbox[1]:
                if bullet.x + bullet.radius > cactus.hitbox[0] and bullet.x - bullet.radius < cactus.hitbox[0] + cactus.hitbox[2]:
                    cactus.hit()
                    bullets.pop(bullets.index(bullet))
            if bullet.x < screen_lengde and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
                
        #menneske drept av fiende
        if cactus.hitbox[0] >= man.hitbox[0] and cactus.hitbox[0] < man.hitbox[0] + man.hitbox[2] or man.hitbox[0] >= cactus.hitbox[0] and man.hitbox[0] < cactus.hitbox[0]+cactus.hitbox[2]:
            if cactus.hitbox[1] >= man.hitbox[1 ] and cactus.hitbox[1] < man.hitbox[1] + man.hitbox[3] or man.hitbox[1] >= cactus.hitbox[1] and man.hitbox[1] < cactus.hitbox[1]+cactus.hitbox[3]:
                man.hit()
                run = False
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 5:
                bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
            shootLoop = 1
            
        if keys[pygame.K_ESCAPE]:
            run=False
    
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x < screen_lengde - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.walkCount = 0
            
        if not(man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10
                
            
        man.blokker()
        redrawGameWindow()
pygame.quit()