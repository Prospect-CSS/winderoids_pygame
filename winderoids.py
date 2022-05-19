import pygame
import random
from os import path



#main game loop =========================================================================
game_loose = True
game_over = True
game_start = True
while game_start:

    img_dir = path.join(path.dirname(__file__), 'img')
    voice_dir = path.join(path.dirname(__file__), 'voice')
    #game variables=============================================================================================
    WIDTH = 650 # WIDTH OF GAME WINDOW
    HEIGHT = 650 # HEIGHT OF GAME WINDOW
    FPS = 60 # UPDATES PER SECOND
    POWERUP_TIME = 50000 # working time for powerUps
    # colors (R, G, B)=============================================================================================
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    score = 0

    # game initialization =======================================================================
    pygame.init() 
    pygame.mixer.init() # voice in game
    screen = pygame.display.set_mode((WIDTH,HEIGHT)) # vareable with all screen sizes
    pygame.display.set_caption("Winderoids") # game window name
    clock = pygame.time.Clock() # variable for displaying FPS in game

    # text =====================================================================================
    font_name = pygame.font.match_font('monospace')

    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    # player shield
    def draw_shield_bar(surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, GREEN, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)

    # player lives
    def draw_lives(surf, x, y, lives, img):
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            surf.blit(img, img_rect)

    # Create new mobs
    def newmob():
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    
    def show_start_screen ():
        print(show_start_screen)
        screen.blit(background, background_rect)
        draw_text(screen, "Welcome to Winderoids", 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, "Good luck have fun", 22,
                WIDTH / 2, HEIGHT / 2)
        draw_text(screen, "To start press \"TAB\"", 18, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_TAB]:
                    waiting = False


    def show_go_screen():
        print("show_go_screen")
        screen.blit(background, background_rect)
        draw_text(screen, "Winderoids", 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, "Arrow keys move, Space to fire", 22,
                WIDTH / 2, HEIGHT / 2)
        draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            show_level_1()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    waiting = False 
    


    

    
    def show_level_1 ():
        print("show_level_1")
        screen.blit(background, background_rect)
        draw_text(screen, "Winderoids", 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, "Level one ", 22,
                WIDTH / 2, HEIGHT / 2)
        draw_text(screen, "All asteroids come from the top,", 22,
                WIDTH / 2, HEIGHT / 2 + 30)
        draw_text(screen, "You need destroy them, and gain a score of 3000", 22,
                WIDTH / 2, HEIGHT / 2 + 60)
        draw_text(screen, "To start press \"TAB\"", 18, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        if score > 3000:
            show_go_screen_level2()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_TAB]:
                    waiting = False

    
    def show_go_screen_level2():
        print("show_go_screen")
        screen.blit(background, background_rect)
        draw_text(screen, "Winderoids", 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, "LEVEL 2", 22,
                WIDTH / 2, HEIGHT / 2)
        draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            show_level_2()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    waiting = False 

    def show_level_2 ():
        print("show_level_1")
        screen.blit(background, background_rect)
        draw_text(screen, "Winderoids", 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, "Level one ", 22,
                WIDTH / 2, HEIGHT / 2)
        draw_text(screen, "All asteroids come from the top,", 22,
                WIDTH / 2, HEIGHT / 2 + 30)
        draw_text(screen, "You need destroy them, and gain a score of 3000", 22,
                WIDTH / 2, HEIGHT / 2 + 60)
        draw_text(screen, "To start press \"TAB\"", 18, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        if score > 5000:
            show_go_screen_level3
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_TAB]:
                    waiting = False

    def show_go_screen_level3():
        print("show_go_screen")
        screen.blit(background, background_rect)
        draw_text(screen, "Winderoids", 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, "LEVEL 2", 22,
                WIDTH / 2, HEIGHT / 2)
        draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            show_level_2()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    waiting = False 

    class Player(pygame.sprite.Sprite):
        MANEUVERABILITY = 3 #
        ACCELERATION = 0.25 #
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img, (50, 38))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = 20
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT / 2
            self.speedx = 0
            self.speedY = 0
            self.rot = 0
            self.rot_speed = 0
            self.shield = 100
            self.shoot_delay = 250
            self.last_shot = pygame.time.get_ticks()
            self.lives = 3
            self.hidden = False
            self.hide_timer = pygame.time.get_ticks()
            self.power = 1
            self.power_time = pygame.time.get_ticks()
        def accelerate(self): #
            self.velocity += self.direction * self.ACCELERATION


        def update(self):
            # timeout for powerups
            if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
                self.power -= 1
                self.power_time = pygame.time.get_ticks()
            # hide if not hide
            if self.hidden and pygame.time.get_ticks() - self.hide_timer > 2000:
                self.hidden = False
                self.rect.centerx = WIDTH / 2
                self.rect.bottom = HEIGHT / 2

            self.speedx = 0
            self.speedy = 0
            keystate = pygame.key.get_pressed()
            
            if keystate[pygame.K_LEFT]:
                self.speedx = -8
            if keystate[pygame.K_RIGHT]:
                self.speedx = 8
            if keystate[pygame.K_UP]:
                self.speedy = -8
            if keystate[pygame.K_DOWN]:
                self.speedy = 8
            if keystate[pygame.K_SPACE]:
                self.shoot()

            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
       
            if self.rect.left < 0:
                self.rect.left = 0
         
            if self.rect.top >= HEIGHT:
                self.rect.top = HEIGHT
          
            if self.rect.bottom <= 0:
                self.rect.bottom = 0
                

        def powerup(self):
            self.power += 1
            self.power_time = pygame.time.get_ticks()
    
        def shoot(self):
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.last_shot = now
                if self.power == 1:
                    bullet = Bullet(self.rect.centerx, self.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    shoot_sound.play()
                if self.power >= 2:
                    bullet1 = Bullet(self.rect.left, self.rect.centery)
                    bullet2 = Bullet(self.rect.right, self.rect.centery)
                    all_sprites.add(bullet1)
                    all_sprites.add(bullet2)
                    bullets.add(bullet1)
                    bullets.add(bullet2)
                    self.shoot_delay = 500
                    shoot_sound.play()
                if self.power >= 3:
                    bullet1 = Bullet(self.rect.left, self.rect.centery)
                    bullet3 = Bullet(self.rect.centerx, self.rect.top)
                    bullet2 = Bullet(self.rect.right, self.rect.centery)
                    all_sprites.add(bullet1)
                    all_sprites.add(bullet2)
                    all_sprites.add(bullet3) 
                    bullets.add(bullet1)
                    bullets.add(bullet2)
                    bullets.add(bullet3)
                    self.shoot_delay = 750
                    shoot_sound.play()
                if self.power >= 4:
                    self.shoot_delay = 500
                    self.power += 1
                if self.power >= 5:
                    self.shoot_delay = 250
                    self.power += 1
                if self.power >= 6:
                    self.shoot_delay = 100
                    self.power == 6


        def hide(self):
            # temp hide player
            self.hidden = True
            self.shoot_delay = self.hide_timer
            self.hide_timer = pygame.time.get_ticks()
            self.rect.center = (WIDTH / 2, HEIGHT + 200)

    # mob class
    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_orig = random.choice(meteor_images)
            self.image_orig.set_colorkey(BLACK)
            self.image = self.image_orig.copy()
            self.rect = self.image.get_rect()
            self.radius = int(self.rect.width * .85 / 2)
            # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, -100)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)
            self.rot = 0
            self.rot_speed = random.randrange(-8, 8)
            self.last_update = pygame.time.get_ticks()
            self.shield = int(self.rect.width * .85 / 2)

        def rotate(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > 50:
                self.last_update = now
                self.rot = (self.rot + self.rot_speed) % 360
                new_image = pygame.transform.rotate(self.image_orig, self.rot)
                old_center = self.rect.center
                self.image = new_image
                self.rect = self.image.get_rect()
                self.rect.center = old_center
        
        
        def update(self):
            self.rotate()
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 8)

    # bullet class
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_img
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = -10
            self.power = 50

        def update(self):
            self.rect.y += self.speedy
            # убить, если он заходит за верхнюю часть экрана
            if self.rect.bottom < 0:
                self.kill()

    # class powerups
    class Pow(pygame.sprite.Sprite):
        def __init__(self, center):
            pygame.sprite.Sprite.__init__(self)
            self.type = random.choice(['shield', 'gun'])
            self.image = powerup_images[self.type]
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.speedy = 2

        def update(self):
            self.rect.y += self.speedy
            # убить, если он сдвинется с нижней части экрана
            if self.rect.top > HEIGHT:
                self.kill()

    # class explosions
    class Explosion(pygame.sprite.Sprite):
        def __init__(self, center, size):
            pygame.sprite.Sprite.__init__(self)
            self.size = size
            self.image = explosion_anim[self.size][0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.frame = 0
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 50

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(explosion_anim[self.size]):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = explosion_anim[self.size][self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center


    #graphics in the game
    background = pygame.image.load(path.join(img_dir, "Backgrounds\starbg.jpg")).convert()
    background_rect = background.get_rect()
    #player battle ship image
    player_img = pygame.image.load(path.join(img_dir, "PNG/playerShip1_orange.png")).convert_alpha()
    player_mini_img = pygame.transform.scale(player_img, (25, 19))
    player_mini_img.set_colorkey(BLACK)
    #Bullet image
    bullet_img = pygame.image.load(path.join(img_dir, "PNG/Lasers/laserRed16.png")).convert_alpha()
    #mobs images
    meteor_images = []
    meteor_list = ['PNG\Meteors\meteorBrown_big1.png', 
                    'PNG\Meteors\meteorBrown_med1.png', 
                    'PNG\Meteors\meteorBrown_med1.png',
                    'PNG\Meteors\meteorBrown_med3.png', 
                    'PNG\Meteors\meteorBrown_small1.png', 
                    'PNG\Meteors\meteorBrown_small2.png',
                    'PNG\Meteors\meteorBrown_tiny1.png']
    for folder in meteor_list:
        meteor_images.append(pygame.image.load(path.join(img_dir, folder)).convert_alpha())

    #explosion images
    explosion_anim = {}
    explosion_anim['lg'] = []
    explosion_anim['sm'] = []
    explosion_anim['player'] = []
    for i in range(9):
        filename = 'explosions/regularExplosion0{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert_alpha()
        img.set_colorkey(BLACK)
        img_lg = pygame.transform.scale(img, (75, 75))
        explosion_anim['lg'].append(img_lg)
        img_sm = pygame.transform.scale(img, (32, 32))
        explosion_anim['sm'].append(img_sm)
        filename = 'explosions/sonicExplosion0{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert_alpha()
        img.set_colorkey(BLACK)
        explosion_anim['player'].append(img)

    #PowerUps images
    powerup_images = {}
    powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'powerUp/shield_gold.png')).convert_alpha()
    powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'powerUp/bolt_gold.png')).convert_alpha()

    #music
    shoot_sound = pygame.mixer.Sound(path.join(voice_dir, 'sfx_laser1.ogg'))
    shield_sound = pygame.mixer.Sound(path.join(voice_dir, 'powerUp/sfx_shieldUp.ogg'))
    power_sound = pygame.mixer.Sound(path.join(voice_dir, 'powerUp/sfx_zap.ogg'))
    expl_sounds = []
    for voice in ['Explosion2.wav', 'Explosion5.wav']:
        expl_sounds.append(pygame.mixer.Sound(path.join(voice_dir, voice)))

    pygame.mixer.music.load(path.join(voice_dir, '1.mp3'))
    pygame.mixer.music.set_volume(0 )
    pygame.mixer.music.play(loops=-1) 



    first_level_running = True
    show_start_screen()
    while first_level_running:
        
       
        if game_over:
            show_go_screen()
            game_over = False
            all_sprites = pygame.sprite.Group()
            mobs = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            powerups = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)
            for i in range(12):
                newmob()
            score = 0
        
        #game speed contro; 
        clock.tick(FPS)
        #events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
        #updates
        all_sprites.update() # update sprites

        #check if hit by bullet
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            score += 50 - hit.radius
            random.choice(expl_sounds).play()
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            if random.random() > 0.9:
                pow = Pow(hit.rect.center)
                all_sprites.add(pow)
                powerups.add(pow)
            newmob()

        #check if mob hit player
        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits: 
            player.shield -= hit.radius * hit.speedy / 3
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            newmob()
            if player.shield <= 0:
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100
            
        # check colusion with powerUps
        hits = pygame.sprite.spritecollide(player, powerups, True)
        for hit in hits:
            if hit.type == 'shield':
                player.shield += random.randrange(10, 30)
                if player.shield >= 100:
                    player.shield = 100
            if hit.type == 'gun':
                player.powerup()
                power_sound.play()
        # if player died game end
        if player.lives == 0 and not death_explosion.alive():
            game_over = True
        elif score > 100:
            for i in range(0):
                newmob()
            first_level_running = False
        #rendering 
        screen.fill(BLACK) #background color
        screen.blit(background, background_rect)
        draw_text(screen, "Level 1",10,WIDTH//2, HEIGHT - 20)
        draw_text(screen, str(score), 18, WIDTH / 2, 10)
        draw_shield_bar(screen, 5, 5, player.shield)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
        
        
        
        all_sprites.draw(screen) #sprites drawing
        #last function for change screen
        pygame.display.flip()
    
    #level 2
    second_level_running = True
    while second_level_running:
        if game_over:
            show_go_screen()
            game_over = False
            all_sprites = pygame.sprite.Group()
            mobs = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            powerups = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)
            for i in range(42):
                newmob()
            score = 0
        
        #game speed contro; 
        clock.tick(FPS)
        #events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
        #updates
        all_sprites.update() # update sprites

        #check if hit by bullet
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            score += 50 - hit.radius
            random.choice(expl_sounds).play()
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            if random.random() > 0.9:
                pow = Pow(hit.rect.center)
                all_sprites.add(pow)
                powerups.add(pow)
            newmob()

        #check if mob hit player
        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits: 
            player.shield -= hit.radius * hit.speedy / 3
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            newmob()
            if player.shield <= 0:
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100
            # if Mob.shield <= 0:
                

        # check colusion wirh powerUps
        hits = pygame.sprite.spritecollide(player, powerups, True)
        for hit in hits:
            if hit.type == 'shield':
                player.shield += random.randrange(10, 30)
                if player.shield >= 100:
                    player.shield = 100
            if hit.type == 'gun':
                player.powerup()
                power_sound.play()
        # if player died game end
        if player.lives == 0 and not death_explosion.alive():
            game_over = True
        elif score > 9000:
            game_over = True
        #rendering 
        screen.fill(BLACK) #background color
        screen.blit(background, background_rect)
        draw_text(screen, "Level 2",10,WIDTH//2, HEIGHT - 20)
        draw_text(screen, str(score), 18, WIDTH / 2, 10)
        draw_shield_bar(screen, 5, 5, player.shield)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
        
        
        
        all_sprites.draw(screen) #sprites drawing
        #last function for change screen
        pygame.display.flip()

pygame.quit()
