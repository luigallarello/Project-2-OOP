from undead import Undead

class CursedUndead(Undead):
    def __init__(self, unit_id, name, min_health, min_power):
        super().__init__(unit_id, name, min_health, min_power)

    def command(self):
        base = super().command()
        return f'{base} The cursed undead has risen.'