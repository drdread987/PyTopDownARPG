

class BaseClass:

    def __init__(self):

        self.ability_one = None
        self.ability_two = None
        self.ability_three = None
        self.ability_four = None
        self.ability_five = None
        self.ability_expertise = None

        self.resource = 0
        self.resource_max = 0
        self.resource_name = None

    def step(self, obj_list):

        pass

    def get_ability_names(self):

        return [self.ability_one.name, self.ability_two.name, self.ability_three.name, self.ability_four.name,
                self.ability_five.name, self.ability_expertise.name]

    def get_ability_cooldowns(self):

        return [self.ability_one.cooldown, self.ability_two.cooldown, self.ability_three.cooldown,
                self.ability_four.cooldown, self.ability_five.cooldown, self.ability_expertise.cooldown]

    def get_ability_description(self, value, stats):

        if value == 1:
            return self.ability_one.get_description(stats)
        elif value == 2:
            return self.ability_two.get_description(stats)
        elif value == 3:
            return self.ability_three.get_description(stats)
        elif value == 4:
            return self.ability_four.get_description(stats)
        elif value == 5:
            return self.ability_five.get_description(stats)
        elif value == 6:
            return self.ability_expertise.get_description(stats)

    def cast_ability(self, value, stats, obj_handler, x, y):

        if value == 1:
            return self.ability_one.cast(stats, obj_handler, x, y)
        elif value == 2:
            return self.ability_two.cast(stats, obj_handler, x, y)
        elif value == 3:
            return self.ability_three.cast(stats, obj_handler, x, y)
        elif value == 4:
            return self.ability_four.cast(stats, obj_handler, x, y)
        elif value == 5:
            return self.ability_five.cast(stats, obj_handler, x, y)
        elif value == 6:
            return self.ability_expertise.cast(stats, obj_handler, x, y)


