import pygame


class AnimatedSprite:

    def __init__(self, width, height, images, image_loader, step_cooldown, animations=None):

        self.height = height
        self.width = width
        self.images = images
        self.image_loader = image_loader
        self.direction = "RIGHT"
        self.direction_step = 0
        self.step_cooldown = 0
        self.step_cooldown_max = step_cooldown
        self.last_direction = self.direction
        if animations is not None:
            self.animations = animations
        else:
            self.animations = ["RIGHT1", "RIGHT2", "RIGHT3", "LEFT1", "LEFT2", "LEFT3"]

    def grab_image(self, animation):
        try:
            y_pos = self.animations.index(animation) * self.height
            x_pos = 0

            animation_surface = self.image_loader.load_image(self.images).subsurface((x_pos, y_pos, self.height,
                                                                                      self.width))
            return animation_surface
        except IndexError:
            print("ANIMATION DOES NOT EXIST")
            return None

    def step(self, direction):

        self.last_direction = self.direction
        self.direction = direction

        if self.direction == self.last_direction:




