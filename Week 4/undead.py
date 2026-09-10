class Undead:
    MAX_LEVEL = 100
    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MIN_POWER = 1
    MAX_POWER = 200

    HEALTH_PER_LEVEL = 2
    POWER_PER_LEVEL = 4

    def __init__(self, unit_id, name, min_health, min_power):
        self.__unit_id = unit_id
        self.__name = name
        self.__health = min_health
        self.__power = min_power
        self.__level = 1

    def get_unit_id(self):
        return self.__unit_id

    unit_id = property(get_unit_id)

    def get_name(self):
        return self.__name

    name = property(get_name)

    def get_health(self):
        return self.__health

    health = property(get_health)

    def get_power(self):
        return self.__power

    power = property(get_power)

    def get_level(self):
        return self.__level

    level = property(get_level)

    def level_up(self):
        if self.__level >= self.MAX_LEVEL:
            print('already at max level')
            return False

        self.__level += 1
        self.__health = min(self.__health + self.HEALTH_PER_LEVEL, self.MAX_HEALTH)
        self.__power = min(self.__power + self.POWER_PER_LEVEL, self.MAX_POWER)
        return True

    def __str__(self):
        return (f'Unit id = {self.unit_id}\n'
                f'Name = {self.name}\n'
                f'Health = {self.health}/{self.MAX_HEALTH}\n'
                f'Power = {self.power}/{self.MAX_POWER}\n'
                f'Level = {self.level}\n')

# u_1= Undead(1, " Undead Skeleton Warrior")

# print(u_1)

# u_1.level_up()
# print(u)

# u_1.level_up()
# print(u)
