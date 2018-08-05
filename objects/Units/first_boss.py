import objects.bases
import objects.Tools.collision as collide


class FirstBoss(objects.bases.BaseUnit):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.enemy = True
        self.maxHealth = 1000
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

        self.dashing_timer = 300
        self.dashing_timer_max = 300

        self.dash_cooldown = 900
        self.dash_cooldown_max = 900

        self.dash_coords = [0, 0]

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
                        self.dash_coords = list([int(player_x), int(player_y)])
                    if player_x > self.x:
                        self.x += self.hor_speed
                    else:
                        self.x -= self.hor_speed

                    if player_y > self.y:
                        self.y += self.ver_speed
                    else:
                        self.y -= self.ver_speed

            if (self.currentHealth / self.maxHealth < .6) and self.stage == 0:
                self.stage = 1
                self.image = self.images[self.stage][0]
                self.width = self.images[self.stage][1]
                self.height = self.images[self.stage][2]

        elif self.stage == 1:

            if self.currentHealth / self.maxHealth < .25:
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

