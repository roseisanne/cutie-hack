import pygame
import pygame_gui
pygame.init()


pygame.display.set_caption('Quick Start')

resolution = (1280, 720)
window_surface = pygame.display.set_mode(resolution)


background = pygame.Surface(resolution)
background.fill(pygame.Color("#424242"))

manager = pygame_gui.ui_manager.UIManager(resolution, 'theme.json')

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=manager)

button_size = ((resolution[0]-0.25)/4, resolution[1]*0.2)
button_height = resolution[1]*0.775
spell_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((resolution[0]*0.05, button_height) , button_size),
                                            text='Spell 1',
                                            object_id='spell_button',
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True


while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                  print('Hello World!')
        manager.process_events(event)
    
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)


    pygame.display.update()
