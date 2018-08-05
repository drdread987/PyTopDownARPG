import objects.bases
import objects.Tools.collision as collide
from random import randint
import objects.Units.unit_spells.green_ball as gb


class Slime(objects.bases.BaseUnit):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.speed = 1.5
        self.damage = 1

        self.enemy = True

        self.image = "res/slime.png"
        self.height = 56
        self.width = 64

        self.maxHealth = 12
        self.currentHealth = self.maxHealth

        self.direction = 1
        self.weight = 5
        self.gravity = True

        self.ball_cooldown_max = 350
        self.ball_cooldown = randint(0, self.ball_cooldown_max)

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)
        player_x = obj_handler.Units[0][0].x
        player_y = obj_handler.Units[0][0].y

        self.ball_cooldown -= 1
        if self.ball_cooldown <= 0:
            obj_handler.add_spell(gb.GreenBall(self.x, self.y, player_x, player_y, self.damage*5))
            self.ball_cooldown = self.ball_cooldown_max

        if player_x > self.x:
            self.direction = 1
        elif player_x < self.x:
            self.direction = -1

        self.move(self.speed * self.direction, obj_handler)

        if collide.rect_collide(self.x, self.width, self.y, self.height,
                                obj_handler.Units[0][0].x, obj_handler.Units[0][0].width, obj_handler.Units[0][0].y,
                                obj_handler.Units[0][0].height):
            obj_handler.Units[0][0].take_damage(self.damage, "PHYSICAL")



