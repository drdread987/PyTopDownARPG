import objects.bases
import objects.Tools.collision as collide


class GreenBall(objects.bases.BaseSpell):

    def __init__(self, x, y, dx, dy, damage):
        super().__init__(x, y)
        self.damage = damage
        self.speed = 4

        self.image = "res/green_ball.png"
        self.width = 10
        self.height = 10

        self.x_distance = dx - x
        self.y_distance = dy - y
        self.x_direction = self.x_distance > 0
        self.y_direction = self.y_distance > 0
        self.x_distance = abs(self.x_distance)
        self.y_distance = abs(self.y_distance)
        if self.x_distance > self.y_distance:
            self.y_speed = self.speed * (self.y_distance / self.x_distance)
            self.x_speed = self.speed
        elif self.x_distance < self.y_distance:
            self.x_speed = self.speed * (self.x_distance / self.y_distance)
            self.y_speed = self.speed
        else:
            self.x_speed = self.speed
            self.y_speed = self.speed

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)
        if self.x_direction:
            self.x += self.x_speed
        else:
            self.x -= self.x_speed
        if self.y_direction:
            self.y += self.y_speed
        else:
            self.y -= self.y_speed

        if collide.rect_collide(self.x, self.width, self.y, self.height,
                                obj_handler.Units[0][0].x, obj_handler.Units[0][0].width, obj_handler.Units[0][0].y,
                                obj_handler.Units[0][0].height):
            obj_handler.Units[0][0].take_damage(self.damage, "PHYSICAL")
            obj_handler.rem_spell(spell=self)

        if self.x > obj_handler.width or self.x < 0 or self.y > obj_handler.height or self.y < 0:
            obj_handler.rem_spell(spell=self)

