import objects.bases
import objects.Tools.collision as collide
import objects.Units.unit_spells.flying_sword as flying_sword
import objects.Units.unit_spells.lightning as lightning
from random import randint


class FirstBoss(objects.bases.BaseUnit):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.enemy = True
        self.maxHealth = 1500
        self.currentHealth = self.maxHealth

        self.damage = 2
        self.speed = 1.5

        self.hor_speed = self.speed * 1
        self.ver_speed = self.speed * .5

        self.stage = 0
        self.images = {0: ["res/first_boss0.png", 79, 94],
                       1: ["res/first_boss1.png", 122, 103],
                       2: ["res/first_boss2.png", 86, 110]}
        self.image = self.images[self.stage][0]
        self.width = self.images[self.stage][1]
        self.height = self.images[self.stage][2]

        self.dashing = False

        self.dashing_timer = 100
        self.dashing_timer_max = 100

        self.dash_cooldown = 400
        self.dash_cooldown_max = 250

        self.dash_coords = [0, 0]

        self.sword_cooldown = 200
        self.sword_max_cooldown = 200

        self.lightning_cooldown = 100
        self.lightning_max_cooldown = 100

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

        player_x = obj_handler.Units[0][0].x
        player_y = obj_handler.Units[0][0].y

        if self.stage == 0 or self.stage == 2:

            if self.dashing:
                if collide.rect_collide(self.x, self.width, self.y, self.height,
                                        self.dash_coords[0], self.width, self.dash_coords[1], self.height):
                    self.x = self.dash_coords[0]
                    self.y = self.dash_coords[1]
                    self.dashing_timer = self.dashing_timer_max
                    self.dashing = False
                else:
                    if self.x < self.dash_coords[0]:
                        self.x += self.speed * 10
                    else:
                        self.x -= self.speed * 10
                    if self.y < self.dash_coords[1]:
                        self.y += self.speed * 10
                    else:
                        self.y -= self.speed * 10
            else:
                if self.dash_cooldown == 0:
                    if self.dashing_timer == 0:
                        self.dashing = True
                        self.dash_cooldown = self.dash_cooldown_max
                    else:
                        self.dashing_timer -= 1
                        self.y -= 1
                else:
                    self.dash_cooldown -= 1
                    if self.dash_cooldown == 0:
                        self.dash_coords = list([int(player_x), int(player_y) - (self.height/2)])
                    if player_x > self.x:
                        self.x += self.hor_speed
                    else:
                        self.x -= self.hor_speed

                    if player_y - (self.height/2) > self.y:
                        self.y += self.ver_speed
                    else:
                        self.y -= self.ver_speed

            if (self.currentHealth / self.maxHealth < .82) and self.stage == 0:
                self.stage = 1
                self.image = self.images[self.stage][0]
                self.width = self.images[self.stage][1]
                self.height = self.images[self.stage][2]

        if self.stage == 1 or self.stage == 2:
            if self.sword_cooldown == 0:
                obj_handler.add_spell(flying_sword.FlyingSword(obj_handler.width, player_y, (self.damage*2)))
                self.sword_cooldown = self.sword_max_cooldown
            else:
                self.sword_cooldown -= 1

            if self.lightning_cooldown == 0:
                obj_handler.add_spell(lightning.Lightning(player_x, 0, (self.damage*4)))
                self.lightning_cooldown = self.lightning_max_cooldown
            else:
                self.lightning_cooldown -= 1

            if self.currentHealth / self.maxHealth < .35 and self.stage == 1:
                self.stage = 2
                self.image = self.images[self.stage][0]
                self.width = self.images[self.stage][1]
                self.height = self.images[self.stage][2]
                self.dashing = False
                self.dash_cooldown = self.dash_cooldown_max
                self.dashing_timer = self.dashing_timer_max

        if collide.rect_collide(self.x, self.width, self.y, self.height,
                                obj_handler.Units[0][0].x, obj_handler.Units[0][0].width, obj_handler.Units[0][0].y,
                                obj_handler.Units[0][0].height):
            obj_handler.Units[0][0].take_damage(self.damage, "PHYSICAL")

