Workshop 4-1    2/09
Today we begin the Necromancy game with creating some of the intial classes. Wasn't able to get a code review from the teacher in the lesson, explained that it would be undertaken next workshop. Didn;t manage to quite finish code from today.

Workshop 4-2   *CODE REVIEW* 4/09
Managed to finish 4-1 tasks. My original resources contained separate setters for each resource. 

 def set_necrotic_rune(self, value):
        if isinstance(value, int) and value >= self.MIN_QUANTITY:
            self.__necrotic_rune = value
            return self.__necrotic_rune
        else:
            print("invalid necrotic rune quantity")
            return None

def set_flesh_rune etc....

Reccomended I trim all that into one method to allow for less bloated code. Something like:

def validate_resource etc....

Also initially had consume_resource as part of create_undead but was told to remove it as the necromancer will handle all of that.

def create_undead(self, unit_id, resource):
        if self.consume_resources(resource) and self.check_ritual(resource) == True:
            return Undead(unit_id, self.undead_name, self.starting_health, self.starting_power)
        else:
            print (f'Cannot create undead, requirements not met')
            return False

    =====

 def create_undead(self, unit_id, resource):
            return Undead(unit_id, self.undead_name, self.starting_health, self.starting_power)

