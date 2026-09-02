class Resource:
    MIN_QUANTITY = 0

    def __init__(self, necrotic_rune, spirit_rune, bone_rune, flesh_rune, ectoplasm):
        self.__necrotic_rune = self.set_necrotic_rune(necrotic_rune)
        self.__spirit_rune = self.set_spirit_rune(spirit_rune)
        self.__bone_rune = self.set_bone_rune(bone_rune)
        self.__flesh_rune = self.set_flesh_rune(flesh_rune)
        self.__ectoplasm = self.set_ectoplasm(ectoplasm)

    def get_necrotic_rune(self):
        return self.__necrotic_rune
    
    def set_necrotic_rune(self, value):
        if isinstance(value, int) and value >= self.MIN_QUANTITY:
            self.__necrotic_rune = value
            return self.__necrotic_rune
        else:
            print("invalid necrotic rune quantity")
            return None

    necrotic_rune = property(get_necrotic_rune)

    def get_spirit_rune(self):
        return self.__spirit_rune

    def set_spirit_rune(self, value):
        if isinstance(value, int) and value >= self.MIN_QUANTITY:
            self.__spirit_rune = value
            return self.__spirit_rune
        else:
            print("invalid spirit rune quantity")
            return None

    spirit_rune = property(get_spirit_rune)

    def get_bone_rune(self):
        return self.__bone_rune

    def set_bone_rune(self, value):
        if isinstance(value, int) and value >= self.MIN_QUANTITY:
            self.__bone_rune = value
            return self.__bone_rune
        else:
            print("invalid bone rune quantity")
            return None

    bone_rune = property(get_bone_rune)

    def get_flesh_rune(self):
        return self.__flesh_rune

    def set_flesh_rune(self, value):
        if isinstance(value, int) and value >= self.MIN_QUANTITY:
            self.__flesh_rune = value
            return self.__flesh_rune
        else:
            print("invalid flesh rune quantity")
            return None

    flesh_rune = property(get_flesh_rune)

    def get_ectoplasm(self):
        return self.__ectoplasm

    def set_ectoplasm(self, value):
        if isinstance(value, int) and value >= self.MIN_QUANTITY:
            self.__ectoplasm = value
            return self.__ectoplasm
        else:
            print("invalid ectoplasm quantity")
            return None

    ectoplasm = property(get_ectoplasm)



    def collect_resource(self, necrotic_rune=0, spirit_rune=0, bone_rune=0, flesh_rune=0, ectoplasm=0):
        if (isinstance(necrotic_rune, int) and necrotic_rune >= self.MIN_QUANTITY and
            isinstance(spirit_rune, int) and spirit_rune >= self.MIN_QUANTITY and
            isinstance(bone_rune, int) and bone_rune >= self.MIN_QUANTITY and
            isinstance(flesh_rune, int) and flesh_rune >= self.MIN_QUANTITY and
            isinstance(ectoplasm, int) and ectoplasm >= self.MIN_QUANTITY):

            self.set_necrotic_rune(self.__necrotic_rune + necrotic_rune)
            self.set_spirit_rune(self.__spirit_rune + spirit_rune)
            self.set_bone_rune(self.__bone_rune + bone_rune)
            self.set_flesh_rune(self.__flesh_rune + flesh_rune)
            self.set_ectoplasm(self.__ectoplasm + ectoplasm)
            return True
        else:
            print("invalid resource quantity supplied")
            return False

    def check_requirements(self, necrotic_rune=0, spirit_rune=0, bone_rune=0, flesh_rune=0, ectoplasm=0):
        if (necrotic_rune <= self.__necrotic_rune and
            spirit_rune <= self.__spirit_rune and
            bone_rune <= self.__bone_rune and
            flesh_rune <= self.__flesh_rune and
            ectoplasm <= self.__ectoplasm):
            return True
        else:
            print("not enough resources")
            return False

    def spend_resource(self, necrotic_rune=0, spirit_rune=0, bone_rune=0, flesh_rune=0, ectoplasm=0):
        if not self.check_requirements(necrotic_rune, spirit_rune, bone_rune, flesh_rune, ectoplasm):
            return False
        
        else:
            self.set_necrotic_rune(self.__necrotic_rune - necrotic_rune)
            self.set_spirit_rune(self.__spirit_rune - spirit_rune)
            self.set_bone_rune(self.__bone_rune - bone_rune)
            self.set_flesh_rune(self.__flesh_rune - flesh_rune)
            self.set_ectoplasm(self.__ectoplasm - ectoplasm)
            return True

    def __str__(self):
        return (f"Available resources:"
                f"Necrotic Runes = {self.necrotic_rune}"
                f"Spirit Runes = {self.spirit_rune}"
                f"Bone Runes = {self.bone_rune}"
                f"Flesh Runes = {self.flesh_rune}"
                f"Ectoplasm = {self.ectoplasm}")


            

    
        




