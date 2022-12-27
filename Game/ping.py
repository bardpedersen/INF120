#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 23:02:32 2021

@author: Bard
"""
import pygame
pygame.init()
screen_lengde= 1000
screen_høyde = 800
tile_size = 50
win = pygame.display.set_mode((screen_lengde,screen_høyde))
pygame.display.set_caption("Spill")
clock = pygame.time.Clock()

while True:
    boks1 = (screen_lengde/2-40,200)
    boks2 = (screen_lengde/2-40,400)
    end_it = False
    while (end_it==False):
        win.fill((0,0,0))
        smallfont = pygame.font.SysFont('Britannic Bold',40) 
        text = smallfont.render('PingPong' , True , (255,255,255)) 
        text1 = smallfont.render('Start' , True , (255,255,255)) 
        text2 = smallfont.render('Avslutt' , True , (255,255,255)) 
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos() 
                if boks1[0] <= mouse[0] <= (boks1[0]+50) and boks1[1] <= mouse[1] <= (boks1[1]+40): 
                    end_it = True
                if boks2[0] <= mouse[0] <= (boks2[0]+50) and boks2[1] <= mouse[1] <= (boks2[1]+40): 
                    pygame.quit()
                
        win.blit(text,(150,100))
        win.blit(text1,boks1) 
        win.blit(text2,boks2)
        pygame.display.update()
    
    class player1(object):
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.down = False
            self.up = False
            self.hitbox = (self.x, self.y, self.width, self.height)
    
        def update(self):
            dy = 0
            key = pygame.key.get_pressed()
            if key[pygame.K_UP]:
                dy = -10
            if key[pygame.K_DOWN]:
                dy = 10
    
            if self.y + self.height +dy > 0 and self.y + dy < screen_høyde:
                self.y += dy
            self.hitbox = (self.x, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 255, 255), (self.hitbox))
        
    class player2(object):
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.down = False
            self.up = False
            self.hitbox = (self.x, self.y, self.width, self.height)
    
        def update(self):
            dy = 0
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                dy = -10
            if key[pygame.K_s]:
                dy = 10
            if self.y + self.height +dy > 0 and self.y + dy < screen_høyde:
                self.y += dy
            self.hitbox = (self.x, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 255, 255), (self.hitbox))
            
    class kule(object):
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.down = False
            self.up = False
            self.velx=5
            self.vely=5
            self.hitbox = (self.x, self.y, self.width, self.height)
    
        def update(self):
            if self.vely > 0:
                if self.y + self.vely < screen_høyde:
                    self.y += self.vely
                else:
                    self.vely = self.vely * -1
            else:
                if self.y - self.vely > 0:
                    self.y += self.vely
                else:
                    self.vely = self.vely * -1

            if self.velx > 0:
                if self.x + self.velx < screen_lengde:
                    self.x += self.velx
                else:
                    self.velx= self.velx * -1
            else:
                if self.x - self.velx > 0:
                    self.x += self.velx
                else:
                    self.velx = self.velx * -1
            self.hitbox =(self.x, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 255, 255), (self.hitbox)) 
                
        def hit1(self):
            self.velx = self.velx * -1
            self.hitbox =(self.x, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 255, 255), (self.hitbox)) 
            print('hit1')
            
        def hit2(self):
            self.velx = self.velx * -1
            self.hitbox =(self.x, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 255, 255), (self.hitbox))
            print('hit2')
    
    man1 = player1(970, 200, 10,60)
    man2 = player2(30, 200, 10,60)
    kule = kule(100,100,10,10)
    run = True
    s1=0
    s2=0
    while run:
        clock.tick(100)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        if kule.hitbox[0] >= man1.hitbox[0] and kule.hitbox[0] < man1.hitbox[0] + man1.hitbox[2] or man1.hitbox[0] >= kule.hitbox[0] and man1.hitbox[0] < kule.hitbox[0]+kule.hitbox[2]:
            if kule.hitbox[1] >= man1.hitbox[1] and kule.hitbox[1] < man1.hitbox[1] + man1.hitbox[3] or man1.hitbox[1] >= kule.hitbox[1] and man1.hitbox[1] < kule.hitbox[1]+kule.hitbox[3]:
                kule.hit1()
        if kule.hitbox[0] >= man2.hitbox[0] and kule.hitbox[0] < man2.hitbox[0] + man2.hitbox[2] or man2.hitbox[0] >= kule.hitbox[0] and man2.hitbox[0] < kule.hitbox[0]+kule.hitbox[2]:
            if kule.hitbox[1] >= man2.hitbox[1] and kule.hitbox[1] < man2.hitbox[1] + man2.hitbox[3] or man2.hitbox[1] >= kule.hitbox[1] and man2.hitbox[1] < kule.hitbox[1]+kule.hitbox[3]:
                kule.hit2()
                
        if kule.hitbox[0] >= screen_lengde - kule.hitbox[2]:
            s1 += 1 
            kule.x = 50
            kule.y = 50
        if kule.hitbox[0] <= 0 :
            s2 += 1
            kule.x = 950
            kule.y = 50
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False

        win.fill((0,0,0))
        boks1 = (100,70)
        boks2 = (900,70)
        ss1='{}'.format(int(s1))
        ss2='{}'.format(int(s2))
        smallfont = pygame.font.SysFont('Britannic Bold',50)
        text = smallfont.render(ss1, True , (255,255,255)) 
        text1 = smallfont.render(ss2 , True , (255,255,255))
        win.blit(text,boks1) 
        win.blit(text1,boks2)
        man1.update()
        man2.update()
        kule.update()
        pygame.display.update() 
        
        if s1 >= 10:
            text = smallfont.render('Spiller 2 vant', True , (255,255,255)) 
            win.blit(text,(500,400)) 
            pygame.display.update()
            pygame.time.wait(5000)  
            run = False
        if s2 >= 10:
            text = smallfont.render('Spiller 1 vant', True , (255,255,255)) 
            win.blit(text,(400,400)) 
            pygame.display.update()
            pygame.time.wait(5000)  
            run = False
    end_it = False
pygame.quit()


