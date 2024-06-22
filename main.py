import pygame
from settings import *
import requests

def draw_background():
    screen.fill(BACKGROUND_COLOR)

def bg_sunny():
    screen.fill((100,150,255))
    pygame.draw.circle(screen, (255,255,0), (0,0), SCREEN_WIDTH/4)
    pygame.draw.polygon(screen, (255,255,0), [(200,200), (200,100), (100,200)])
    pygame.draw.polygon(screen, (255,255,0), [(220,-50), (300,25), (200,90)])
    pygame.draw.polygon(screen, (255,255,0), [(-50,220), (25,300), (90,200)])

def bg_cloudy():
    screen.fill((100,150,200))
    pygame.draw.circle(screen, (200,200,200), (150,70), 50)
    pygame.draw.circle(screen, (200,200,200), (80,120), 50)
    pygame.draw.circle(screen, (200,200,200), (220,120), 50)
    pygame.draw.rect(screen, (200,200,200), (80,100,150,70))

def bg_rainy():
    bg_cloudy()
    pygame.draw.circle(screen, (0,0,200), (100,250), 15)
    pygame.draw.polygon()







def get_data():
    BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
    API_KEY=open("api_key.txt", 'r').read()
    CITY="London"

    url = BASE_URL + "appid=" +API_KEY+"&q="+CITY

    response = requests.get(url).json()

    print(response)

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.display.set_caption('Weather app')
font = pygame.font.SysFont('arial', 20)
bg_cloudy()
# get_data()
run  = True

while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
        if (event.type == pygame.KEYDOWN):
            pass
    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()