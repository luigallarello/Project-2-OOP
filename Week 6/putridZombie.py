from undead import Undead


class PutridZombie(Undead):
    MIN_HEALTH = 25
    MAX_HEALTH = 115
    MIN_POWER = 6
    MAX_POWER = 190

    def __init__(self, unit_id):
        super().__init__(unit_id, 'Putrid Zombie', self.MIN_HEALTH, self.MIN_POWER)
