import objects.bases
import objects.Tools.collision as collide


class Slime(objects.bases.BaseUnit):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.speed = 1.5
        self.damage = 1

        self.image = "res/slime.png"
        self.height = 56
        self.width = 64

        self.maxHealth = 10
        self.currentHealth = self.maxHealth

        self.direction = 1
        self.weight = 5
        self.gravity = True

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)
        player_x = obj_handler.Units[0][0].x

        if player_x > self.x:
            self.direction = 1
        elif player_x < self.x:
            self.direction = -1

        self.move(self.speed * self.direction, obj_handler)

        if collide.rect_collide(self.x, self.width, self.y, self.height,
                                obj_handler.Units[0][0].x, obj_handler.Units[0][0].width, obj_handler.Units[0][0].y,
                                obj_handler.Units[0][0].height):
            obj_handler.Units[0][0].take_damage(self.damage, "PHYSICAL")



