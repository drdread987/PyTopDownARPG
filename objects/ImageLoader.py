import pygame


class IL:

    def __init__(self):

        self.images = {}  # stored {file_location: image_data, ...}

    def load_image(self, image_location):

        if image_location in self.images:
            return self.images[image_location]
        else:
            print(image_location)
            self.images[image_location] = pygame.image.load(image_location).convert()
            return self.images[image_location]
