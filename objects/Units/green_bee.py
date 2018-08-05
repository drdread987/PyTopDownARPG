import objects.bases
import objects.Tools.collision as collide


class GreenBee(objects.bases.BaseUnit):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.speed = 1.5
        self.damage = .5

        self.enemy = True

        self.maxHealth = 5
        self.currentHealth = self.maxHealth

        self.direction = "RIGHT"
        self.vert_direction = "DOWN"
        self.image = "res/green_bee.png"
        self.images = {"RIGHT": "res/green_bee.png",
                       "LEFT": "res/green_bee_left.png"}
        self.width = 37
        self.height = 34

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

        player_x = obj_handler.Units[0][0].x
        player_y = obj_handler.Units[0][0].y

        if player_x > self.x:
            self.direction = "RIGHT"
            self.x += self.speed
        else:
            self.direction = "LEFT"
            self.x -= self.speed

        if player_y > self.y:
            self.vert_direction = "DOWN"
            self.y += self.speed
        else:
            self.vert_direction = "UP"
            self.y -= self.speed

        self.image = self.images[self.direction]

        if collide.rect_collide(self.x, self.width, self.y, self.height,
                                obj_handler.Units[0][0].x, obj_handler.Units[0][0].width, obj_handler.Units[0][0].y,
                                obj_handler.Units[0][0].height):
            obj_handler.Units[0][0].take_damage(self.damage, "PHYSICAL")
