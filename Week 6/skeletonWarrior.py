from warriorUndead import WarriorUndead


class SkeletonWarrior(WarriorUndead):
    MIN_HEALTH = 15
    MAX_HEALTH = 110
    MIN_POWER = 8
    MAX_POWER = 210

    def __init__(self, unit_id):
        super().__init__(unit_id, 'Skeleton Warrior', self.MIN_HEALTH, self.MIN_POWER)
