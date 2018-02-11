import objects.bases
from objects.Tools.collision import rect_collide as collide


class Player(objects.bases.BaseUnit):

    def __init__(self, x, y, save_name):
        super().__init__(x, y)

        self.level = None

        self.experience = None

        self.pclass = None
        self.gravity = True
        self.maxHealth = 1
        self.currentHealth = self.maxHealth

        self.image = "res/Player/scr1_rt2.png"

        self.width = 32
        self.height = 32
        self.speed = 2.5

    def load_pclass(self, save_name):

        pass

    def draw(self, db, IL):
        super().draw(db, IL)

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)
        # print(self.x, self.y)
        self.handle_keys(keys, obj_handler)

    def handle_keys(self, keys, obj_handler):
        for key in keys:
            print(key)
            if key == 100:
                good = True
                for obj in obj_handler.Doodads:
                    if obj[0].obstruction:
                        if collide(self.x + self.speed, self.width, self.y-1, self.height,
                                   obj[0].x, obj[0].width, obj[0].y, obj[0].height):
                            good = False
                if good:
                    self.x += self.speed
            elif key == 97:
                good = True
                for obj in obj_handler.Doodads:
                    if obj[0].obstruction:
                        if collide(self.x - self.speed, self.width, self.y-1, self.height,
                                   obj[0].x, obj[0].width, obj[0].y, obj[0].height):
                            good = False
                if good:
                    self.x -= self.speed

            elif key == 32 and self.onGround and not self.jumping:
                self.jumping = True
