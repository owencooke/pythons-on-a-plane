# FIXME: Fancy Header Here Later

import pygame
from pygame.locals import *
from random import randint

def game():
    # Initialize main menu appearance
    #background = pygame.image.load("graphics/backgrounds/colored_talltrees.png")
    background = pygame.image.load("graphics/BG.png")
    background = pygame.transform.scale(background, (1280, 1280)) # 1280, 1280
    plane_fly1, plane_fly2 = plane_menu_images()
    plane_rect = plane_fly1.get_rect(topright=(1500, 100)) # 1500, 100 start for moving
    screen.blit(background, (0, 0))
    #cloud1, cloud2, cloud3, cloud4, cloud5, cloud6 = cloud_images()
    play_img, how_img, lboard_img = button_images()
    # Main Menu loop
    running = True
    frame_flag = True
    opacity = 0
    gamestate = 0
    enemyStopwatch = 0
    while running:
        if gamestate == 0:
            for event in pygame.event.get():
            # If user hits the x button on pygame window
                if event.type == QUIT:
                    running = False
                # If any of the buttons are clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if play_rect.collidepoint(pos):
                        gamestate = 1 # <-------- PUT GAMEPLAY FUNCTION HERE
                    if how_rect.collidepoint(pos):
                        pass # <------ PUT HOW TO PLAY MENU HERE
                    if lboard_rect.collidepoint(pos):
                        pass # <----- PUT LEADERBOARD MENU HERE
                    if credits_rect.collidepoint(pos):
                        print('credits') # <----- PUT CREDIT MENU HERE
            # Plane animation
            screen.blit(background, (0, 0))
            plane_rect, frame_flag = plane_animation(plane_rect, plane_fly1, plane_fly2, frame_flag)

            # Buttons / GUI Functionality
            play_rect = buttons(play_img, opacity, (width/2, height/2))
            how_rect = buttons(how_img, opacity, (320, 550))
            lboard_rect = buttons(lboard_img, opacity, (920, 550))
            font = pygame.font.SysFont(None, 36)
            credits = font.render("CREDITS", True, (255, 255, 255))
            credits_rect = credits.get_rect(center=(width/2, 650))
            screen.blit(credits, credits_rect)
            pygame.display.update()
            opacity += 3
        elif gamestate == 1:
            time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (time - player.stopwatch) > 480:
                            rocket_group.add(player.create_rocket())
                            player.stopwatch = pygame.time.get_ticks()
                            player.animationState = 2
                            shoot.play()
                            shoot.set_volume(0.2)
            if (time - enemyStopwatch) > 2000:
                enemies.add(Enemy(1400,randint(100,620)))
                enemyStopwatch = pygame.time.get_ticks()
            screen.blit(background,(0,0))
            
            pygame.sprite.groupcollide(rocket_group,enemies,False,False)
            player_group.draw(screen)
            player_group.update()
            enemies.draw(screen)
            enemies.update()
            rocket_group.draw(screen)
            rocket_group.update()
            for enemy in enemies:
                if pygame.sprite.spritecollideany(enemy,rocket_group):
                    enemy.getHit = True
            for rocket in rocket_group:
                if pygame.sprite.spritecollideany(rocket,enemies):
                    rocket.getHit = True
            pygame.display.update()
            clock.tick(60)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original1 = pygame.image.load('graphics/plane/Fly (1).png').convert_alpha()
        self.original2 = pygame.image.load('graphics/plane/Fly (2).png').convert_alpha()
        self.shoot1 = pygame.image.load('graphics/plane/Shoot (1).png').convert_alpha()
        self.shoot2 = pygame.image.load('graphics/plane/Shoot (2).png').convert_alpha()
        self.shoot3 = pygame.image.load('graphics/plane/Shoot (3).png').convert_alpha()
        self.shoot4 = pygame.image.load('graphics/plane/Shoot (4).png').convert_alpha()
        self.shoot5 = pygame.image.load('graphics/plane/Shoot (5).png').convert_alpha()
        self.animationState = 0
        self.image = pygame.transform.scale(self.original1, (232,159))
        self.rect = self.image.get_rect()
        self.stopwatch = 0
    def create_rocket(self):
        return Rocket(self.rect.x,self.rect.y)
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x += -10
        if keys[pygame.K_w]:
            self.rect.y += -10
        if keys[pygame.K_s]:
            self.rect.y += 10
        if keys[pygame.K_d]:
            self.rect.x += 10
    def player_animation(self):
        if self.animationState == 0:
            self.image = pygame.transform.scale(self.original2, (232,159))
            self.animationState = 1
        elif self.animationState == 1:
            self.image = pygame.transform.scale(self.original1, (232,159))
            self.animationState = 0
        elif self.animationState == 2:
            self.image = pygame.transform.scale(self.shoot1, (232,159))
            self.animationState = 3
        elif self.animationState == 3:
            self.image = pygame.transform.scale(self.shoot2, (232,159))
            self.animationState = 4
        elif self.animationState == 4:
            self.image = pygame.transform.scale(self.shoot3, (232,159))
            self.animationState = 5
        elif self.animationState == 5:
            self.image = pygame.transform.scale(self.shoot4, (232,159))
            self.animationState = 6
        elif self.animationState == 6:
            self.image = pygame.transform.scale(self.shoot5, (232,159))
            self.animationState = 0
    def update(self):
        self.player_input()
        self.player_animation()
class Rocket(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load('graphics/bullet/shell.gif').convert_alpha()
        self.one = pygame.image.load('graphics/explosion/1.png').convert_alpha()
        self.two = pygame.image.load('graphics/explosion/2.gif').convert_alpha()
        self.three = pygame.image.load('graphics/explosion/3.gif').convert_alpha()
        self.four = pygame.image.load('graphics/explosion/4.gif').convert_alpha()
        self.five = pygame.image.load('graphics/explosion/5.gif').convert_alpha()
        self.six = pygame.image.load('graphics/explosion/6.gif').convert_alpha()
        self.seven = pygame.image.load('graphics/explosion/7.gif').convert_alpha()
        self.eight = pygame.image.load('graphics/explosion/8.gif').convert_alpha()
        self.nine = pygame.image.load('graphics/explosion/9.gif').convert_alpha()
        self.ten = pygame.image.load('graphics/explosion/10.gif').convert_alpha()
        self.eleven = pygame.image.load('graphics/explosion/11.gif').convert_alpha()
        self.twelve = pygame.image.load('graphics/explosion/12.gif').convert_alpha()
        self.thirteen = pygame.image.load('graphics/explosion/13.gif').convert_alpha()
        self.fourteen = pygame.image.load('graphics/explosion/14.gif').convert_alpha()
        self.fifteen = pygame.image.load('graphics/explosion/15.gif').convert_alpha()
        self.rect = self.image.get_rect(center = (pos_x+180,pos_y+118))
        self.speed = 0
        self.getHit = False
        self.animationState = -1
    def explosion(self):
        if self.animationState == -1:
            self.animationState = 0
            enemyDie.play()
            enemyDie.set_volume(0.2)
        elif self.animationState == 0:
            self.rect.x -= 50
            self.rect.y -= 50
            self.image = self.one
            self.animationState = 1
        elif self.animationState == 1:
            self.image = self.two
            self.animationState = 2
        elif self.animationState == 2:
            self.image = self.three
            self.animationState = 3
        elif self.animationState == 3:
            self.image = self.four
            self.animationState = 4
        elif self.animationState == 4:
            self.image = self.five
            self.animationState = 5
        elif self.animationState == 5:
            self.image = self.six
            self.animationState = 6
        elif self.animationState == 6:
            self.image = self.seven
            self.animationState = 7
        elif self.animationState == 7:
            self.image = self.eight
            self.animationState = 8
        elif self.animationState == 8:
            self.image = self.nine
            self.animationState = 9
        elif self.animationState == 9:
            self.image = self.ten
            self.animationState = 10
        elif self.animationState == 10:
            self.image = self.eleven
            self.animationState = 11
        elif self.animationState == 11:
            self.image = self.twelve
            self.animationState = 12
        elif self.animationState == 12:
            self.image = self.thirteen
            self.animationState = 13
        elif self.animationState == 13:
            self.image = self.fourteen
            self.animationState = 14
        elif self.animationState == 14:
            self.image = self.fifteen
            self.kill()
    def update(self):
        if self.getHit:
            self.explosion()
        else:
            self.speed += 0.4
            self.rect.x += self.speed
            if self.rect.x >= 1400:
                self.kill()
class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.original1 = pygame.image.load('graphics/enemy/enemy1.png')
        self.original2 = pygame.image.load('graphics/enemy/enemy2.png')
        self.dead = pygame.image.load('graphics/enemy/enemy_dead.png')
        self.image = pygame.transform.flip(pygame.transform.scale(self.original1, (232,159)),True,False)
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.animationState = 0
        self.stopwatch = 0
        self.falling = 0
        self.getHit = False
    def enemy_animation(self):
        if self.animationState == 0:
            self.image = pygame.transform.flip(pygame.transform.scale(self.original2, (232,159)),True,False)
            self.animationState = 1
        elif self.animationState == 1:
            self.image = pygame.transform.flip(pygame.transform.scale(self.original1, (232,159)),True,False)
            self.animationState = 0
        elif self.animationState == 2:
            self.image = pygame.transform.flip(pygame.transform.scale(self.dead, (232,159)),True,False)
    def update(self):
        self.enemy_animation()
        self.rect.x -= 10
        if self.getHit:
            self.animationState = 2
            self.rect.y += self.falling
            self.falling += 0.5
        else:
            if self.rect.y < player.rect.y:
                self.rect.y += 2
            if self.rect.y > player.rect.y:
                self.rect.y -= 2
def plane_menu_images():
    ''' Loads plane images and returns them after manipulation '''

    # Loading, scaling and flipping first plane image
    plane_fly1 = pygame.image.load("graphics/plane/Fly (1).png")
    plane_fly1 = pygame.transform.scale(plane_fly1, (222, 151))
    plane_fly1 = pygame.transform.flip(plane_fly1, True, False)
    # Loading, scaling and flipping second plane image
    plane_fly2 = pygame.image.load("graphics/plane/Fly (2).png")
    plane_fly2 = pygame.transform.scale(plane_fly2, (222, 151))
    plane_fly2 = pygame.transform.flip(plane_fly2, True, False)
    # Returns two pygame images
    return plane_fly1, plane_fly2


def plane_animation(plane_rect, plane_fly1, plane_fly2, frame_flag):
    ''' Creates animation for plane's propellor.
    Also some functionality for menu movement.
    NOTE: be sure to call screen.blit(background, (0, 0)) before this function '''

    # Get center position from the previous frame's rectangle
    current_center = plane_rect.center
    # Speed is only necessary for flying plane image across screen, not animation
    speed = [-5,0]	# <--- not needed for propellor animation
    # Alternate images every frame
    if frame_flag:
        # Create a new rect with alternate plane image
        # *** At same location as previous frame using "center ="
        plane_rect = plane_fly2.get_rect(center = current_center)
        plane_rect = plane_rect.move(speed) # <--- not needed for propellor animation
        screen.blit(plane_fly2, plane_rect)
    else:
        plane_rect = plane_fly1.get_rect(center = current_center)
        plane_rect = plane_rect.move(speed) # <--- not needed for propellor animation
        screen.blit(plane_fly1, plane_rect)
    frame_flag = not frame_flag
    return plane_rect, frame_flag


def button_images():
    ''' Loads cloud images w/ certain transparency
    cloud1 = pygame.image.load("graphics/PNG/cloud1.png")
    cloud1 = pygame.transform.scale(cloud1, (322, 151))
    cloud2 = pygame.image.load("graphics/PNG/cloud2.png")
    cloud2 = pygame.transform.scale(cloud2, (322, 151))
    cloud3 = pygame.image.load("graphics/PNG/cloud3.png")
    cloud3 = pygame.transform.scale(cloud3, (322, 151))
    cloud4 = pygame.image.load("graphics/PNG/cloud4.png")
    cloud4 = pygame.transform.scale(cloud4, (322, 151))
    cloud5 = pygame.image.load("graphics/PNG/cloud5.png")
    cloud5 = pygame.transform.scale(cloud5, (200, 85))
    cloud6 = pygame.image.load("graphics/PNG/cloud6.png")
    cloud6 = pygame.transform.scale(cloud6, (322, 151))
    return cloud1, cloud2, cloud3, cloud4, cloud5, cloud6'''
    #cloud6 = pygame.image.load("graphics/PNG/cloud6.png")
    #cloud6 = pygame.transform.scale(cloud6, (322, 151))
    play_img = pygame.image.load("graphics/play.png")
    play_img = pygame.transform.scale(play_img, (322, 151))
    how_img = pygame.image.load("graphics/howtoplay.png")
    how_img = pygame.transform.scale(how_img, (300, 200))
    lboard_img = pygame.image.load("graphics/leaderboard.png")
    lboard_img = pygame.transform.scale(lboard_img, (505, 135))
    return play_img, how_img, lboard_img #cloud6


def buttons(img, opacity, position):
    ''' Adding buttons/fading in to the screen '''
    img.set_alpha(opacity)
    rect = img.get_rect(center=position)
    screen.blit(img, rect)
    return rect

if __name__ == "__main__":
    # CONSTANT values like colours here
    SKYBLUE = (135, 206, 235)

    # Create vars for screen size and width/height of screen
    size = 1280, 720
    width, height = size
    #Initialization
    pygame.init()
    screen = pygame.display.set_mode(size)
    #background
    background1 = pygame.image.load('graphics/backgrounds/colored_castle.png')
    clock = pygame.time.Clock()
    #player
    player = Player()
    player_group = pygame.sprite.GroupSingle()
    player_group.add(player)

    #sounds
    pygame.mixer.music.load('sfx/calm.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    shoot = pygame.mixer.Sound('sfx/playershoot.wav')
    enemyDie = pygame.mixer.Sound('sfx/enemy_die.wav')
    #rocket 
    rocket_group = pygame.sprite.Group()
    #enemies
    enemies = pygame.sprite.Group()

    # Main game loop
    game()

    pygame.quit()
