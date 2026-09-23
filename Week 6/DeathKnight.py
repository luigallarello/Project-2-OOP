from warriorUndead import WarriorUndead
from cursedUndead import CursedUndead
from undead import Undead


class DeathKnight(WarriorUndead, CursedUndead):
    MIN_HEALTH = 40
    MAX_HEALTH = 180
    MIN_POWER = 25
    MAX_POWER = 300

    HEALTH_PER_LEVEL = 5
    POWER_PER_LEVEL = 8

    def __init__(self, unit_id):
        super().__init__(unit_id, 'Death Knight', self.MIN_HEALTH, self.MIN_POWER)

    def combat_style(self):
        return super().combat_style()

    def compare_combat_styles(self):
        warrior_style = WarriorUndead.combat_style(self)
        cursed_style = CursedUndead.combat_style(self)
        return warrior_style, cursed_style


if __name__ == '__main__':
    dk = DeathKnight(1)
    print(dk)

    print('isinstance(dk, WarriorUndead):', isinstance(dk, WarriorUndead))
    print('isinstance(dk, CursedUndead):', isinstance(dk, CursedUndead))
    print('isinstance(dk, Undead):', isinstance(dk, Undead))

    print()
    print('DeathKnight MRO:')
    for cls in DeathKnight.__mro__:
        print(' ', cls.__name__)

    print()
    print('combat_style() via super():', dk.combat_style())
    print('-> matches WarriorUndead, the first parent after DeathKnight in the MRO.')

    print()
    warrior_style, cursed_style = dk.compare_combat_styles()
    print('WarriorUndead.combat_style(self):', warrior_style)
    print('CursedUndead.combat_style(self): ', cursed_style)
