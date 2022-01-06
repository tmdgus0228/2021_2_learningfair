import pygame
import sys
import random
import math
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_SPACE,Rect
import time
from time import sleep
from pygame.constants import QUIT

pygame.init()

# 색 지정 
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
NeonPink = (249, 6, 214)
NeonGreen = (149, 255, 0)
NeonPurple = (233, 0, 255)
NeonGgreen = (0, 249, 42)


# 각 게임의 탈출 열쇠 상태를 False로 지정
Runkey = False
Shootkey = False
Breakkey = False

delay = 1000  # 화면 딜레이 변수 (ms)

# 화면 크기
display_width = 1000
display_height = 800

# 화면 설정
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("오락실에서 살아남기")
clock = pygame.time.Clock()

# 배경화면 함수 
def background():
    gameDisplay.blit(pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/arcade.jpg"), (0, 0))

# 열쇠 이미지 지정 
key = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/key.png")
key_size = key.get_rect().size

# 이미지 지정 
yellow = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/yellow.jpg")
god = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/god.jpg")
ending = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images//end.jpg")
How = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/How.jpg")
door0 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/door0.jpg")
door1 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/door1.jpg")
door2 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/door2.jpg")
bubble = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/bubble.png")

# 텍스트 설정 함수 지정 
def text_objects(text, font): 
    textSurface = font.render(text, True, white) 
    return textSurface, textSurface.get_rect()

#폰트 지정 
smallText = pygame.font.SysFont(None, 20)
bigText = pygame.font.SysFont(None, 50)
korText = pygame.font.Font("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/NanumSoMiCe.ttf", 50)  # 글꼴, 크기
storyText = pygame.font.Font("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/NanumBaReunJeongSin.ttf", 40)  # 글꼴, 크기  
nextText = pygame.font.Font("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/NanumSoMiCe.ttf", 70) # 글꼴, 크기  

# 게임 시작화면 버튼 함수(블로그 참고)
def button(txt, x, y, w, h, ic, ac, font, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h> mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))  # 버튼 그리기 
        if click[0] == 1 and action != None:
            action()        
    else: 
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    
    textSurt, textRect = text_objects(txt, font)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurt, textRect)

# 게임 종료 함수 
def quitgame():
    pygame.quit()
    sys.exit()

# 스토리 화면 함수들
def introScreen():
    intro = True  # 인트로 시작 

    while intro:  # 인트로가 True일 동안 반복 
        for event in pygame.event.get():   # 이벤트 지정 
            if event.type == pygame.QUIT:  # 만약 나가기 이벤트(X를 눌렀거나 게임종료 버튼을 눌렀을 때)
                quitgame()                 # 게임종료
        
        gameDisplay.fill(black)            # 화면을 검정으로 채우기 
        background()                       # 배경화면 함수 불러옴 
        # 화면 윗부분에 게임 제목 띄우기 
        largeText = pygame.font.Font("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/NanumSoMiCe.ttf", 140)   
        TextSurf, TextRect = text_objects("오락실에서 살아남기", largeText) 
        TextRect.center = ((display_width / 2), (display_height / 2 - 200))
        gameDisplay.blit(TextSurf, TextRect)

        # 두 개의 버튼 생성(함수)
        button("게임시작", display_width * 0.3 - 100, 450, 200, 100, NeonGgreen, NeonGreen, korText, storyScreen0)
        button("게임종료", display_width * 0.7 - 100 , 450, 200, 100, NeonPink, NeonPurple, korText, quitgame)

        pygame.display.update()  # 기본으로 해주는 작업
        clock.tick(15)  

def storyScreen0(): # 주인공 독백 화면 
    story0 = True  # 독백 화면 시작 
    timer = 0      # 변수 초기화

    while story0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        timer += 1     # timer를 1씩 증가 
        gameDisplay.fill(white)   # 화면을 흰색으로 채우기 
        gameDisplay.blit(yellow, (0, 0))   # 화면에 yellow에 지정된 이미지 띄우기 

        # 텍스트 부분 설정
        story0_text0 = storyText.render("윽... 여기가 어디지?", True, white)
        story0_text1 = storyText.render("어... 여긴 오락실?", True, white)
        story0_text2 = storyText.render("아.. 나 게임 싫어하는데 왜 오락실에 있는거지?", True, white)
        story0_text3 = storyText.render("그때 어디선가 목소리가 들렸다", True, white)

        # 텍스트 위치 지정 
        story0_text_xpos = 180
        story0_text0_ypos = display_height * 0.28
        story0_text1_ypos = display_height * 0.38
        story0_text2_ypos = display_height * 0.48
        story0_text3_ypos = display_height * 0.58
        
        # 텍스트가 천천히 나오도록 지정 
        if delay > timer:  # 첫 번째 줄 띄우기 
            gameDisplay.blit(story0_text0, (story0_text_xpos, story0_text0_ypos))
        elif delay * 2 > timer >= delay:  # 기존 첫 번째 줄 띄우기 + 두 번째 줄 띄우기 
            gameDisplay.blit(story0_text0, (story0_text_xpos, story0_text0_ypos))
            gameDisplay.blit(story0_text1, (story0_text_xpos, story0_text1_ypos))
        elif delay * 3 > timer >= delay * 2:  # 기존 + 세 번째 줄
            gameDisplay.blit(story0_text0, (story0_text_xpos, story0_text0_ypos))
            gameDisplay.blit(story0_text1, (story0_text_xpos, story0_text1_ypos))
            gameDisplay.blit(story0_text2, (story0_text_xpos, story0_text2_ypos))
        else:  # 기존 + 네 번째 줄
            gameDisplay.blit(story0_text0, (story0_text_xpos, story0_text0_ypos))
            gameDisplay.blit(story0_text1, (story0_text_xpos, story0_text1_ypos))
            gameDisplay.blit(story0_text2, (story0_text_xpos, story0_text2_ypos))
            gameDisplay.blit(story0_text3, (story0_text_xpos, story0_text3_ypos))
            button("다음", display_width - 250, display_height - 150, 200, 100, black, white, nextText, storyScreen)   # 다음 버튼 생성 
        
        pygame.display.update()

def storyScreen(): # 게임의 신 발언부분 화면 
    story = True
    timer = 0

    while story:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        timer += 1
        gameDisplay.fill((255, 255, 255))
        gameDisplay.blit(god, (0, 0))

        story_text0 = storyText.render('" 나는 게임의 신이다', True, white)
        story_text1 = storyText.render("자네는 평소에 게임을 소중히 여기지 않았지...", True, white)
        story_text2 = storyText.render("게임의 즐거움을 모르는 너에게 즐거움을 알려주지", True, white)
        story_text3 = storyText.render('집에 가고싶다면 오락실을 탈출해보거라 "', True, white)

        story_text_xpos = 200
        story_text0_ypos = display_height * 0.3
        story_text1_ypos = display_height * 0.4
        story_text2_ypos = display_height * 0.5
        story_text3_ypos = display_height * 0.6

        if delay > timer:
            gameDisplay.blit(story_text0, (story_text_xpos, story_text0_ypos))
        elif delay * 2 > timer >= delay:
            gameDisplay.blit(story_text0, (story_text_xpos, story_text0_ypos))
            gameDisplay.blit(story_text1, (story_text_xpos, story_text1_ypos))
        elif delay * 3 > timer >= delay * 2:
            gameDisplay.blit(story_text0, (story_text_xpos, story_text0_ypos))
            gameDisplay.blit(story_text1, (story_text_xpos, story_text1_ypos))
            gameDisplay.blit(story_text2, (story_text_xpos, story_text2_ypos))
        else:
            gameDisplay.blit(story_text0, (story_text_xpos, story_text0_ypos))
            gameDisplay.blit(story_text1, (story_text_xpos, story_text1_ypos))
            gameDisplay.blit(story_text2, (story_text_xpos, story_text2_ypos))
            gameDisplay.blit(story_text3, (story_text_xpos, story_text3_ypos))
            button("게임방법", display_width - 250, display_height - 150, 200, 100, black, white, nextText, HowToPlay)
        
        pygame.display.update()

def HowToPlay():  # 게임방법 화면 
    howrun = True
    timer = 0
    while howrun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        timer += 1
        gameDisplay.blit(How, (0, 0))
        if timer > delay:  # 일정시간 지난 후 다음 버튼 띄우기 
            button("다음", display_width - 250, display_height - 150, 200, 100, black, white, nextText, door0Screen)
        
        pygame.display.update()

def door0Screen():  # 첫번째 문 열쇠를 얻는 단계의 화면 
    door0run = True
    while door0run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(door0, (0, 0))
        button("달리기게임", display_width * 0.3 - 200, display_height / 2 - 50, 200, 100, black, white, korText, RunGame)  # 달리기게임 플레이버튼 띄우기 
        pygame.display.update()

def RunGame():  # 달리기게임 코드 부분 
    screen_width = 1000
    screen_height = 800
    xpad = 200
    ypad = 125
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("달리기 게임")
    clock = pygame.time.Clock()

    #바닥
    floor0 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/floor.png")
    floor1 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/floor.png")
    floor_xpos = xpad
    floor_ypos = screen_width - screen_height/1.6
    floor_xpos_defult = xpad

    #천장
    ceiling0 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/floor.png")
    ceiling1 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/floor.png")
    ceiling_size = ceiling0.get_rect().size
    ceiling_xpos = xpad
    ceiling_ypos = -45 + ypad

    #캐릭터
    run1 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/run1.png")
    run2 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/run2.png")
    run3 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/run3.png")
    jump = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/jump.png")
    roll = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/roll.png")
    chara_size = run1.get_rect().size
    chara_width = chara_size[0]
    chara_height = chara_size[1]
    chara_xpos = 20 + xpad
    chara_ypos_default = floor_ypos - chara_height
    chara_ypos = chara_ypos_default
    jump_y = 150

    #장애물
    block1_image = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/block1.png")
    block2_image = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/block2.png")
    block3_image = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/block3.png")
    block1_size = block1_image.get_rect().size
    block1_ypos = floor_ypos - block1_size[1]
    block2_size = block2_image.get_rect().size
    block2_ypos = floor_ypos - block2_size[1]
    block3_size = block3_image.get_rect().size
    block3_ypos = ceiling_ypos + ceiling_size[1]

    block1s = []
    block2s = []
    block3s = []

    block1_xpos = []
    block2_xpos = []
    block3_xpos = []

    block_rects = []

    #목숨
    heart_image = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/heart.png")
    heart_size = heart_image.get_rect().size
    heart_xpos = screen_width - heart_size[0] - xpad
    heart_ypos = screen_height - 100 - ypad
    hearts = []
    for i in range(3):
        heart = heart_image.get_rect(left = heart_xpos, top = heart_ypos)
        hearts.append(heart)

    #padding
    padding0 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/black1.png")
    padding0_xpos = 0
    padding0_ypos = 0
    padding1 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/black1.png")
    padding1_xpos = padding0_xpos + 800
    padding1_ypos = padding0_ypos

    font = pygame.font.SysFont(None, 50)
    end_font = pygame.font.SysFont(None, 100)
    running = True
    double_jump = False
    image = 0
    timer = 0
    speed = 15
    heart_int = 3
    end = False
    endtimer = 60

    Runkey = False

    while running:
        dt = clock.tick(30)
        timer += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:#점프
                    if chara_ypos == chara_ypos_default:#바닥에 있으면
                        image = "jump"
                        chara_ypos = chara_ypos_default - jump_y#점프
                        double_jump = True#더블점프허용
                    elif double_jump:#더블점프허용이면
                        image = "jump"
                        chara_ypos -= jump_y#점프
                        double_jump = False#더블점프끄기
                if event.key == pygame.K_DOWN:#구르기
                    image = "roll"
                    chara_ypos = chara_ypos_default + 30
                if event.key == pygame.K_0:
                    screen.blit(key, (((screen_width - key_size[0]) / 2), (screen_height - key_size[1]) / 2))
                    Runkey = True
                    end = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    image = 0
                    chara_ypos = chara_ypos_default

        if chara_ypos < chara_ypos_default:#중력
            chara_ypos += 10
        
        if chara_ypos == chara_ypos_default and image == "jump":#점프끝나고 다시 달리기
            image = 0

        #배경화면
        screen.fill((0, 0, 0))
        #텍스트배치
        score_text = font.render("SCORE: " + str(timer // 30), True, "white")
        screen.blit(score_text, (20 + xpad, 500 + ypad))
        #목숨배치
        for i in range(heart_int):
            screen.blit(heart_image, (heart_xpos - (heart_size[0] * (i)), heart_ypos))
        #바닥배치
        screen.blit(floor0, (floor_xpos, floor_ypos))
        screen.blit(floor1, (floor_xpos + 600, floor_ypos))
        #천장배치
        screen.blit(ceiling0, (ceiling_xpos, ceiling_ypos))
        screen.blit(ceiling1, (ceiling_xpos + 600, ceiling_ypos))
        #캐릭터배치
        if image == "jump":
            screen.blit(jump, (chara_xpos, chara_ypos))
        elif image == "roll":
            screen.blit(roll, (chara_xpos, chara_ypos))
        else:
            image += 1
            if(image < 5):
                screen.blit(run1, (chara_xpos, chara_ypos))
            elif(10 > image > 5):
                screen.blit(run2, (chara_xpos, chara_ypos))
            elif(image > 10):
                screen.blit(run3, (chara_xpos, chara_ypos))
            if image > 15:
                image = 0

        #바닥 움직임
        floor_xpos -= speed
        if(floor_xpos < -600 + xpad):
            floor_xpos = 0
        #천장 움직임
        ceiling_xpos -= speed
        if(ceiling_xpos < -600 + xpad):
            ceiling_xpos = 0

        #장애물 추가
        if timer % 30 == 0:
            num = random.randint(0, 2)
            if num == 0:
                block1 = block1_image.get_rect(left = 600, top = block1_ypos)
                block1s.append(block1)
                block1_xpos.append(600 + xpad)
            elif num == 1:
                block2 = block2_image.get_rect(left = 600, top = block2_ypos)
                block2s.append(block2)
                block2_xpos.append(600 + xpad)
            else:
                block3 = block3_image.get_rect(left = 600, top = block3_ypos)
                block3s.append(block3)
                block3_xpos.append(600 + xpad)
        #장애물 배치
        for i in range(len(block1s)):
            block1s[i].left = block1_xpos[i]
        for i in range(len(block2s)):
            block2s[i].left = block2_xpos[i]
        for i in range(len(block3s)):
            block3s[i].left = block3_xpos[i]
            
        for i in range(len(block1s)):
            screen.blit(block1_image, block1s[i])
        for i in range(len(block2s)):
            screen.blit(block2_image, block2s[i])
        for i in range(len(block3s)):
            screen.blit(block3_image, block3s[i])
        #장애물 움직임
        for i in range(len(block1_xpos)):
            block1_xpos[i] -= speed
        for i in range(len(block2_xpos)):
            block2_xpos[i] -= speed
        for i in range(len(block3_xpos)):
            block3_xpos[i] -= speed
        
        #캐릭터 충돌
        run_rect = run1.get_rect()
        run_rect.left = chara_xpos
        run_rect.top = chara_ypos

        jump_rect = jump.get_rect()
        jump_rect.left = chara_xpos
        jump_rect.top = chara_ypos

        roll_rect = roll.get_rect()
        roll_rect.left = chara_xpos
        roll_rect.top = chara_ypos
        
        if len(block1s) > 0:
            if run_rect.colliderect(block1s[0]) or jump_rect.colliderect(block1s[0]) or roll_rect.colliderect(block1s[0]):
                heart_int -= 1
                del block1s[0]
                del block1_xpos[0]
        if len(block2s) > 0:
            if run_rect.colliderect(block2s[0]) or jump_rect.colliderect(block2s[0]) or roll_rect.colliderect(block2s[0]):
                heart_int -= 1
                del block2s[0]
                del block2_xpos[0]
        if len(block3s) > 0:
            if run_rect.colliderect(block3s[0]) or jump_rect.colliderect(block3s[0]) or roll_rect.colliderect(block3s[0]):
                heart_int -= 1
                del block3s[0]
                del block3_xpos[0]

        #배열 정리
        for i in range(len(block1s)):
            try:#오류가 나는데 대체 왜그런지 모르겠어서..
                if block1_xpos[i] < chara_xpos:
                    del block1s[0]
                    del block1_xpos[0]
            except:
                pass
        for i in range(len(block2s)):
            try:
                if block2_xpos[i] < chara_xpos:
                    del block2s[0]
                    del block2_xpos[0]
            except:
                pass
        for i in range(len(block3s)):
            try:
                if block3_xpos[i] < chara_xpos:
                    del block3s[0]
                    del block3_xpos[0]
            except:
                pass
        #게임 오버
        if heart_int <= 0:
            end_text = end_font.render("GameOver", True, "white")
            end_text_size = end_text.get_size()
            screen.blit(end_text, ((screen_width- end_text_size[0]) / 2, (screen_height - end_text_size[1]) / 2))
            end = True
            
        #클리어
        elif timer > 900:
            screen.blit(key, (((screen_width - key_size[0]) / 2), (screen_height - key_size[1]) / 2))
            Runkey = True
            end = True

        #padding배치
        screen.blit(padding0, (padding0_xpos, padding0_ypos))
        screen.blit(padding1, (padding1_xpos, padding1_ypos))

        if end:
            endtimer -= 1
        if endtimer < 0:
            if Runkey:
                door1Screen()
            else:
                door0Screen()
            running = False

        pygame.display.update()

def door1Screen(): # 달리기게임 클리어한 후의 화면 
    door1run = True
    while door1run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(door1, (0, 0))
        button("비행기게임", display_width * 0.5 - 130, display_height / 2 - 50, 270, 100, black, white, korText, shootingGame)  #비행기게임 플레이버튼 띄우기 
        pygame.display.update()
    
def shootingGame():  # 비행기게임 코드 부분 
    # 화면 크기
    screen_width = 1000 # 가로 크기
    screen_height = 800 # 세로 크기
    xpad = 200
    ypad = 80
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 화면 타이틀 설정
    pygame.display.set_caption("Plane Game") # 게임 이름

    #FPS
    clock = pygame.time.Clock()

    # 이미지 불러오기
    background = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/background.png")
    character = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/fighter.png")
    missile = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/missile.png")
    enemy1 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/ene1.png")
    enemy2 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/ene2.png")
    explosion = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/explosion.png")

    # 플레이어 크기
    character_size = character.get_rect().size # 이미지의 크기를 구해옴 # rect = 사각형
    character_width = character_size[0] # 캐릭터의 가로 크기
    character_height = character_size[1] # 캐릭터의 세로 크기

    # padding
    padding0 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/black.png")
    padding0_xpos = 0
    padding0_ypos = 0
    padding1 = pygame.image.load("C:/Users/k8581/OneDrive/바탕 화면/오락실에서 살아남기/images/black.png")
    padding1_xpos = 0
    padding1_ypos = padding0_ypos + 640 + ypad

    def writeMessage(text): # 게임 메세지를 출력하는 함수
        textfont = pygame.font.SysFont("arial", 80, True, False)
        text = textfont.render(text, True, (255, 0, 0))
        textpos = text.get_rect()
        textpos.center = (screen_width/2, screen_height/2)
        screen.blit(text, textpos)
        pygame.display.update()


    def runGame():
        # 전투기 초기 위치
        x = screen_width * 0.48
        y = screen_height * 0.8
        characterX = 0
        characterY = 0

        missileXY = []  # 내 미사일 좌표 리스트

        # 적1 랜덤 생성
        enemy1Size = enemy1.get_rect().size  # 적 크기
        enemy1_width = enemy1Size[0]
        enemy1_height = enemy1Size[1]

        # 적1 초기 위치 설정
        enemy1X = random.randrange(xpad, screen_width - enemy1_width - xpad)
        enemy1Y = ypad
        enemy1Speed = 2

        # 적2 랜덤 생성
        enemy2Size = enemy2.get_rect().size  # 적 크기
        enemy2_width = enemy2Size[0]
        enemy2_height = enemy2Size[1]

        # 적2 초기 위치 설정
        enemy2X = random.randrange(xpad, screen_width - enemy2_width - xpad)
        enemy2Y = ypad
        enemy2Speed = 4

        # 충돌처리 변수 (미사일에 적이 맞았을 경우 True)
        isShot1 = False
        isShot2 = False

        shotCount = 0   # 점수

        end = False
        endtimer = 60  # 60ms 

        onGame = True
        while onGame:
            for event in pygame.event.get():  # 게임 이벤트 추가
                if event.type in [pygame.QUIT]:  # 파이게임 종료 시
                    pygame.quit()  # 파이게임 종료
                    sys.exit()  # 시스템 종료
                
                if event.type in [pygame.KEYDOWN]:  # 방향키를 눌렀을 때 플레이어 이동 코드
                    if event.key == pygame.K_LEFT:
                        characterX -= 5
                    elif event.key == pygame.K_RIGHT:
                        characterX += 5
                    elif event.key == pygame.K_UP:
                        characterY -= 5
                    elif event.key == pygame.K_DOWN:
                        characterY += 5

                    elif event.key == pygame.K_SPACE:  # 스페이스바 누르면 미사일 발사 
                        missileX = x + character_width / 2
                        missileY = y - character_height
                        missileXY.append([missileX, missileY])
                    
                    elif event.key == pygame.K_0:  # 게임 테스트할 때 쓰인 부분(0을 누르면 바로 클리어됨)
                        screen.blit(key, (((screen_width - key_size[0]) / 2), (screen_height - key_size[1]) / 2)) 
                        Shootkey = True
                        end = True  


                if event.type in [pygame.KEYUP]:  # 키 떼면 멈춤
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        characterX = 0
                    
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_UP:
                        characterY = 0

            screen.fill((0, 0, 0))  # 화면 검정으로 채우기 
            screen.blit(background, (xpad, ypad))  # 게임 배경 띄우기

            x += characterX
            if x < xpad:  # 게임화면 밖으로 빠져나갈 경우
                x = xpad  # 게임화면의 끝 부분으로 위치 변경 
            elif x > screen_width - character_width - xpad:  # 게임화면 밖으로 빠져나갈 경우
                x = screen_width - character_width - xpad    # 게임화면의 끝 부분으로 위치 변경 

            y += characterY
            if y < ypad:  # 게임 밖으로 빠져나갈 경우
                y = ypad
            elif y > screen_height - character_height - ypad:  # 게임화면 밖으로 빠져나갈 경우
                y = screen_height - character_height - ypad
            
            if y < enemy1Y + enemy1_height:  # 적1과 플레이어가 닿았을 경우
                if(enemy1X > x and enemy1X < x + character_width) or (enemy1X + enemy1_width > x and enemy1X + enemy1_width < x + character_width):
                    writeMessage("GAME OVER")  # 게임오버 글자 띄우기 
                    sleep(1)  # 딜레이 
                    onGame = False  # 게임종료
            
            if y < enemy2Y + enemy2_height:  # 적2와 플레이어가 닿았을 경우
                if(enemy2X > x and enemy2X < x + character_width) or (enemy2X + enemy2_width > x and enemy2X + enemy2_width < x + character_width):
                    writeMessage("GAME OVER")  # 게임오버 글자 띄우기 
                    sleep(1)  # 딜레이 
                    onGame = False  # 게임종료


            screen.blit(character, (x, y))  # 플레이어 생성

            if len(missileXY) != 0:
                for i, bxy in enumerate(missileXY):  # 미사일 요소에 대해 반복할
                    bxy[1] -= 10  # 미사일 위로 발사
                    missileXY[i][1] = bxy[1]  # 미사일이 여러 개니까

                    # 미사일이 적1을 맞췄을 경우
                    if bxy[1] < enemy1Y:
                        if bxy[0] > enemy1X and bxy[0] < enemy1X + enemy1_width:
                            missileXY.remove(bxy)  # 미사일 삭제
                            isShot1 = True
                            shotCount += 10  # 점수에 10점 추가 
                            
                    # 미사일이 적2를 맞췄을 경우
                    if bxy[1] < enemy2Y:
                        if bxy[0] > enemy2X and bxy[0] < enemy2X + enemy2_width:
                            missileXY.remove(bxy)  # 미사일 삭제
                            isShot2 = True
                            shotCount += 20  # 점수에 20점 추가 


                    if bxy[1] <= ypad:  # 미사일이 화면 밖을 벗어나면
                        try:
                            missileXY.remove  # 미사일 제거
                        except:
                            pass 

            if len(missileXY) != 0:  # 미사일 리스트의 길이가 0이 아닐 경우 (미사일 리스트에 요소가 있을 경우)
                for bx, by in missileXY:  
                    screen.blit(missile, (bx, by))  # 미사일 생성
            
            enemy1Y += enemy1Speed  # 적1 아래로 움직임
            enemy2Y += enemy2Speed  # 적2 아래로 움직임

            if enemy1Y > screen_height- ypad:  # 적1이 화면 밑으로 떨어진 경우
                # 새로운 적 스폰
                enemy1Size = enemy1.get_rect().size  
                enemy1_width = enemy1Size[0]
                enemy1_height = enemy1Size[1]
                enemy1X = random.randrange(xpad, screen_width - enemy1_width - xpad)
                enemy1Y = ypad
            
            if enemy2Y > screen_height - ypad:  # 적2가 화면 밑으로 떨어진 경우
                # 새로운 적 스폰
                enemy2Size = enemy2.get_rect().size  
                enemy2_width = enemy2Size[0]
                enemy2_height = enemy2Size[1]
                enemy2X = random.randrange(xpad, screen_width - enemy2_width - xpad)
                enemy2Y = ypad

            if isShot1:  # 적1이 미사일에 맞았을 경우 
                screen.blit(explosion, (enemy1X, enemy1Y))  # 적1 자리에 폭발하는 이미지 띄우기 
                # 적 새로 그리기
                enemy1Size = enemy1.get_rect().size  
                enemy1_width = enemy1Size[0]
                enemy1_height = enemy1Size[1]
                enemy1X = random.randrange(xpad, screen_width - enemy1_width - xpad)
                enemy1Y = ypad
                isShot1 = False  
            
            if isShot2:  # 적2이 미사일에 맞았을 경우 
                screen.blit(explosion, (enemy2X, enemy2Y))  # 적2 자리에 폭발하는 이미지 띄우기 
                # 적 새로 그리기
                enemy2Size = enemy2.get_rect().size  
                enemy2_width = enemy2Size[0]
                enemy2_height = enemy2Size[1]
                enemy2X = random.randrange(xpad, screen_width - enemy2_width - xpad)
                enemy2Y = ypad
                isShot2 = False  
                
            # 화면에 띄울 점수 요소 지정 
            game_font = pygame.font.SysFont("arial", 30, True, False)
            score = game_font.render("SCORE: " + str(shotCount), True, (255, 255, 255))
            screen.blit(score, (560 + xpad, 10 + ypad))

            if shotCount >= 300:  # 만약 점수가 300점 이상일 경우
                screen.blit(key, (((screen_width - key_size[0]) / 2), (screen_height - key_size[1]) / 2)) # 화면 중간에 열쇠 띄우기
                Shootkey = True  # 게임 종료 처리를 위해 변수들을 True로 돌림
                end = True       # 게임 종료 처리를 위해 변수들을 True로 돌림

            screen.blit(enemy1, (enemy1X, enemy1Y))  # 화면에 적1 띄우기 
            screen.blit(enemy2, (enemy2X, enemy2Y))  # 화면에 적2 띄우기 

            screen.blit(padding0, (padding0_xpos, padding0_ypos))  # 밑에 부분 검정으로 가려놓기(화면 크기가 바뀌면서 잉여 밑 부분을 가려놓음)
            screen.blit(padding1, (padding1_xpos, padding1_ypos)) 

            if end:   # end가 True일 경우
                endtimer -= 1  # 약간의 딜레이 생성을 위함 
            if endtimer < 0:   # endtimer가 음수가 되었을 때  
                if Shootkey:   # 열쇠를 얻었을 경우
                    door2Screen()  # 다음 화면으로 넘어가기
                else:  # 열쇠를 얻지 못했을 경우
                    door1Screen()  # 이전 화면으로 넘어가기
               
                onGame = False  # 게임 종료 

            pygame.display.update()  # 게임화면을 다시 그림

            clock.tick(60)  # 초당 프레임 수 60으로 해서 진행

    runGame()

def door2Screen(): # 비행기게임 클리어한 후의 화면 
    door2run = True
    while door2run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(door2, (0, 0))
        button("블록깨기", display_width * 0.7, display_height / 2 - 50, 220, 100, black, white, korText, Breakout)
        pygame.display.update()

def Breakout(): # 블록깨기 게임 코드 부분 
    class Block:
        def __init__(self,col,rect,speed = 0):
            self.col = col
            self.rect = rect
            self.speed = speed
            self.dir = random.randint(-45, 45) +270

        def move(self):
            self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
            self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed
        def draw_E(self):
            pygame.draw.ellipse(SURFACE, self.col, self.rect)
        def draw_R(self):
            pygame.draw.rect(SURFACE,self.col,self.rect)

    pygame.display.set_caption('블록깨기 게임')
    pygame.key.set_repeat(10,10)
    SURFACE = pygame.display.set_mode((1000,800))
    FPSCLOCK = pygame.time.Clock()

    def main():
        Breakkey = False
        Game_Start = False
        Score = 0
        BLOCK = []
        PADDLE = Block((200,200,0),Rect(375,700,100,30))
        BALL = Block((200,200,0),Rect(375,650,20,20),10)
        colors = [(255, 0, 0), (255, 150, 0), (255, 228, 0), (11, 201, 4),(0,84,255),(0,0,147)]
        for y,color in enumerate(colors,start=0):
            for x in range(0,8):
                BLOCK.append(Block(color,Rect(x*80 + 150, y *40 + 40, 60, 20)))

        Bigfont = pygame.font.SysFont(None, 80)
        Smallfont = pygame.font.SysFont(None, 50)
        M_Game_Start1 = Bigfont.render("DO YOU WANT GAME_START?", True, (255, 255, 255))
        M_Game_Start2 = Bigfont.render("CLICK THE SPACE_BAR", True, (255, 255, 255))
        M_CLEAR = Bigfont.render("CLEAR!!", True, (255, 255, 255))
        M_FAIL = Bigfont.render("FAILED", True, (255, 255, 255))

        end = False
        endtimer = 60


        while True:
            M_SCORE = Smallfont.render("SCORE : {}".format(Score), True, (255, 255, 255))
            M_SPEED = Smallfont.render("SPEED : {}".format(BALL.speed), True, (255, 255, 255))
            SURFACE.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        PADDLE.rect.centerx -= 10
                    elif event.key == K_RIGHT:
                        PADDLE.rect.centerx += 10
                    elif event.key == K_SPACE:
                        Game_Start = True
                    elif event.key == pygame.K_0:
                        SURFACE.blit(key, (((1000 - key_size[0]) / 2), (800 - key_size[1]) / 2))
                        Breakkey = True
                        end = True

            if Game_Start == False:
                SURFACE.blit(M_Game_Start1, (80,280))
                SURFACE.blit(M_Game_Start2, (180,380))

            else:
                SURFACE.blit(M_SCORE, (250, 500))
                SURFACE.blit(M_SPEED, (550, 500))

                LenBlock = len(BLOCK)
                BLOCK = [x for x in BLOCK if not x.rect.colliderect(BALL.rect)]
                if len(BLOCK) != LenBlock:
                    Score += 10
                    BALL.dir *= -1


                if BALL.rect.centery < 1000:
                    BALL.move()


                if PADDLE.rect.colliderect(BALL.rect):
                    BALL.speed += 0.25
                    BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 100



                if PADDLE.rect.centerx <55 :
                    PADDLE.rect.centerx = 55
                if PADDLE.rect.centerx >945:
                    PADDLE.rect.centerx = 945

                if BALL.rect.centerx < 0 or BALL.rect.centerx > 1000:
                    BALL.dir = 180 - BALL.dir

                elif BALL.rect.centery < 0:
                    BALL.dir = -BALL.dir
                
                if Score >= 400:
                    SURFACE.blit(key, (((1000 - key_size[0]) / 2), (800 - key_size[1]) / 2))
                    Breakkey = True
                    end = True
                if len(BLOCK) == 0:
                    SURFACE.blit(key, (((1000 - key_size[0]) / 2), (800 - key_size[1]) / 2))
                    Breakkey = True
                    end = True
                if BALL.rect.centery >770 and len(BLOCK) > 0:
                    SURFACE.blit(M_FAIL,(380,400))
                    end = True
                BALL.draw_E()
                PADDLE.draw_R()
                for i in BLOCK:
                    i.draw_R()
            
            if end:
                endtimer -= 1
            if endtimer < 0:
                if Breakkey:
                    endScreen()
                else:
                    door2Screen()
                break

            pygame.display.update()
            FPSCLOCK.tick(30)

    if __name__ == '__main__':
        main()

def endScreen():  # 블록깨기 게임 클리어한 후의 화면: 엔딩 화면  
    endrun = True
    timer = 0

    while endrun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        timer += 1
        gameDisplay.fill((255, 255, 255))
        gameDisplay.blit(ending, (0, 0))

        story2_text0 = storyText.render('세 개의 게임을 모두 클리어 해', True, white)
        story2_text1 = storyText.render("드디어 오락실을 탈출했다.", True, white)
        story2_text2 = storyText.render("휴~ 정말 이상한 경험이었어 ", True, white)
        story2_text3 = storyText.render('얼른 집에 가자!', True, white)
        story2_text4 = storyText.render('그 후 주인공은 게임이 얼마나 즐거운지 알게 되어', True, white)
        story2_text5 = storyText.render('여러 게임에 빠지게 되었고', True, white)
        story2_text6 = storyText.render('게임도 직접 만들게 되며', True, white)
        story2_text7 = storyText.render('후에 게임학과를 지망하게 되었다 ', True, white)

        story2_text_xpos = 200
        story2_text0_ypos = display_height * 0.3
        story2_text1_ypos = display_height * 0.4
        story2_text2_ypos = display_height * 0.5
        story2_text3_ypos = display_height * 0.6
        story2_text4_ypos = display_height * 0.3

        if delay > timer:
            gameDisplay.blit(story2_text0, (story2_text_xpos, story2_text0_ypos))
        elif delay * 2 > timer >= delay:
            gameDisplay.blit(story2_text0, (story2_text_xpos, story2_text0_ypos))
            gameDisplay.blit(story2_text1, (story2_text_xpos, story2_text1_ypos))
        elif delay * 3 > timer >= delay * 2:
            gameDisplay.blit(story2_text0, (story2_text_xpos, story2_text0_ypos))
            gameDisplay.blit(story2_text1, (story2_text_xpos, story2_text1_ypos))
            gameDisplay.blit(story2_text2, (story2_text_xpos, story2_text2_ypos))
        elif delay * 4 >timer >= delay * 3:
            gameDisplay.blit(story2_text0, (story2_text_xpos, story2_text0_ypos))
            gameDisplay.blit(story2_text1, (story2_text_xpos, story2_text1_ypos))
            gameDisplay.blit(story2_text2, (story2_text_xpos, story2_text2_ypos))
            gameDisplay.blit(story2_text3, (story2_text_xpos, story2_text3_ypos))
        else:
            gameDisplay.blit(story2_text4, (story2_text_xpos, story2_text0_ypos))
            gameDisplay.blit(story2_text5, (story2_text_xpos, story2_text1_ypos))
            gameDisplay.blit(story2_text6, (story2_text_xpos, story2_text2_ypos))
            gameDisplay.blit(story2_text7, (story2_text_xpos, story2_text3_ypos))
            button("끝", display_width - 250, display_height - 150, 200, 100, black, white, nextText, quitgame)
        
        pygame.display.update()


introScreen()   # 게임시작 함수 불러옴


