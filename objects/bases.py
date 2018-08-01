import objects.Tools.collision as collide


class BaseObject:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.alignment = "NEUTRAL"
        self.width = 0
        self.height = 0

        self.image = None

        self.player = False

        self.gravity = False
        self.onGround = False
        self.jumping = False
        self.downwardVelocity = 0
        self.upwardVelocity = 0
        self.upwardVelocityStep = .5
        self.upwardVelocityMax = 10
        self.weight = 3

        self.animated = False
        self.animation = None

        self.alive = True

    def step(self, obj_handler, keys, mouse_info):
        if self.animation:
            self.image.step()
        if self.gravity and not self.jumping:
            self.onGround = False
            for obj in obj_handler.Doodads:
                if obj[0].obstruction:
                    if collide.rect_collide(self.x, self.width, self.y + self.height + self.downwardVelocity,
                                            1, obj[0].x, obj[0].width, obj[0].y,
                                            self.downwardVelocity):
                        self.y = obj[0].y - self.height
                        self.onGround = True
                        self.downwardVelocity = 0

            if not self.onGround:

                if self.downwardVelocity < self.weight * 2:
                    self.downwardVelocity += self.weight / 6
                self.y += self.downwardVelocity
        if self.jumping:
            self.downwardVelocity = 0
            self.onGround = False
            if self.upwardVelocity > 0:
                self.y -= self.upwardVelocity
                self.upwardVelocity -= self.upwardVelocityStep
            else:
                self.jumping = False
                self.upwardVelocity = self.upwardVelocityMax

    def draw(self, object_handler, IL):

        if self.animated:
            object_handler.draw_object(self.image.grab_image(), (self.x, self.y))
        elif self.image is not None:
            object_handler.draw_object(IL.load_image(self.image), (self.x, self.y))

    def move(self, speed, obj_handler):
        if speed > 0:

            good = True
            for obj in obj_handler.Doodads:
                if obj[0].obstruction:
                    if collide.rect_collide(self.x + self.width + speed, 1, self.y - 1, self.height,
                                            obj[0].x, obj[0].width, obj[0].y, obj[0].height):
                        if obj[0].passable:
                            good = True
                        else:
                            self.x = obj[0].x - self.width - 1
                            good = False

            if good:
                self.x += speed

            return good
        elif speed < 0:

            good = True
            for obj in obj_handler.Doodads:
                if obj[0].obstruction:
                    if collide.rect_collide(self.x + speed, 1, self.y - 1, self.height,
                                            obj[0].x, obj[0].width, obj[0].y, obj[0].height):
                        if obj[0].passable:
                            good = True
                        else:
                            self.x = obj[0].x + obj[0].width + 1
                            good = False

            if good:
                self.x += speed
            return good


class BaseDoodad(BaseObject):

    def __init__(self, x, y):
        super(BaseDoodad, self).__init__(x, y)

        self.destroyable = False
        self.obstruction = True
        self.health = 1
        self.passable = True

    def step(self, obj_handler, keys, mouse_info):
        super(BaseDoodad, self).step(obj_handler, keys, mouse_info)

    def draw(self, object_handler, IL):
        super(BaseDoodad, self).draw(object_handler, IL)


class BaseSpell(BaseObject):

    def __init__(self, x, y):
        super(BaseSpell, self).__init__(x, y)

        self.speed = 0
        self.direction = 0

        self.tags = []

        self.effects = []

        self.cooldown = 0

        self.cost = 0

    def draw(self,  object_handler, IL):
        super(BaseSpell, self).draw(object_handler, IL)

    def step(self, obj_handler, keys, mouse_info):
        super(BaseSpell, self).step(obj_handler, keys, mouse_info)


class BaseUnit(BaseObject):

    def __init__(self, x, y):
        super(BaseUnit, self).__init__(x, y)

        self.speed = 0
        self.direction = 0
        
        self.maxHealth = 0
        self.currentHealth = self.maxHealth

        self.player = False

        self.enemy = True

        self.tags = []

        self.damage = 0

        self.spells = {}  # stored spell:cd

    def draw(self,  object_handler, IL):
        super(BaseUnit, self).draw(object_handler, IL)

    def step(self, obj_handler, keys, mouse_info):
        super(BaseUnit, self).step(obj_handler, keys, mouse_info)

    def take_damage(self, value, dtype):

        self.currentHealth -= value

        if self.currentHealth <= 0:
            self.alive = False














