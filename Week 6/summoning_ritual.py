from resource import Resource

class SummoningRitual:
    def __init__(self, ritual_name, summon_class, starting_health, starting_power,
                 necrotic_cost=0, spirit_cost=0, bone_cost=0, flesh_cost=0, ectoplasm_cost=0):
        self.__ritual_name = ritual_name
        self.__summon_class = summon_class
        self.__starting_health = starting_health
        self.__starting_power = starting_power
        self.__necrotic_cost = necrotic_cost
        self.__spirit_cost = spirit_cost
        self.__bone_cost = bone_cost
        self.__flesh_cost = flesh_cost
        self.__ectoplasm_cost = ectoplasm_cost

        if ectoplasm_cost > 0:
            self.__ectoplasm_cost = ectoplasm_cost
        else:
            print("ritual must use ectoplasm")
            self.__ectoplasm_cost = None  

    def get_ectoplasm_cost(self):
        return self.__ectoplasm_cost

    ectoplasm_cost = property(get_ectoplasm_cost)

    def get_ritual_name(self):
        return self.__ritual_name

    ritual_name = property(get_ritual_name)


    def get_starting_health(self):
        return self.__starting_health
        
    starting_health = property(get_starting_health)


    def get_starting_power(self):
        return self.__starting_power
        
    starting_power = property(get_starting_power)


    def get_necrotic_cost(self):
        return self.__necrotic_cost
        
    necrotic_cost = property(get_necrotic_cost)


    def get_spirit_cost(self):
        return self.__spirit_cost
        
    spirit_cost = property(get_spirit_cost)

    def get_bone_cost(self):
        return self.__bone_cost
                
    bone_cost = property(get_bone_cost)


    def get_flesh_cost(self):
        return self.__flesh_cost

    flesh_cost = property(get_flesh_cost)

    def get_summon_class(self):
        return self.__summon_class

    summon_class = property(get_summon_class)

    def check_ritual(self, resource):
        if isinstance(resource, Resource):
            if resource.check_requirements(
                necrotic_rune=self.necrotic_cost,
                spirit_rune=self.spirit_cost,
                bone_rune=self.bone_cost,
                flesh_rune=self.flesh_cost,
                ectoplasm=self.ectoplasm_cost
                ):
                return True
            else:
                print("not enough resources")
                return False
        else:
            print("invalid resource object")
            return False

    def consume_resources(self, resource):
        if isinstance(resource, Resource):
            if resource.spend_resource(
                necrotic_rune=self.necrotic_cost,
                spirit_rune=self.spirit_cost,
                bone_rune=self.bone_cost,
                flesh_rune=self.flesh_cost,
                ectoplasm=self.ectoplasm_cost
                ):
                return True
            else:
                print("failed to consume resources")
                return False
        else:
            print("invalid resource object")
            return False

    def create_summon(self, unit_id):
        return self.summon_class(unit_id)


if __name__ == '__main__':
    from skeletonWarrior import SkeletonWarrior
    from vengefulGhost import VengefulGhost
    from putridZombie import PutridZombie
    from phantomGuardian import PhantomGuardian

    ritual = SummoningRitual("Undead Skeleton Warrior", SkeletonWarrior, SkeletonWarrior.MIN_HEALTH, SkeletonWarrior.MIN_POWER, bone_cost=5, ectoplasm_cost=3)
    ritual_1 = SummoningRitual("Vengeful Ghost", VengefulGhost, VengefulGhost.MIN_HEALTH, VengefulGhost.MIN_POWER, spirit_cost=5, ectoplasm_cost=3)
    ritual_2 = SummoningRitual("Putrid Zombie", PutridZombie, PutridZombie.MIN_HEALTH, PutridZombie.MIN_POWER, flesh_cost=5, ectoplasm_cost=3)
    ritual_3 = SummoningRitual("Phantom Guardian", PhantomGuardian, PhantomGuardian.MIN_HEALTH, PhantomGuardian.MIN_POWER, spirit_cost=7, ectoplasm_cost=3)


