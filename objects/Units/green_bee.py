import objects.bases
import objects.Tools.collision as collide


class GreenBee(objects.bases.BaseUnit):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.speed = 1.5
        self.damage = .5

        self.enemy = True

        self.maxHealth = 8
        self.currentHealth = self.maxHealth

        self.direction = "RIGHT"
        self.vert_direction = "DOWN"
        self.image = "res/green_bee.png"
        self.images = {"RIGHT": "res/green_bee.png",
                       "LEFT": "res/green_bee_left.png"}
        self.width = 37
        self.height = 34

        self.dashing = False

        self.dashing_timer = 100
        self.dashing_timer_max = 100

        self.dash_cooldown = 400
        self.dash_cooldown_max = 250

        self.dash_coords = [0, 0]

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

        player_x = obj_handler.Units[0][0].x
        player_y = obj_handler.Units[0][0].y

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

            else:
                self.dash_cooldown -= 1
                if self.dash_cooldown == 0:
                    self.dash_coords = list([int(player_x), int(player_y) - (self.height / 2)])
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

    def take_damage(self, value, dtype):
        super().take_damage(value, dtype)
