import pygame
import numpy


class IconLocation(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, icon):
        super().__init__()
        self.image = pygame.image.load('img/'+icon+'.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    def set_image(self, image):
        self.image = image


def start():
    global total_coins
    # Generate tree random icon
    rand_icons = numpy.random.choice(icons, 3, p=icon_proba)

    # Draw the random icons on the correct location
    loc_left.set_image(icon_dict[rand_icons[0]])
    loc_middle.set_image(icon_dict[rand_icons[1]])
    loc_right.set_image(icon_dict[rand_icons[2]])

    # Reward if there are thhree identical icons 
    if rand_icons[0] == rand_icons[1] == rand_icons[2]:
        # Get reward from a dict 
        coins = icon_rewerd_dict[rand_icons[0]]
        total_coins += coins



# setup
pygame.init()
width = 700
height = 550
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Slot Machine Game')
logo = pygame.image.load('img/groceries.png')
pygame.display.set_icon(logo)
white = [250, 250, 250]
screen.fill(white)


# Load location icons 
height_location = height / 2 - 13
Location = pygame.sprite.Group()
loc_left = IconLocation(102, height_location, 'icons8-admission-48')
loc_middle = IconLocation(192, height_location, 'icons8-club-suit-48')
loc_right = IconLocation(282, height_location, 'icons8-diamond-suit-48')


# Group location
Location.add(loc_left)
Location.add(loc_middle)
Location.add(loc_right)





# coins players
total_coins = 500



# Stock the icon in list 
icons = ['icons8-admission-48',
        'icons8-club-suit-48',
        'icons8-diamond-suit-48',
        'icons8-heart-suit-48',
        'icons8-spade-suit-48'
        ]
icon_proba = [0.2, 0.25, 0.35, 0.15, 0.05]

# stock on dict every icon 

icon_rewerd_dict = {
    'icons8-admission-48' : 25,
    'icons8-club-suit-48' : 20,
    'icons8-diamond-suit-48' : 15,
    'icons8-heart-suit-48' : 35,
    'icons8-spade-suit-48' : 200
}

icon_dict = {
    'icons8-admission-48' : pygame.image.load('img/icons8-admission-48.png'),
    'icons8-club-suit-48' : pygame.image.load('img/icons8-club-suit-48.png'),
    'icons8-diamond-suit-48' : pygame.image.load('img/icons8-diamond-suit-48.png'),
    'icons8-heart-suit-48' : pygame.image.load('img/icons8-heart-suit-48.png'),
    'icons8-spade-suit-48' : pygame.image.load('img/icons8-spade-suit-48.png')
}


# Main loop 
run = True 

while run:
    screen.fill(white)

    # Draw icon bg image
    Location.draw(screen)


    # Update screan 
    pygame.display.flip()
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            run = False
            quit()
        # chek if key is presed
        if even.type == pygame.KEYDOWN:
            if total_coins >= 15:
                total_coins -= 15
                start()



