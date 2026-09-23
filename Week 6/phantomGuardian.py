from warriorUndead import WarriorUndead


class PhantomGuardian(WarriorUndead):
    MIN_HEALTH = 20
    MAX_HEALTH = 120
    MIN_POWER = 10
    MAX_POWER = 220

    def __init__(self, unit_id):
        super().__init__(unit_id, 'Phantom Guardian', self.MIN_HEALTH, self.MIN_POWER)
