import pygame
import piano_lists as pl
from pygame import mixer

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
HEIGHT =  400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Just the piano for now")
active_whites = []
active_blacks = []


def draw_piano(whites, blacks):
    white_rects = []
    for i in range (52): #number of white keys on the keyboard
        rect = pygame.draw.rect(screen, 'white', [i*rect_width, HEIGHT - 300, rect_width, 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i*rect_width, HEIGHT - 300, rect_width, 300], 2, 2)
        key_label = small_font.render(pl.white_notes[i], True, 'black')
        screen.blit(key_label, (i * rect_width + 3, HEIGHT - 20))
    skip_count = 0 #how many times we've skipped a space
    last_skip = 2 #tells us if last time we skipped was a set of 2 or a set of 3
    skip_track = 2 #checks how many keys drawn since we last skipped
    black_rects = []
    for i in range (36):# all black keys on the board
        rect = pygame.draw.rect(screen, 'black', [17 + (i * rect_width) + (skip_count * rect_width), HEIGHT-300, 25, 200], 0, 2)
        for q in range (len(blacks)):
            if blacks[q][0] == i:
                if blacks [q][1] > 0:
                    pygame.draw.rect(screen, 'green', [17 + (i * rect_width) + (skip_count* rect_width), HEIGHT - 300, 24, 200], 2, 2)
                    blacks[q][1] -= 1

        key_label = real_small_font.render(pl.black_labels[i], True, 'white')
        screen.blit(key_label, (21 + (i*rect_width) + (skip_count * rect_width), HEIGHT - 120))
        black_rects.append(rect)
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


running = True
while running:
    timer.tick(fps)
    screen.fill('gray')
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()#push all visual elements onto the screen in the correct order
pygame.quit()