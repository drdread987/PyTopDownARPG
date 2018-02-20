import objects.bases
import pygame
import objects.Tools.collision


class ClickableFont(objects.bases.BaseDoodad):

    def __init__(self, x, y, width, height, text, font, font_size, called_function, color, hcolor):
        super().__init__(x, y)

        self.width = width
        self.height = height
        self.text = text
        self.called_function = called_function
        pygame.font.init()
        self.highlighted = False
        self.colors = [color, hcolor]
        self.color = color

        self.font = pygame.font.SysFont(font, font_size)
        self.size = self.font.size(self.text)

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

        super().step(obj_handler, keys, mouse_info)
        mouse_x = mouse_info[1][0]
        mouse_y = mouse_info[1][1]
        if objects.Tools.collision.rect_collide(mouse_x, 1, mouse_y, 1, self.x - self.width/2, self.width,
                                                self.y - self.height/2, self.height):
            self.color = self.colors[1]
            self.highlighted = True
        else:
            self.color = self.colors[0]
            self.highlighted = False

        if mouse_info[0][0] and self.highlighted:
            self.called_function()

    def draw(self, object_handler, IL):
        textsurface = self.font.render(self.text, False, self.color)

        object_handler.draw_object(textsurface, (self.x - (self.size[0]/2), self.y - (self.size[1]/2)))


class Quit(ClickableFont):
    def __init__(self, x, y, width, height, text, font, font_size, called_function, color, hcolor):
        super().__init__(x, y, width, height, text, font, font_size, called_function, color, hcolor)

        self.original_image = "res/Quit.png"
        self.highlighted_image = "res/Quit_highlighted.png"
        self.image = self.original_image
        self.height = 100
        self.width = 400

        self.highlighted = False

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)
        mouse_x = mouse_info[1][0]
        mouse_y = mouse_info[1][1]
        if objects.Tools.collision.rect_collide(mouse_x, 1, mouse_y, 1, self.x, self.width, self.y, self.height):
            self.image = self.highlighted_image
            self.highlighted = True
        else:
            self.image = self.original_image
            self.highlighted = False

        if mouse_info[0][0] and self.highlighted:
            obj_handler.quit_game()

    def draw(self, object_handler, IL):
        super().draw(object_handler, IL)


class NewGame(objects.bases.BaseDoodad):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.original_image = "res/New_game.png"
        self.highlighted_image = "res/New_game_highlighted.png"
        self.image = self.original_image
        self.height = 100
        self.width = 400

        self.highlighted = False

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)
        mouse_x = mouse_info[1][0]
        mouse_y = mouse_info[1][1]
        if objects.Tools.collision.rect_collide(mouse_x, 1, mouse_y, 1, self.x, self.width, self.y, self.height):
            self.image = self.highlighted_image
            self.highlighted = True
        else:
            self.image = self.original_image
            self.highlighted = False

        if mouse_info[0][0] and self.highlighted:
            obj_handler.set_next_room("NG")
            obj_handler.end_room()

    def draw(self, object_handler, IL):
        super().draw(object_handler, IL)
