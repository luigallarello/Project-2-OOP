class SummoningRitual:
    def __init__(self, ritual_name, undead_name, starting_health, starting_power,
                 necrotic_cost=0, spirit_cost=0, bone_cost=0, flesh_cost=0, ectoplasm_cost=0):
        self.__ritual_name = ritual_name
        self.__undead_name = undead_name
        self.__starting_health = starting_health
        self.__starting_power = starting_power
        self.__necrotic_cost = necrotic_cost
        self.__spirit_cost = spirit_cost
        self.__bone_cost = bone_cost
        self.__flesh_cost = flesh_cost

        if ectoplasm_cost > 0:
            self.__ectoplasm_cost = ectoplasm_cost
        else:
            print("ritual must use ectoplasm")
            self.__ectoplasm_cost = None  

        def get_ritual_name(self):
            return self.__ritual_name

        ritual_name = property(get_ritual_name)


        def get_undead_name(self):
            return self.__undead_name
        
        undead_name = property(get_undead_name)


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




