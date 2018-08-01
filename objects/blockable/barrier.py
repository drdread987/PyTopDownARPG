import objects.bases


class InvisibleBarrier(objects.bases.BaseDoodad):

    def __init__(self, x, y, width, height):
        super().__init__(x, y)

        self.weight = 50000

        self.obstruction = True

        self.width = width
        self.height = height

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

    def draw(self, db, IL):
        super().draw(db, IL)


class BlackBarrier(objects.bases.BaseDoodad):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.weight = 50000

        self.obstruction = True

        self.width = 32
        self.height = 32

        self.passable = True

        self.image = "res/black_barrier.jpeg"

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

    def draw(self, db, IL):
        super().draw(db, IL)


class GrassBlock(objects.bases.BaseDoodad):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.weight = 50000

        self.obstruction = True

        self.width = 32
        self.height = 32

        self.passable = True

        self.image = "res/grass_single_tile.png"

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

    def draw(self, db, IL):
        super().draw(db, IL)


class GrassSideBlock(objects.bases.BaseDoodad):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.weight = 50000

        self.obstruction = True

        self.width = 32
        self.height = 1600

        self.passable = False

        self.image = "res/grass_long_side.png"

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

    def draw(self, db, IL):
        super().draw(db, IL)


class GrassBottomBlock(objects.bases.BaseDoodad):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.weight = 50000

        self.obstruction = True

        self.width = 2560
        self.height = 32

        self.passable = False

        self.image = "res/grass_long_bottom.png"

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

    def draw(self, db, IL):
        super().draw(db, IL)


class GrassBottomShortBlock(objects.bases.BaseDoodad):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.weight = 50000

        self.obstruction = True

        self.width = 256
        self.height = 32

        self.passable = True

        self.image = "res/grass_short_bottom.png"

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)

    def draw(self, db, IL):
        super().draw(db, IL)
