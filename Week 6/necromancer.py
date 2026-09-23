from resource import Resource
from summoning_ritual import SummoningRitual
from undead import Undead

class Necromancer():
    MAX_UNDEAD = 10

    def __init__(self, name):
        self.__name = name
        self.__resource = Resource(0,0,0,0,0)
        self.__undead_collection = []
        self.__next_id = 1

    def get_name(self):
        return self.__name

    name = property(get_name)


    def get_resource(self):
        return self.__resource

    resource = property(get_resource)


    def get_controlled_undead(self):
        return self.__undead_collection

    undead_collection = property(get_controlled_undead)


    def collect_resource(self, necrotic_rune, spirit_rune, bone_rune, flesh_rune, ectoplasm):
        self.__resource.collect_resource(necrotic_rune, spirit_rune, bone_rune, flesh_rune, ectoplasm)

    def summon(self, ritual):
        if not isinstance(ritual, SummoningRitual):
            return None
        if len(self.__undead_collection) >= self.MAX_UNDEAD:
            print("at maximum undead capacity")
            return None
        if not ritual.check_ritual(self.__resource):
            return None

        ritual.consume_resources(self.__resource)
        new_undead = ritual.create_undead(self.__next_id)   # check signature
        self.__undead_collection.append(new_undead)
        self.__next_id += 1
        return new_undead

    def dismiss(self, unit_id):
        undead = self._find_undead(unit_id)
        if undead is not None:
            self.__undead_collection.remove(undead)
            return True
        else:
            print('Undead does not exist')
            return False


    def _find_undead(self, unit_id):
        for undead in self.__undead_collection:
            if undead.unit_id == unit_id:
                return undead
        return None

    def level_undead(self, unit_id):
        undead = self._find_undead(unit_id)
        if undead is not None:
            return undead.level_up()
        return False

                


    