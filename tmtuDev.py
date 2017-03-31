# TO ME TO UTILS

# FORMATTING
# One blank line at a time within each section
# Two blank lines seperate unrelated sections (eg: each function)
# No blank line after comments

# IMPORTS
import csv
import pygame


# PYGAME INIT
pygame.init()


# VARIABLES
#done = False
# RGB flatuicolors.com
RED      = (255,  0,  0)
GREEN    = (  0,255,  0)
BLUE     = (  0,  0,255)
WHITE    = (255,255,255)
BLACK    = (  0,  0,  0)

L_TURQ   = (26, 188, 156)
D_TURQ   = (22, 160, 133)

L_GREEN  = ( 46, 204,113)
D_GREEN  = ( 39, 174, 96)

L_BLUE   = (52, 152, 219)
D_BLUE   = (41, 128, 185)

L_PURPLE = (155, 89, 182)
D_PURPLE = (142, 68, 173)

YELLOW   = (241, 196, 15)
O_YELLOW = (243, 156, 18)

ORANGE   = (230, 126, 34)
D_ORANGE = (211, 84,  0)

RED      = (231, 76, 60)
D_RED    = (192, 57, 43)

GREY_1   = (236, 240, 241)
GREY_2   = (189, 195, 199)
GREY_3   = (149, 165, 166)
GREY_4   = (127, 140, 141)

D_B_GREY = (52, 73, 94)
L_B_GREY = (44, 62, 80)

SKIN     = (255,223,196)

# FUNCTIONS
def factorial(i):
    total = i
    while i > 1:
        i -= 1
        total *= i
    return total
    

def setup_pygame(screensize,givencaption):
    size = screensize
    caption = givencaption
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(caption)
    clock = pygame.time.Clock()
    done = False
    font = pygame.font.SysFont("roboto",25,True,False)
    return [done,screen,clock,font]
    

def draw_gnome(x,y,screen,hatcol):
    #BODY
    pygame.draw.polygon(screen, hatcol, [(x+25,y),(x,y+33),(x+50,y+33)])
    pygame.draw.rect(screen, L_BLUE, (x,y+34,50,66))
    pygame.draw.rect(screen, SKIN, (x,y+34,50,25))
    #BEARD
    pygame.draw.rect(screen, WHITE, (x,y+41,10,20))
    pygame.draw.rect(screen, WHITE, (x+40,y+41,10,20))
    pygame.draw.rect(screen, WHITE, (x+5,y+59,40,10))
    pygame.draw.rect(screen,WHITE, (x+15,y+49,20,15),5)
    #EYES
    pygame.draw.rect(screen,BLACK, (x+15,y+39,5,5))
    pygame.draw.rect(screen,BLACK, (x+30,y+39,5,5))
    

def flip():
    pygame.display.flip()


def draw_tick(x,y,width,tickcol):
    pygame.draw.rect(screen, BLACK, (x,y,width,width),5)
    start_x = x+(width/2)
    start_y = y+((width/2)*1.25)
    unit = round(width/25)
    if unit == 0:
        unit = 1
    pygame.draw.polygon(screen, GREEN, ((start_x,start_y),(start_x+ unit*19,start_y+unit*-21),(start_x,start_y+unit*-5),(start_x+unit*-5,start_y+unit*-10)))



# CLASSES
#"Let's make some sliders bitchezzzzzz"~Kai 2k17
class Slider():
    def __init__(self,x,y,height,slider_type,col,radius,screen):
        self.start_coords = [x,y]
        self.x_pos = x
        self.y_pos = y
        self.height = height
        self.type = slider_type
        self.colour = col
        self.radius = radius
        self.screen = screen
        self.held = False
        if self.type == "rectangle":
            self.x_length = self.radius*2
            self.y_length = int(self.x_length*0.4)
        if self.type == "square":
            self.x_length = self.radius*2
            self.y_length = self.x_length
        if self.type == "circle":
            self.x_length = self.radius*2
            self.y_length = self.radius*2
    def is_held(self,boolean):
        if boolean == True:
            self.current_pos = pygame.mouse.get_pos()
            if self.current_pos[0] >= self.x_pos and self.current_pos[0] <= self.x_pos+self.x_length and self.current_pos[1] >= self.y_pos and self.current_pos[1] <= self.y_pos + self.y_length:
                self.held = True
        else:
            self.held = False
    def draw(self, text):
        pygame.draw.line(self.screen, (0, 0, 0), (self.start_coords[0]+self.radius,self.start_coords[1]), (self.start_coords[0]+self.radius,self.start_coords[1]+self.height), 5)
        if self.held:
            self.current_pos = pygame.mouse.get_pos()
            self.y_pos = self.current_pos[1]
            if self.y_pos > self.start_coords[1] + self.height:
                self.y_pos = self.start_coords[1] + self.height
            if self.y_pos < self.start_coords[1]:
                self.y_pos = self.start_coords[1]
        if self.type == "circle":
            pygame.draw.circle(self.screen, self.colour, (self.x_pos+self.radius,self.y_pos), self.radius)
        if self.type == "rectangle" or self.type == "square":
            pygame.draw.rect(self.screen, self.colour, (self.x_pos,self.y_pos-(self.y_length//2),self.x_length,self.y_length))
        if text:
            self.font = pygame.font.SysFont("kaiti",25,True,False)
            self.number = self.font.render(str(self.return_percent_value()),1,(0,0,0))
            self.screen.blit(self.number,(self.start_coords[0],self.start_coords[1]+self.height))
    def return_absolute_value(self):
        return self.y_pos
    def return_percent_value(self):
        self.value = (self.start_coords[1] + self.height) - self.y_pos
        self.value = int((self.value / self.height) * 100)
        return self.value


class Toggle_button():
    def __init__(self, x, y, radius, button_type, screen, start_position, on, off):
        self.x_pos = x
        self.y_pos = y
        self.radius = radius
        self.type = button_type
        self.on = on
        self.off = off
        if start_position == True:
            self.colour = on
            self.boolean = True
        else:
            self.colour = off
            self.boolean = False
        self.screen = screen
        if self.type == "circle":
            self.diameter = self.radius*2
            self.midpoint = [self.x_pos,self.y_pos]
        if self.type == "square":
            self.height = self.radius*2
            self.midpoint = [self.x_pos+self.radius,self.y_pos+self.radius]
        if self.type == "rectangle":
            self.width = self.radius*2
            self.height = self.width*0.4
            self.midpoint = [self.x_pos+self.radius, self.y_pos+int(self.height/2)]
    def draw(self):
        if self.boolean == True:
            self.colour = self.on
        else:
            self.colour = self.off
        if self.type == "circle":
            pygame.draw.circle(self.screen,(0,0,0),(self.x_pos,self.y_pos),self.radius)
            pygame.draw.circle(self.screen,self.colour,(self.x_pos,self.y_pos),self.radius-3)
        if self.type == "square":
            pygame.draw.rect(self.screen,self.colour,(self.x_pos, self.y_pos,self.height,self.height))
            pygame.draw.rect(self.screen,(0,0,0),(self.x_pos, self.y_pos,self.height,self.height),3)
        if self.type == "rectangle":
            pygame.draw.rect(self.screen,self.colour,(self.x_pos,self.y_pos,self.width,self.height))
            pygame.draw.rect(self.screen,(0,0,0),(self.x_pos,self.y_pos,self.width,self.height),3)
    def detect(self):
        self.pos = pygame.mouse.get_pos()
        if self.type == "circle":
            if self.pos[0] >= self.x_pos - self.radius and self.pos[0] <= self.x_pos - self.radius + self.diameter and self.pos[1] >= self.y_pos - self.radius and self.pos[1] <= self.y_pos - self.radius + self.diameter:
                self.boolean = not self.boolean
        if self.type == "square":
            if self.pos[0] >= self.x_pos and self.pos[0] <= self.x_pos + self.height and self.pos[1] >= self.y_pos and self.pos[1] <= self.y_pos + self.height:
                self.boolean = not self.boolean
        if self.type == "rectangle":
            if self.pos[0] >= self.x_pos and self.pos[0] <= self.x_pos + self.width and self.pos[1] >= self.y_pos and self.pos[1] <= self.y_pos + self.height:
                self.boolean = not self.boolean
    def return_bool(self):
        return self.boolean


class Tickbox():
    def __init__(self, x, y, width, bgcol, tickcol, start_set, screen):
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.bgcolour = bgcol
        self.tickcol = tickcol
        self.boolean = start_set
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.bgcolour, (self.x_pos,self.y_pos,self.width,self.width))
        pygame.draw.rect(self.screen, (0,0,0), (self.x_pos,self.y_pos,self.width,self.width),3)
        if self.boolean == True:
            self.start_x = self.x_pos+(self.width/2)
            self.start_y = self.y_pos+((self.width/2)*1.25)
            self.unit = round(self.width/25)
            if self.unit == 0:
                self.unit = 1
            pygame.draw.polygon(self.screen, self.tickcol, ((self.start_x,self.start_y),(self.start_x+ self.unit*19,self.start_y+self.unit*-21),(self.start_x,self.start_y+self.unit*-5),(self.start_x+self.unit*-5,self.start_y+self.unit*-10)))
            pygame.draw.polygon(self.screen, (0,0,0), ((self.start_x,self.start_y),(self.start_x+ self.unit*19,self.start_y+self.unit*-21),(self.start_x,self.start_y+self.unit*-5),(self.start_x+self.unit*-5,self.start_y+self.unit*-10)),2)

    def detect(self):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] >= self.x_pos and self.pos[0] <= self.x_pos + self.width and self.pos[1] >= self.y_pos and self.pos[1] <= self.y_pos + self.width:
            self.boolean = not self.boolean

    def return_bool(self):
        return self.boolean

    def set_width(self,width):
        self.width = width


class Open_CSV():
    def __init__(self, filename, col=0, row=0):
        self.filename = filename
        self.x_pos = col
        self.y_pos = row
        self.file = open(self.filename,"r+")
        self.reader = csv.reader(self.file)
        self.rows = []
        for row in self.reader:
            self.rows.append(row)
    def read(self, row = -1, col = -1):
        if row < 0 or row >= len(self.rows):
            return self.rows
        elif col >= len(self.rows[row]) or col < 0:
            return self.rows[row]
        else:
            self.temp = self.rows[row]
            return self.temp[col]


class Toggle_button2():
    def __init__(self, x, y, radius, screen, off, correctcol, wrongcol):
        self.x_pos = x
        self.y_pos = y
        self.radius = radius
        self.off = off
        self.correctcol = correctcol
        self.wrongcol = wrongcol
        self.colour = self.off
        self.guess = 0
        self.screen = screen
        self.width = self.radius*2
        self.height = self.width*0.4
        self.midpoint = [self.x_pos+self.radius, self.y_pos+int(self.height/2)]
        self.click = False
    def draw(self, click=False):
        self.click = click
        if self.guess == 0:
            self.colour = self.off
        if self.guess == 1:
            self.colour = self.correctcol
        elif self.guess == 2:
            self.colour = self.wrongcol
        pygame.draw.rect(self.screen,self.colour,(self.x_pos,self.y_pos,self.width,self.height))
        pygame.draw.rect(self.screen,(0,0,0),(self.x_pos,self.y_pos,self.width,self.height),3)
    def detect(self):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] >= self.x_pos and self.pos[0] <= self.x_pos + self.width and self.pos[1] >= self.y_pos and self.pos[1] <= self.y_pos + self.height:
            self.click = True
        return(self.click)
        

class Key_detect():
    def __init__(self,screen,font,col=(0,0,0),text=""):
        self.starttext = text
        self.input_string = ""
        self.screen, self.clock, self.font = screen, pygame.time.Clock(),font
        self.col = col
    def draw(self):
        self.screen.fill(GREY_1)
        self.text = self.font.render(self.starttext+self.input_string,True,self.col)
        self.screen.blit(self.text,[0,0])
    def run(self):
        self.done = False
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.KEYDOWN:
                    mod = pygame.key.get_mods()
                    if mod == 1 or mod == 2:
                        if event.key == 97:
                            self.input_string += "A"
                            mod = 0
                        elif event.key == 98:
                            self.input_string += "B"
                            mod = 0
                        elif event.key == 99:
                            self.input_string += "C"
                            mod = 0
                        elif event.key == 100:
                            self.input_string += "D"
                            mod = 0
                        elif event.key == 101:
                            self.input_string += "E"
                            mod = 0
                        elif event.key == 102:
                            self.input_string += "F"
                            mod = 0
                        elif event.key == 103:
                            self.input_string += "G"
                            mod = 0
                        elif event.key == 104:
                            self.input_string += "H"
                            mod = 0
                        elif event.key == 105:
                            self.input_string += "I"
                            mod = 0
                        elif event.key == 106:
                            self.input_string += "J"
                            mod = 0
                        elif event.key == 107:
                            self.input_string += "K"
                            mod = 0
                        elif event.key == 108:
                            self.input_string += "L"
                            mod = 0
                        elif event.key == 109:
                            self.input_string += "M"
                            mod = 0
                        elif event.key == 110:
                            self.input_string += "N"
                            mod = 0
                        elif event.key == 111:
                            self.input_string += "O"
                            mod = 0
                        elif event.key == 112:
                            self.input_string += "P"
                            mod = 0
                        elif event.key == 113:
                            self.input_string += "Q"
                            mod = 0
                        elif event.key == 114:
                            self.input_string += "R"
                            mod = 0
                        elif event.key == 115:
                            self.input_string += "S"
                            mod = 0
                        elif event.key == 116:
                            self.input_string += "T"
                            mod = 0
                        elif event.key == 117:
                            self.input_string += "U"
                            mod = 0
                        elif event.key == 118:
                            self.input_string += "V"
                            mod = 0
                        elif event.key == 119:
                            self.input_string += "W"
                            mod = 0
                        elif event.key == 120:
                            self.input_string += "X"
                            mod = 0
                        elif event.key == 121:
                            self.input_string += "Y"
                            mod = 0
                        elif event.key == 122:
                            self.input_string += "Z"
                    else:
                        if event.key == 48:
                            self.input_string += "0"
                        elif event.key == 49:
                            self.input_string += "1"
                        elif event.key == 50:
                            self.input_string += "2"
                        elif event.key == 51:
                            self.input_string += "3"
                        elif event.key == 52:
                            self.input_string += "4"
                        elif event.key == 53:
                            self.input_string += "5"
                        elif event.key == 54:
                            self.input_string += "6"
                        elif event.key == 55:
                            self.input_string += "7"
                        elif event.key == 56:
                            self.input_string += "8"
                        elif event.key == 57:
                            self.input_string += "9"
                        elif event.key == 46:
                            self.input_string += "."
                        elif event.key == 97:
                            self.input_string += "a"
                        elif event.key == 98:
                            self.input_string += "b"
                        elif event.key == 99:
                            self.input_string += "c"
                        elif event.key == 100:
                            self.input_string += "d"
                        elif event.key == 101:
                            self.input_string += "e"
                        elif event.key == 102:
                            self.input_string += "f"
                        elif event.key == 103:
                            self.input_string += "g"
                        elif event.key == 104:
                            self.input_string += "h"
                        elif event.key == 105:
                            self.input_string += "i"
                        elif event.key == 106:
                            self.input_string += "j"
                        elif event.key == 107:
                            self.input_string += "k"
                        elif event.key == 108:
                            self.input_string += "l"
                        elif event.key == 109:
                            self.input_string += "m"
                        elif event.key == 110:
                            self.input_string += "n"
                        elif event.key == 111:
                            self.input_string += "o"
                        elif event.key == 112:
                            self.input_string += "p"
                        elif event.key == 113:
                            self.input_string += "q"
                        elif event.key == 114:
                            self.input_string += "r"
                        elif event.key == 115:
                            self.input_string += "s"
                        elif event.key == 116:
                            self.input_string += "t"
                        elif event.key == 117:
                            self.input_string += "u"
                        elif event.key == 118:
                            self.input_string += "v"
                        elif event.key == 119:
                            self.input_string += "w"
                        elif event.key == 120:
                            self.input_string += "x"
                        elif event.key == 121:
                            self.input_string += "y"
                        elif event.key == 122:
                            self.input_string += "z"
                    if event.key == 32:
                        self.input_string += " "
                    elif event.key == 8:
                        self.length = len(self.input_string)
                        self.input_string = self.input_string[0:self.length-1]
                    elif event.key == 13:
                        self.done = True
                        return self.input_string

            self.draw()
            flip()
            self.clock.tick(60)