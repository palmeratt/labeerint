from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
background = transform.scale(image.load("background.png"), (700, 500))

sprite1 = transform.scale(
    image.load('sprite1.png'),
    (100, 100)
)

sprite2 = transform.scale(
    image.load('sprite2.png'),
    (100, 100)
)

window.blit(sprite1, (250, 300))
window.blit(sprite2, (320, 300))

game = True
while game:
    window.blit(background,(0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()

    
    while game:
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and x1 >5:
            x1 -= speed
        if keys_pressed[K_RIGHT] and x1 < 595:
            x1 += speed
        if keys_pressed[K_UP] and x1 >5:
            x1 -= speed
        if keys_pressed[K_DOWN] and x1 < 395:
            x1 += speed

clock = time.Clock()
FPS = 60
clock.tick(FPS)