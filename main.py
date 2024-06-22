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
    pygame.draw.circle(screen, (200,200,200), (140,70), 50)
    pygame.draw.circle(screen, (200,200,200), (70,120), 50)
    pygame.draw.circle(screen, (200,200,200), (210,120), 50)
    pygame.draw.rect(screen, (200,200,200), (70,100,150,70))

def bg_rainy():
    bg_cloudy()
    pygame.draw.polygon(screen, (0,0,200), [(85,246), (114,246), (100,210)])
    pygame.draw.circle(screen, (0,0,200), (100,250), 15)

    pygame.draw.polygon(screen, (0,0,200), [(185,246), (214,246), (200,210)])
    pygame.draw.circle(screen, (0,0,200), (200,250), 15)

    pygame.draw.polygon(screen, (0,0,200), [(135,296), (164,296), (150,260)])
    pygame.draw.circle(screen, (0,0,200), (150,300), 15)

def bg_snow():
    screen.fill((150,180,200))
    pygame.draw.circle(screen, (230,230,230), (140,70), 50)
    pygame.draw.circle(screen, (230,230,230), (70,120), 50)
    pygame.draw.circle(screen, (230,230,230), (210,120), 50)
    pygame.draw.rect(screen, (230,230,230), (70,100,150,70))

    pygame.draw.circle(screen, (230,230,230), (100,200), 10)
    pygame.draw.circle(screen, (230,230,230), (150,200), 10)
    pygame.draw.circle(screen, (230,230,230), (200,200), 10)
    pygame.draw.circle(screen, (230,230,230), (125,225), 10)
    pygame.draw.circle(screen, (230,230,230), (175,225), 10)
    pygame.draw.circle(screen, (230,230,230), (100,250), 10)
    pygame.draw.circle(screen, (230,230,230), (150,250), 10)
    pygame.draw.circle(screen, (230,230,230), (200,250), 10)
    pygame.draw.circle(screen, (230,230,230), (125,275), 10)
    pygame.draw.circle(screen, (230,230,230), (175,275), 10)

def data_square():
    pygame.draw.rect(screen, (255,255,255),(280,100,470,450))
    pygame.draw.rect(screen, (0,0,80),(280,100,470,450),3)

def get_data():
    BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
    API_KEY=open("api_key.txt", 'r').read()
    CITY="Verona"

    url = BASE_URL + "appid=" +API_KEY+"&q="+CITY

    response = requests.get(url).json()

    return(response)

def f_to_c(f):
    return(int((f - 32) / 5/9))

def display_info():
    w_condition=data['weather'][0]['main']
    set_background(w_condition)
    city=data['name']
    font = pygame.font.SysFont('arial', 40)
    text=font.render(city, True, (0,0,0))
    screen.blit(text, (280,50))

    
    text=font.render("Weather: ", True, (0,0,0))
    screen.blit(text, (290,110))
    text=font.render(w_condition, True, (0,0,0))
    screen.blit(text, (460,110))

    temp=f_to_c(float(data['main']['temp']))
    pygame.draw.rect(screen, (255,200,240),(290,200,85,70))
    pygame.draw.rect(screen, (0,0,80),(290,200,85,70),3)
    font = pygame.font.SysFont('arial', 30)
    text=font.render("Temperature: ", True, (0,0,0))
    screen.blit(text, (290,160))
    font = pygame.font.SysFont('arial', 50)
    text=font.render(str(temp)+'°', True, (0,0,0))
    screen.blit(text, (295,210))

    temp_max=f_to_c(float(data['main']['temp_max']))
    pygame.draw.rect(screen, (200,200,255),(440,200,85,70))
    pygame.draw.rect(screen, (0,0,80),(440,200,85,70),3)
    text=font.render(str(temp_max)+'°', True, (0,0,0))
    screen.blit(text, (445,210))
    pygame.draw.rect(screen, (200,200,255),(540,230,20,40))
    pygame.draw.rect(screen, (0,0,0),(540,230,20,40),3)
    pygame.draw.polygon(screen, (200,200,255),[(550,200),(530,230),(570,230)])
    pygame.draw.polygon(screen, (0,0,0),[(550,200),(530,230),(570,230)], 3)
    pygame.draw.rect(screen, (200,200,255),(543,220,14,20))

    temp_min=f_to_c(float(data['main']['temp_min']))
    pygame.draw.rect(screen, (255,230,200),(600,200,85,70))
    pygame.draw.rect(screen, (0,0,80),(600,200,85,70),3)
    text=font.render(str(temp_min)+'°', True, (0,0,0))
    screen.blit(text, (605,210))
    pygame.draw.rect(screen, (255,230,200),(700,200,20,40))
    pygame.draw.rect(screen, (0,0,0),(700,200,20,40),3)
    pygame.draw.polygon(screen, (255,230,200),[(710,270),(690,240),(730,240)])
    pygame.draw.polygon(screen, (0,0,0),[(710,270),(690,240),(730,240)], 3)
    pygame.draw.rect(screen, (255,230,200),(703,230,14,20))

def set_background(w):
    if(w=="Clouds"):
        bg_cloudy()
    elif(w=="Rain"):
        bg_rainy()
    elif(w=='Snow'):
        bg_snow()
    elif(w=='Clear'):
        bg_sunny()
    data_square()






pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.display.set_caption('Weather app')
font = pygame.font.SysFont('arial', 20)
bg_sunny()
data_square()
data=get_data()
print(data)
display_info()
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