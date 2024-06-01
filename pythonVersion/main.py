import pygame
import piano_lists as pl
from pygame import mixer
import random

pygame.init()
pygame.mixer.set_num_channels(50)

font = pygame.font.Font('assets/TimesNewRoman.ttf', 48)
medium_font = pygame.font.Font('assets/TimesNewRoman.ttf', 28)
small_font = pygame.font.Font('assets/TimesNewRoman.ttf', 14)
real_small_font = pygame.font.Font('assets/TimesNewRoman.ttf', 9)

fps = 60 #set up a frame rate
timer = pygame.time.Clock() #set up a timer
rect_width = 29
WIDTH = 52 * rect_width #largest width possible for my monitor
HEIGHT =  800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Piano Game")
active_whites = []
active_blacks = []
white_sounds= []
black_sounds = []

piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels

for i in range (len(white_notes)):
    white_sounds.append(mixer.Sound(f'assets/notes/{white_notes[i]}.wav'))

for i in range (len(black_notes)):
    black_sounds.append(mixer.Sound(f'assets/notes/{black_notes[i]}.wav'))

class Key:
    def __init__(self, rect, name):
        self.rect = rect
        self.name = name

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, screen, font):
        pygame.draw.rect(screen, '#C3C3C3', self.rect, 0)
        text_surface = font.render(self.text, True, 'white')
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def splash_screen():
    splash_running = True
    initial_x = -200  # Starting off-screen to the left
    target_x = 650  # Final position for buttons
    title_target_x = 500  # Final position for the title
    clef_target_x = 550  # Final position for the clef question
    exit_x = WIDTH + 200  # Position to move elements off-screen to the right
    animation_speed = 60  # How fast to move elements per frame

    buttons = [
        Button(initial_x, 400, 200, 40, 'Treble'),
        Button(initial_x, 460, 200, 40, 'Bass'),
        Button(initial_x, 520, 200, 40, 'Both')
    ]
    title_text = "Hello! Welcome to the game!"
    clef_text = "Which clef would you like to practice?"
    title_x = initial_x
    clef_x = initial_x

    animating_out = False  

    while splash_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(event.pos):
                        print(f"{button.text} clef selected!")
                        animating_out = True

        screen.fill('#171717')

        if not animating_out:
            title_x = min(title_x + animation_speed, title_target_x)
            clef_x = min(clef_x + animation_speed, clef_target_x)

            title_surface = font.render(title_text, True, 'white')
            screen.blit(title_surface, (title_x, 200))
            clef_surface = medium_font.render(clef_text, True, 'white')
            screen.blit(clef_surface, (clef_x, 300))

            for button in buttons:
                button.rect.x = min(button.rect.x + animation_speed, target_x)
                button.draw(screen, medium_font)
        else:
            # Move all elements to the right until they are off-screen
            if title_x < exit_x:
                title_x += animation_speed  
                clef_x += animation_speed 
                for button in buttons:
                    button.rect.x += animation_speed 
            else:
                pygame.time.delay(60)
                return button.text  # Return after animation is complete

            # Draw elements moving out
            title_surface = font.render(title_text, True, 'white')
            screen.blit(title_surface, (title_x, 200))
            clef_surface = medium_font.render(clef_text, True, 'white')
            screen.blit(clef_surface, (clef_x, 300))
            for button in buttons:
                button.draw(screen, medium_font)

        pygame.display.flip()
        timer.tick(fps)

def draw_piano(whites, blacks):
    white_rects = []
    for i in range (52): #number of white keys on the keyboard
        rect = pygame.draw.rect(screen, 'white', [i*rect_width, HEIGHT - 300, rect_width, 300], 0, 2)
        white_rects.append(Key(rect, white_notes[i]))
        pygame.draw.rect(screen, 'black', [i*rect_width, HEIGHT - 300, rect_width, 300], 2, 2)
        key_label = small_font.render(white_notes[i], True, 'black')
        screen.blit(key_label, (i * rect_width + 7, HEIGHT - 20))
    skip_count = 0 #how many times we've skipped a space
    last_skip = 2 #tells us if last time we skipped was a set of 2 or a set of 3
    skip_track = 2 #checks how many keys drawn since we last skipped
    black_rects = []
    for i in range (36):# all black keys on the board
        rect = pygame.draw.rect(screen, 'black', [17 + (i * rect_width) + (skip_count * rect_width), HEIGHT-300, 25, 200], 0, 2)
        black_rects.append(Key(rect, black_labels[i]))

        for q in range (len(blacks)):
            if blacks[q][0] == i:
                if blacks [q][1] > 0:
                    pygame.draw.rect(screen, 'green', [17 + (i * rect_width) + (skip_count* rect_width), HEIGHT - 300, 24, 200], 2, 2)
                    blacks[q][1] -= 1

        key_label = real_small_font.render(black_labels[i], True, 'white')
        screen.blit(key_label, (21 + (i*rect_width) + (skip_count * rect_width), HEIGHT - 120))
        #black_rects.append(rect)
        skip_track += 1 #adding 1 because we're tracking how many keys we've drawn since the last time we skipped

        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1

    for i in range (len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, 'green', [j * rect_width, HEIGHT-100, rect_width, 100], 2, 2)
            whites[i][1] -= 1

    return white_rects, black_rects, whites, blacks

def draw_note():
        note_number = random.randint(36,67) #0-87 bc 88 notes in the list
        note = piano_notes[note_number]
        displayImage = pygame.image.load(f'assets/graphics/note_png/{note}.png')
        return displayImage, note

note_image, note_name = draw_note() #calling drawnote outside of the maiin loop so it doesnt run 60times/sec

# Define a custom event for updating the note
NOTE_UPDATE_EVENT = pygame.USEREVENT + 1

# Load images for correct and incorrect notes
correct_image = pygame.transform.scale(pygame.image.load('assets/graphics/feedback/CheckMark.png'), (200,200))
incorrect_image = pygame.transform.scale(pygame.image.load('assets/graphics/feedback/x.png'), (200,200))

# Prepare text rendering
correct_text = font.render("Correct!", True, 'green')
incorrect_text = font.render("Wrong", True, 'red')

# Variables to track if correct or incorrect note was clicked
show_correct = False
show_incorrect = False
message_timer = 0

running = True
selected_clef = splash_screen()
while running:
    timer.tick(fps)
    screen.fill('#171717')
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
    screen.blit(pygame.transform.scale(note_image, (600, 329)), (460, 20))

    if show_correct:
            screen.blit(correct_image, (1100, 100))
            screen.blit(correct_text, (1125, 280))
            message_timer -= 1
            if message_timer <= 0:
                show_correct = False
    elif show_incorrect:
        screen.blit(incorrect_image, (200, 100))
        screen.blit(incorrect_text, (235, 280))
        message_timer -= 1
        if message_timer <= 0:
            show_incorrect = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            black_key = False #if a black note is played, we have to make sure we play the black key and not the white keys below it, since black keys are just black rectangles over the white rectangles we draw.
            for i in range(len(black_keys)):#list of rectangles that we get back from drawpiano
                if black_keys[i].rect.collidepoint(event.pos): #if it collides w the mouse coordinate
                    black_sounds[i].play(0,1000) #then we play the sound with the same index as the key index
                    black_key = True
                    active_blacks.append([i, 30])#30 is the timer saying how long we want the rectangle to be active for
                    #plays for half a second because of our 60 fps, 30 scans is half a second
                    if black_keys[i].name==note_name:
                       pygame.time.set_timer(NOTE_UPDATE_EVENT, 2000)
                       show_correct = True
                       message_timer = 119
                    else:
                        show_incorrect = True
                        message_timer = 60
            for i in range(len(white_keys)):
                if white_keys[i].rect.collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0,1000)
                    active_whites.append([i,30])
                    if white_keys[i].name == note_name:
                       pygame.time.set_timer(NOTE_UPDATE_EVENT, 2000)
                       show_correct = True
                       message_timer = 119
                    else:
                        show_incorrect = True
                        message_timer = 60
        if event.type == NOTE_UPDATE_EVENT:
            note_image, note_name = draw_note()  # Update the note image and name
            pygame.time.set_timer(NOTE_UPDATE_EVENT, 0)  # Stop the timer

    pygame.display.flip()#push all visual elements onto the screen in the correct order
pygame.quit()