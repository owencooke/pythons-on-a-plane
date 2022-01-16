import pygame
import game_database

colour_invactive = pygame.Color('lightskyblue3')
colour_active = pygame.Color('dodgerblue2')
my_font = pygame.font.Font(None, 32)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.submitted = False
        self.rect = pygame.Rect(x, y, w, h)
        self.color = colour_invactive
        self.text = text
        self.txt_surface = my_font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event, score):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = colour_active if self.active else colour_invactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.text != '':
                        print(self.text)
                        print(score)
                        game_database.addScore(self.text, score)
                        
                        self.text = ''
                        self.submitted = True
                        
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = my_font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)