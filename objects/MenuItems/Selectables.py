import objects.bases
import pygame
import objects.Tools.collision


class Quit(objects.bases.BaseDoodad):
    def __init__(self, x, y):
        super().__init__(x, y)

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

    def draw(self, db, IL):
        super().draw(db, IL)


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

    def draw(self, db, IL):
        super().draw(db, IL)
