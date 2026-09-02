class Resource:
    MIN_QUANTITY = 0

    def __init__(self, necrotic_rune, spirit_rune, bone_rune, flesh_rune, ectoplasm):
        self.__necrotic_rune = self.set_necrotic_rune(necrotic_rune)
        self.__spirit_rune = self.set_spirit_rune(spirit_rune)
        self.__bone_rune = self.set_bone_rune(bone_rune)
        self.__flesh_rune = self.set_flesh_rune(flesh_rune)
        self.__ectoplasm = self.set_ectoplasm(ectoplasm)

    def set_necrotic_rune(self, value):
        if isinstance(value, int) and value >= self.MIN_QUANTITY:
            self.__necrotic_rune = value
            return self.__necrotic_rune
        else:
            print("invalid necrotic rune quantity")
            return None

    def set_spirit_rune(self, value):
        if isinstance(value, int) and value >= self.MIN_QUANTITY:
            self.__spirit_rune = value
            return self.__spirit_rune
        else:
            print("invalid spirit rune quantity")
            return None

    def set_bone_rune(self, value):
        if isinstance(value, int) and value >= self.MIN_QUANTITY:
            self.__bone_rune = value
            return self.__bone_rune
        else:
            print("invalid bone rune quantity")
            return None

    def set_flesh_rune(self, value):
        if isinstance(value, int) and value >= self.MIN_QUANTITY:
            self.__flesh_rune = value
            return self.__flesh_rune
        else:
            print("invalid flesh rune quantity")
            return None

    def set_ectoplasm(self, value):
        if isinstance(value, int) and value >= self.MIN_QUANTITY:
            self.__ectoplasm = value
            return self.__ectoplasm
        else:
            print("invalid ectoplasm quantity")
            return None



    def collect_resource(self, necrotic_rune=0, spirit_rune=0, bone_rune=0, flesh_rune=0, ectoplasm=0):
        amounts = {
            "necrotic_rune": necrotic_rune,
            "spirit_rune": spirit_rune,
            "bone_rune": bone_rune,
            "flesh_rune": flesh_rune,
            "ectoplasm": ectoplasm,
            }

        # Step 1: validate everything first, change nothing yet
        for name, value in amounts.items():
            if not (isinstance(value, int) and value >= self.MIN_QUANTITY):
                print(f"invalid quantity for {name}")
                return False

        # Step 2: all valid, now safe to apply changes
        self.set_necrotic_rune(self.__necrotic_rune + necrotic_rune)
        self.set_spirit_rune(self.__spirit_rune + spirit_rune)
        self.set_bone_rune(self.__bone_rune + bone_rune)
        self.set_flesh_rune(self.__flesh_rune + flesh_rune)
        self.set_ectoplasm(self.__ectoplasm + ectoplasm)

        return True 

    def check_requirements(self, necrotic_rune=0, spirit_rune=0, bone_rune=0, flesh_rune=0, ectoplasm=0):
        required = {
            "necrotic_rune": (necrotic_rune, self.__necrotic_rune),
            "spirit_rune": (spirit_rune, self.__spirit_rune),
            "bone_rune": (bone_rune, self.__bone_rune),
            "flesh_rune": (flesh_rune, self.__flesh_rune),
            "ectoplasm": (ectoplasm, self.__ectoplasm),
            }

        for name, (needed, available) in required.items():
            if needed > available:
                print(f"not enough {name}")
                return False

        return True
            

    
        




