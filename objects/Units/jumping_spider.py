import objects.bases
import objects.Tools.collision as collide


class JumpingSpider(objects.bases.BaseUnit):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.gravity = True
        self.enemy = True
        self.direction = "RIGHT"
        self.images = {"RIGHT": "res/jumping_spider.png",
                       "LEFT": "res/jumping_spider_left.png"}
        self.width = 30
        self.height = 24

        self.upwardVelocityMax = 15

        self.speed = 2
        self.damage = 2
        self.maxHealth = 6
        self.currentHealth = self.maxHealth

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

        player_x = obj_handler.Units[0][0].x
        player_y = obj_handler.Units[0][0].y

        if player_x > self.x:
            self.direction = "RIGHT"
            self.move(self.speed, obj_handler)
        else:
            self.direction = "LEFT"
            self.move(-self.speed, obj_handler)

        if player_y < self.y and self.onGround:
            self.jumping = True
        elif player_y > self.y:
            self.y += 3
            self.onGround = False

        self.image = self.images[self.direction]

        if collide.rect_collide(self.x, self.width, self.y, self.height,
                                obj_handler.Units[0][0].x, obj_handler.Units[0][0].width, obj_handler.Units[0][0].y,
                                obj_handler.Units[0][0].height):
            obj_handler.Units[0][0].take_damage(self.damage, "PHYSICAL")
