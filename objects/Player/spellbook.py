

class Spellbook:

    def __init__(self):

        self.known_spells = {}  # stored {spellId: [spell, cooldown], ...}

    def learn_spell(self, spellId, pclass, player):
        requested_spell = pclass.get_spell(spellId)
        if player.level >= requested_spell.required_level():

            if spellId not in self.known_spells:
                self.known_spells[spellId] = [requested_spell, 0]

                


