
class BaseObject:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.width = 0
        self.height = 0

        self.image = None

    def step(self, dt, obj_handler, keys, mouse_info):

        pass

    def draw(self, db):

        if self.image is not None:
            db.blit(self.image, (self.x, self.y))


class BaseDoodad(BaseObject):

    def __init__(self, x, y):
        super(BaseDoodad, self).__init__(x, y)

        self.destroyable = False
        self.health = 1

    def step(self, dt, obj_handler, keys, mouse_info):
        super(BaseDoodad, self).step(dt, obj_handler, keys, mouse_info)

    def draw(self, db):
        super(BaseDoodad, self).draw(db)


class BaseSpell(BaseObject):

    def __init__(self, x, y):
        super(BaseSpell, self).__init__(x, y)

        self.speed = 0
        self.direction = 0

        self.tags = []

        self.effects = []

        self.cooldown = 0

        self.cost = 0

    def draw(self, db):
        super(BaseSpell, self).draw(db)

    def step(self, dt, obj_handler, keys, mouse_info):
        super(BaseSpell, self).step(dt, obj_handler, keys, mouse_info)


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

    def draw(self, db):
        super(BaseUnit, self).draw(db)

    def step(self, dt, obj_handler, keys, mouse_info):
        super(BaseUnit, self).step(dt, obj_handler, keys, mouse_info)












