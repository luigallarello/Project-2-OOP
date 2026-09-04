from resource import Resource
from summoning_ritual import SummoningRitual
from undead import Undead

r = Resource(5, 5, 5, 5, 5)
print(r)

r.collect_resource(5, 5, 5, 5, 5)
print(r)

skeleton_ritual = SummoningRitual("Undead Skeleton Warrior", "Skeleton Warrior", 20, 10, bone_cost=5, ectoplasm_cost=3)
ghost_ritual = SummoningRitual("Vengeful Ghost", "Vengeful Ghost", 20, 10, spirit_cost=5, ectoplasm_cost=3)
zombie_ritual = SummoningRitual("Putrid Zombie", "Putrid Zombie", 20, 10, flesh_cost=5, ectoplasm_cost=3)
phantom_ritual = SummoningRitual("Phantom Guardian", "Phantom Guardian", 20, 10, spirit_cost=7, ectoplasm_cost=3)

print(r.necrotic_rune, r.spirit_rune, r.flesh_rune, r.bone_rune, r.ectoplasm)

print(skeleton_ritual.check_ritual(r))
# print(skeleton_ritual.consume_resources(r))

u = skeleton_ritual.create_undead(1, r)
print(u)

u.level_up()
print(u)




