class Undead:
    MAX_LEVEL = 100
    MAX_LEVEL = 100
    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MIN_POWER = 1
    MAX_POWER = 100

    HEALTH_PER_LEVEL = 2
    POWER_PER_LEVEL = 4
    
    def __init__(self, unit_id, name):
        self.__unit_id = unit_id
        self.__name = name
        self.__health = self.MIN_HEALTH
        self.__power = self.MIN_POWER
        self.__level = 1

    def get_unit_id(self):
        return self.__unit_id

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_power(self):
        return self.__power

    def get_level(self):
        return self.__level