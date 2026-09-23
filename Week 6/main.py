from resource import Resource
from summoning_ritual import SummoningRitual
from undead import Undead
from necromancer import Necromancer
from warriorUndead import WarriorUndead
from cursedUndead import CursedUndead
from DeathKnight import DeathKnight
from skeletonWarrior import SkeletonWarrior
from phantomGuardian import PhantomGuardian
from vengefulGhost import VengefulGhost
from putridZombie import PutridZombie

# r = Resource(5, 5, 5, 5, 5)
# # print(r)

# r.collect_resource(15, 15, 15, 15, 15)
# print(r)

skeleton_ritual = SummoningRitual("Undead Skeleton Warrior", SkeletonWarrior, SkeletonWarrior.MIN_HEALTH, SkeletonWarrior.MIN_POWER, bone_cost=5, ectoplasm_cost=3)
ghost_ritual = SummoningRitual("Vengeful Ghost", VengefulGhost, VengefulGhost.MIN_HEALTH, VengefulGhost.MIN_POWER, spirit_cost=5, ectoplasm_cost=3)
zombie_ritual = SummoningRitual("Putrid Zombie", PutridZombie, PutridZombie.MIN_HEALTH, PutridZombie.MIN_POWER, flesh_cost=5, ectoplasm_cost=3)
phantom_ritual = SummoningRitual("Phantom Guardian", PhantomGuardian, PhantomGuardian.MIN_HEALTH, PhantomGuardian.MIN_POWER, spirit_cost=7, ectoplasm_cost=3)

death_knight_ritual = SummoningRitual(
    "Death Knight Ritual", DeathKnight, DeathKnight.MIN_HEALTH, DeathKnight.MIN_POWER,
    necrotic_cost=10, spirit_cost=8, bone_cost=8, flesh_cost=8, ectoplasm_cost=10
)

# print(r.necrotic_rune, r.spirit_rune, r.flesh_rune, r.bone_rune, r.ectoplasm)

# print(skeleton_ritual.check_ritual(r))
# # print(skeleton_ritual.consume_resources(r))

# u = skeleton_ritual.create_summon(1)
# print(u)

# u.level_up()
# print(u)

necromancer_1 = Necromancer('Lui')
necromancer_1.collect_resource(20, 20, 20, 20, 20)


u1 = necromancer_1.summon(skeleton_ritual)
u2 = necromancer_1.summon(ghost_ritual)
u3 = necromancer_1.summon(zombie_ritual)
u4 = necromancer_1.summon(phantom_ritual)

print(necromancer_1.resource)

u5 = necromancer_1.summon(skeleton_ritual)
u6 = necromancer_1.summon(ghost_ritual)

necromancer_1.collect_resource(20, 20, 20, 20, 20)

print(u1)
necromancer_1.level_undead(u1.unit_id)
print(u1)

necromancer_1.dismiss(u1.unit_id)
print(necromancer_1.get_controlled_undead())


# --- Task 4: Death Knight ---

necromancer_1.collect_resource(20, 20, 20, 20, 20)

death_knight = necromancer_1.summon(death_knight_ritual)

print()
print(death_knight)

print('isinstance(death_knight, WarriorUndead):', isinstance(death_knight, WarriorUndead))
print('isinstance(death_knight, CursedUndead):', isinstance(death_knight, CursedUndead))
print('isinstance(death_knight, Undead):', isinstance(death_knight, Undead))

print()
print('DeathKnight MRO:')
for cls in DeathKnight.__mro__:
    print(' ', cls.__name__)

print()
print('combat_style() via super():', death_knight.combat_style())

warrior_style, cursed_style = death_knight.compare_combat_styles()
print('WarriorUndead.combat_style(self):', warrior_style)
print('CursedUndead.combat_style(self): ', cursed_style)

print()
print(death_knight.command())
necromancer_1.level_undead(death_knight.unit_id)
print(death_knight)







