import pygame

import random
import math

pygame.init()
win = pygame.display.set_mode((1024, 600))

pygame.display.set_caption("Alien destroyer")

icon = pygame.image.load('Images/icon.png')
pygame.display.set_icon(icon)

background_game = pygame.image.load('Images/background_game.jpg')
background_menu = pygame.image.load('Images/background_menu.jpg')


def background():
    win.blit(background_game, (0, 0))


# Звуки
sounds_on = True
pygame.mixer.music.load('Sounds/Megadeth.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1, 1)
sound_button_click = pygame.mixer.Sound('Sounds/button.wav')
sound_shot = pygame.mixer.Sound('Sounds/shot.wav')
sound_explosion = pygame.mixer.Sound('Sounds/explosion.wav')
sound_loss = pygame.mixer.Sound('Sounds/loss.wav')

# Игрок
shipStand = pygame.image.load('Images/Ship.png')
shipRun = pygame.image.load('Images/ShipRun.png')
shipX = 470
shipY = 430
ship_width = 95
ship_height = 160
ship_speed = 20

# Отображение движения корабля
motion = False


# Отрисовка корабля
def ship(x, y):
    global motion
    if motion:
        win.blit(shipRun, (x, y))
    else:
        win.blit(shipStand, (x, y))


# Снаряд
bullet = pygame.image.load('Images/Bullet.png')
bulletX = 0
bulletY = 430
bulletX_change = 0
bulletY_change = 20
bullet_state = False


def fire_bullet(x, y):
    global bullet_state, sounds_on
    bullet_state = True
    win.blit(bullet, (x + 44, y - 10))


# Враг №1
enemy1 = []
enemy2 = []
enemy3 = []
enemyX = []
enemyY = []
enemyX_change = []
enemy_width = []
enemy_height = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemy1.append(pygame.image.load('Images/Enemy1.png'))
    enemy2.append(pygame.image.load('Images/Enemy2.png'))
    enemy3.append(pygame.image.load('Images/Enemy3.png'))
    enemyX.append(random.randint(0, 600))
    enemyY.append(random.randint(0, 100))
    enemyX_change.append(5)
    enemy_width.append(120)
    enemy_height.append(89)


def enemy1show(x, y, i):
    win.blit(enemy1[i], (x, y))


def enemy2show(x, y, i):
    win.blit(enemy2[i], (x, y))


def enemy3show(x, y, i):
    win.blit(enemy3[i], (x, y))


def isCollision(firstX, firstY, secondX, secondY, boss_bool):
    global sounds_on
    distance = math.sqrt((math.pow(firstX - secondX, 2)) + (math.pow(firstY - secondY, 2)))
    if distance < 50 and not boss_bool:
        if sounds_on:
            pygame.mixer.Sound.play(sound_explosion)
        return True
    elif distance < 175 and boss_bool:
        if sounds_on:
            pygame.mixer.Sound.play(sound_explosion)
        return True
    else:
        return False


# Босс
boss = pygame.image.load('Images/Boss.png')
bossX = 412
bossY = 7
boss_height = 157
boss_width = 200
bossX_change = 1
boss_hits = 0


def boss_show(x, y):
    win.blit(boss, (x, y))


# Отображение текста
def print_text(message, x, y, font_color=(0, 0, 0), font_type='freesansbold.ttf', font_size=32):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    win.blit(text, (x, y))


# Счет
score = 0
score_textX = 10
score_textY = 10

# Конец игры
game_over_bool = False


def game_over():
    global game_over_bool, en_lang_bool, sounds_on
    if en_lang_bool:
        print_text(game_over_text, 300, 270, (255, 255, 255), 'freesansbold.ttf', 70)
    else:
        print_text(game_over_text, 270, 270, (255, 255, 255), 'freesansbold.ttf', 70)
    game_over_bool = True


# Запуск новой игры
def new_game():
    global en_lang_bool
    if en_lang_bool:
        print_text(new_game_text, 300, 340, (255, 255, 255), 'freesansbold.ttf', 32)
    else:
        print_text(new_game_text, 260, 340, (255, 255, 255), 'freesansbold.ttf', 32)


# Класс для кнопок
class Button:
    global sounds_on

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (118, 4, 189)
        self.active_color = (129, 9, 203)

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(win, self.active_color, (x, y, self.width, self.height))

            if click[0] == 1:
                if sounds_on:
                    pygame.mixer.Sound.play(sound_button_click)
                pygame.time.delay(300)
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()

        else:
            pygame.draw.rect(win, self.inactive_color, (x, y, self.width, self.height))

        print_text(message=message, x=x + 10, y=y + 10, font_size=font_size)


# Изменение языка
en_lang_bool = True
start_text = "Start game"
exit_text = "Exit"
game_over_text = "GAME OVER"
new_game_text = "click 'space' for a new game"
score_text = "Score: "
sound_on_text = "Sounds on"
sound_off_text = "Sounds off"
start_button_en_X = 368
start_button_en_Y = 160
exit_button_en_X = 452
exit_button_en_Y = 250

start_button_ua_X = 325
start_button_ua_Y = 160
exit_button_ua_X = 427
exit_button_ua_Y = 250


def select_en():
    global en_lang_bool
    en_lang_bool = True
    global start_text, exit_text, game_over_text, new_game_text, score_text, sound_on_text, sound_off_text
    start_text = "Start game"
    exit_text = "Exit"
    game_over_text = "GAME OVER"
    new_game_text = "click 'space' for a new game"
    score_text = "Score: "
    sound_on_text = "Sounds on"
    sound_off_text = "Sounds off"


def select_ua():
    global en_lang_bool
    en_lang_bool = False
    global start_text, exit_text, game_over_text, new_game_text, score_text, sound_on_text, sound_off_text
    start_text = "Розпочати гру"
    exit_text = "Вихід"
    game_over_text = "Гра закінчена"
    new_game_text = "натисніть 'space' для нової гри"
    score_text = "Рахунок: "
    sound_on_text = "Звуки ввімк."
    sound_off_text = "Звуки вимк."


# Управление звуками
def sound_on_select():
    global sounds_on
    sounds_on = True


def sound_off_select():
    global sounds_on
    sounds_on = False


# Инициализация меню
menu_bool = True


def menu():
    global event, menu_bool, en_lang_bool, sounds_on
    lang_en_button = Button(70, 60)
    lang_ua_button = Button(70, 60)
    pygame.mixer.music.pause()

    show_menu = True
    while show_menu:
        win.blit(background_menu, (0, -60))

        if en_lang_bool:
            start_button = Button(288, 70)
            exit_button = Button(120, 70)
            sound_on_button = Button(288, 60)
            sound_off_button = Button(288, 60)
            start_button.draw(start_button_en_X, start_button_en_Y, start_text, start_game, 50)
            exit_button.draw(exit_button_en_X, exit_button_en_Y, exit_text, quit, 50)
            sound_on_button.draw(690, 450, sound_on_text, sound_on_select, 50)
            sound_off_button.draw(690, 520, sound_off_text, sound_off_select, 50)
        else:
            start_button = Button(375, 70)
            exit_button = Button(170, 70)
            sound_on_button = Button(330, 60)
            sound_off_button = Button(330, 60)
            start_button.draw(start_button_ua_X, start_button_ua_Y, start_text, start_game, 50)
            exit_button.draw(exit_button_ua_X, exit_button_ua_Y, exit_text, quit, 50)
            sound_on_button.draw(690, 450, sound_on_text, sound_on_select, 50)
            sound_off_button.draw(690, 520, sound_off_text, sound_off_select, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        lang_en_button.draw(30, 520, "En", select_en, 40)
        lang_ua_button.draw(120, 520, "Ua", select_ua, 40)

        if not menu_bool:
            show_menu = False
            pygame.mixer.music.unpause()

        pygame.display.update()


def start_game():
    global menu_bool
    menu_bool = False


# Игровой цикл
run = True

while run:
    global event
    if menu_bool:
        menu()
    else:
        pygame.time.delay(30)
        background()

        if not sounds_on:
            pygame.mixer.music.pause()
        if sounds_on:
            pygame.mixer.music.unpause()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Управление
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and shipX > ship_speed:
                shipX -= ship_speed
                motion = True
            if event.key == pygame.K_RIGHT and shipX < 1024 - ship_speed - ship_width:
                shipX += ship_speed
                motion = True
            if event.key == pygame.K_SPACE:
                motion = False
                if not bullet_state:
                    if sounds_on:
                        pygame.mixer.Sound.play(sound_shot)
                    bulletX = shipX
                    fire_bullet(shipX, bulletY)
            if event.key == pygame.K_SPACE and game_over_bool:
                score = 0
                game_over_bool = False
                bossY = 7
                pygame.mixer.music.play(-1, 1)
                for j in range(num_of_enemy):
                    enemyY[j] = 50

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                motion = False

        # Движение противника
        for i in range(num_of_enemy):

            # Конец игры
            if enemyY[i] >= (430 - enemy_height[i]):
                for j in range(num_of_enemy):
                    enemyY[j] = 2000
                pygame.mixer.music.stop()
                game_over()
                new_game()
                one = 1
                if sounds_on and one == 1:
                    pygame.mixer.Sound.play(sound_loss)
                    one += 1
                break

            # Изменение скорости противников в зависимости от количества очков
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                if score >= 0:
                    enemyX_change[i] = 5
                if score >= 50:
                    enemyX_change[i] = 6
                if score >= 100:
                    enemyX_change[i] = 8
                if score >= 200:
                    enemyX_change[i] = 12
                enemyY[i] += enemy_height[i]
            elif enemyX[i] >= 1024 - enemy_width[i] - enemyX_change[i]:
                if score >= 0:
                    enemyX_change[i] = -5
                if score >= 50:
                    enemyX_change[i] = -6
                if score >= 100:
                    enemyX_change[i] = -8
                if score >= 200:
                    enemyX_change[i] = -12
                enemyY[i] += enemy_height[i]

            # Изменение противников, в зависимости от количества очков
            if score >= 0:
                enemy1show(enemyX[i], enemyY[i], i)
            if score >= 100:
                enemy2show(enemyX[i], enemyY[i], i)
            if score >= 200:
                enemy3show(enemyX[i], enemyY[i], i)

            # Вызов Босса
            if score == 100:
                for j in range(num_of_enemy):
                    enemyY[j] = -2000
                boss_show(bossX, bossY)

                # Движение Босса
                bossX += bossX_change
                if bossX <= 0:
                    bossX_change = 1
                    bossY += boss_height
                if bossX >= 1024 - boss_width - bossX_change:
                    bossX_change = -1
                    bossY += boss_height

                # Проверка колизии Босса
                boss_collision = isCollision(bossX, bossY, bulletX, bulletY, True)
                if boss_collision:
                    bulletY = 430
                    bullet_state = False
                    boss_hits += 1
                if boss_hits == 5:
                    score += 1
                    for j in range(num_of_enemy):
                        enemyY[j] = 50

                # Конец игры
                if bossY >=(430 - boss_height):
                    bossY = 2000
                    pygame.mixer.music.stop()
                    game_over()
                    new_game()
                    one = 1
                    if sounds_on and one == 1:
                        pygame.mixer.Sound.play(sound_loss)
                        one += 1
                    break

            # Проверка колизии обычных противников
            collision_enemy = isCollision(enemyX[i], enemyY[i], bulletX, bulletY, False)
            if collision_enemy:
                bulletY = 430
                bullet_state = False
                score += 1
                enemyX[i] = random.randint(0, 600)
                enemyY[i] = random.randint(0, 100)

        # Движение заряда
        if bulletY <= 0:
            bulletY = 430
            bullet_state = False
        if bullet_state:
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        ship(shipX, shipY)
        print_text(score_text + str(score), score_textX, score_textY, (120, 0, 82), 'freesansbold.ttf', 32)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu_bool = True

        pygame.display.update()
