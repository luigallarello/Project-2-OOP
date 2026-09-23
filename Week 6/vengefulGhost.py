from cursedUndead import CursedUndead


class VengefulGhost(CursedUndead):
    MIN_HEALTH = 15
    MAX_HEALTH = 110
    MIN_POWER = 12
    MAX_POWER = 230

    def __init__(self, unit_id):
        super().__init__(unit_id, 'Vengeful Ghost', self.MIN_HEALTH, self.MIN_POWER)
