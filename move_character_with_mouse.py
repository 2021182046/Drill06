from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

def draw_line(p1, p2):
    x1, y1 = p1[0], p1[1] #(-100, -100)
    x2, y2 = p2[0], p2[1] #(300, 150)

    for i in range(0, 100+1, 3):
        t = i/100
        x = (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2

def handle_events():
    global running
    global x, y
    global character_x, character_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            character_x, character_y = x, y

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
character_x = TUK_WIDTH//2
character_y = TUK_HEIGHT//2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    mouse.draw(x, y)
    character.clip_draw(frame * 100, 0, 100, 100, character_x, character_y)
    frame = (frame + 1) % 8
    update_canvas()

    handle_events()

close_canvas()




