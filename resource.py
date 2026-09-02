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


    def __str__(self):
        return (f"Necrotic Runes: {self.__necrotic_rune}, "
                f"Spirit Runes: {self.__spirit_rune}, "
                f"Bone Runes: {self.__bone_rune}, "
                f"Flesh Runes: {self.__flesh_rune}, "
                f"Ectoplasm: {self.__ectoplasm}")

        
            

    
        




