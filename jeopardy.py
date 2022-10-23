import sys, pygame,os
pygame.init()

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

contestants = input("Enter player names with a space in between:").split()
numplayers = len(contestants)
scores = []
for i in range(numplayers):
    scores.append(0)

size = width, height = 300*numplayers, 600
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0
user_text = ''
screen = pygame.display.set_mode(size,pygame.RESIZABLE)

input_rect = pygame.Rect(100, 535, 100, 40)  

scoreval = [200,400,600,800,1000,1200,1600,2000]
font = pygame.font.Font(None, 32)
def drawText(text,x,y):
    font = pygame.font.Font(None, 32)
    text = font.render(str(text),True,black)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
while 1:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
            for xv in range(numplayers):
                
                x,y = pygame.mouse.get_pos()
                xpos = xv*300
                yvals = [138,188,238,288,338,388,438,488,538]
                for i in range(9):
                    ypos = yvals[i]
                    if xpos+230<x<xpos+250 and ypos<y<ypos+20:
                        if i<8:scores[xv] += scoreval[i]
                        else: 
                            try:
                                scores[xv] += int(user_text)
                            except: print('not a number idiot')
                    elif xpos+260<x<xpos+280 and ypos<y<ypos+20:
                        if i<8:scores[xv] -= scoreval[i]
                        else:
                            try:
                                scores[xv] -= int(user_text)
                            except: print('not a number idiot')
        if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
                  
                    
    for i in range(numplayers):
        yvals = [150,200,250,300,350,400,450,500,550]
        drawText(contestants[i],150+(300*i),50)
        drawText(f'Score: {scores[i]}',150+(300*i),100)
        for p in range(8):
            drawText(scoreval[p],150+(300*i),yvals[p])
        #drawText("Custom",150+(300*i),550)
        
        
        for y in yvals:
            pygame.draw.rect(screen, green, (230+i*300,y-12,20,20))
            pygame.draw.rect(screen, red, (260+i*300,y-12,20,20))
    pygame.draw.rect(screen, black, input_rect,3)
  
    text_surface = font.render(user_text, True, black)
      
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)       
    
    pygame.display.flip()
