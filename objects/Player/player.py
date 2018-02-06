import objects.bases


class Player(objects.bases.BaseUnit):

    def __init__(self, x, y, save_name):
        super().__init__(x, y)

        self.level = None

        self.experience = None

        self.pclass = None

        self.maxHealth = 1
        self.currentHealth = self.maxHealth

        self.image = "res/Player/scr1_rt2.png"

        self.width = 32
        self.height = 32

    def load_pclass(self, save_name):

        pass

    def draw(self, db, IL):
        super().draw(db, IL)

    def step(self, obj_handler, keys, mouse_info):
        super().step(obj_handler, keys, mouse_info)
        # print(self.x, self.y)
        self.handle_keys(keys)

    def handle_keys(self, keys):
        for key in keys:
            # print(key)
            if key == 100:
                self.x += 2.5
            elif key == 97:
                self.x -= 2.5
            if key == 119:
                self.y -= 2.5
            elif key == 115:
                self.y += 2.5
