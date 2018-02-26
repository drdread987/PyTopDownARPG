import pygame


class AnimatedSprite:

    def __init__(self, width, height, images, image_loader, step_cooldown, order_of_animations, animation_counts):

        self.height = height
        self.width = width
        self.images = images
        self.image_loader = image_loader

        self.animation_step = 0  # stores which image we are in, in a animation loop
        self.step_cooldown_max = step_cooldown  # how often we change image during animation
        self.step_cooldown = self.step_cooldown_max  # stores when it is time to change, if it hits 0 we change
        self.order_of_animations = order_of_animations  # [right, left, jump, fall, ...]
        self.animation = self.order_of_animations[0]  # stores the animation we are using
        self.animation_counts = animation_counts  # [number animation images 1, number of animation images 2, ...]

    def grab_image(self):

        try:
            animation_number = self.order_of_animations.index(self.animation)
            y_pos = 0

            for x in range(animation_number):
                y_pos += self.animation_counts[x] * self.height
            y_pos += self.height * self.animation_step
            x_pos = 0

            animation_surface = self.image_loader.load_image(self.images).subsurface((x_pos, y_pos, self.width,
                                                                                      self.height))
            return animation_surface
        except IndexError:
            print("ANIMATION DOES NOT EXIST")
            return None

    def step(self):
        self.step_cooldown -= 1
        if self.step_cooldown == 0:
            self.step_cooldown = self.step_cooldown_max

            animation_number = self.order_of_animations.index(self.animation)
            self.animation_step += 1
            if self.animation_step >= self.animation_counts[animation_number]:
                self.animation_step = 0

    def new_animation(self, animation):

        if animation in self.order_of_animations and self.animation != animation:
            self.animation = animation
            self.animation_step = 0





