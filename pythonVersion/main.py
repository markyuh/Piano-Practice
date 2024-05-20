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
pygame.display.set_caption("Just the piano for now")
active_whites = []
active_blacks = []
white_sounds= []
black_sounds = []

# right_hand = pl.right_hand
# left_hand = pl.left_hand
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
        note_number = random.randint(36,47) #0-87 bc 88 notes in the list
        note = piano_notes[note_number]
        displayImage = pygame.image.load(f'assets/graphics/notes/{note}.png')
        
        return displayImage, note

note_image, note_name = draw_note() #calling drawnote outside of the maiin loop so it doesnt run 60times/sec

running = True
while running:
    timer.tick(fps)
    screen.fill('#171717')
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
    screen.blit(pygame.transform.scale(note_image, (600, 329)), (460, 20))
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
                       print("Correct black")

                    else:
                        print("Correct black")
                        print(black_keys[i].name)
            for i in range(len(white_keys)):
                if white_keys[i].rect.collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0,1000)
                    active_whites.append([i,30])
                    if white_keys[i].name==note_name:
                       print("Correct white")
                    else:
                        print("Correct white")


    pygame.display.flip()#push all visual elements onto the screen in the correct order
pygame.quit()