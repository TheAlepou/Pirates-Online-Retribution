from panda3d.core import VBase3
from pirates.piratesbase import PLocalizer
from pirates.battle import EnemyGlobals
from pirates.battle.EnemySkills import *
from pirates.pirate import AvatarTypes
from pirates.uberdog.UberDogGlobals import InventoryType
from pirates.inventory import ItemGlobals
BOSS_NPC_LIST = {
    '': {
        'AvatarType': None,
        'HpScale': 5,
        'MpScale': 1,
        'Level': None,
        'Weapon': None,
        'WeaponLevel': 0,
        'Skills': [],
        'SkillLevel': 0,
        'GoldScale': 2,
        'ModelScale': 1.10,
        'DamageScale': 1,
        'ArmorScale': 1.0,
        'HighlightColor': VBase3(1) },
    'dynamicBoss_1': {
        'AvatarType': AvatarTypes.Muck,
        'Level': 14,
        'Weapon': EnemyGlobals.CUTLASS,
        'Skills': (InventoryType.CutlassSlash, EnemySkills.CUTLASS_CHOP, EnemySkills.CUTLASS_WILDSLASH, InventoryType.CutlassCleave, EnemySkills.CUTLASS_DOUBLESLASH),
        'HpScale': 5,
        'GoldScale': 2,
        'ModelScale': 1.3,
        'HighlightColor': VBase3(1, 0.5, 0.5) },
    '1154059362.19Shochet': {
        'Skills': (EnemySkills.DUAL_CLAW,),
        'HpScale': 2,
        'GoldScale': 2,
        'ModelScale': 3,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1154059366.69Shochet': {
        'Skills': (EnemySkills.FLYTRAP_SPIT,),
        'HpScale': 2,
        'GoldScale': 2,
        'ModelScale': 3,
        'HighlightColor': VBase3(1, 0, 1) },
    '1169616489.03Shochet': {
        'Skills': (EnemySkills.STUMP_STOMP,),
        'HpScale': 2,
        'GoldScale': 2,
        'ModelScale': 3,
        'HighlightColor': VBase3(1, 0, 0.5) },
    '1247517440.0jloehrle': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.75,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1220906480.53mtucker': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.75,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1219434293.16mtucker': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.75,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1238440501.07piwanow': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.75,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1239930457.38piwanow': {
        'HpScale': 2,
        'MpScale': 1.5,
        'Level': 6,
        'GoldScale': 2,
        'ModelScale': 1.2,
        'DamageScale': 1.3,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1238441187.46piwanow': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.5,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1219426331.38mtucker': {
        'HpScale': 7,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.5,
        'DamageScale': 1.75,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1248740229.97robrusso': {
        'HpScale': 1,
        'MpScale': 1,
        'GoldScale': 2,
        'ModelScale': 1.2,
        'DamageScale': 1,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1274906957.35gcarranza': {
        'HpScale': 3.5,
        'MpScale': 3,
        'Level': 30,
        'GoldScale': 2,
        'ModelScale': 1.0,
        'DamageScale': 2.0,
        'HighlightColor': VBase3(1, 1, 1) },
    '1274889994.04gcarranza': {
        'HpScale': 5,
        'MpScale': 3,
        'Level': 40,
        'GoldScale': 2,
        'ModelScale': 1.3,
        'DamageScale': 2.0,
        'HighlightColor': VBase3(1, 1, 1) },
    '1291327895.46jloehrle': {
        'HpScale': 50,
        'MpScale': 10,
        'Level': 50,
        'GoldScale': 2,
        'ModelScale': 1.5,
        'DamageScale': 6.0,
        'HighlightColor': VBase3(1, 1, 1),
        'DropAmount': 2,
        'DropRate': 100,
        'RarityDict': {
            ItemGlobals.FAMED: 15,
            ItemGlobals.LEGENDARY: 10 } },
    '1302895055.78jloehrle': {
        'HpScale': 5,
        'MpScale': 3,
        'Level': 25,
        'GoldScale': 2,
        'ModelScale': 1.3,
        'DamageScale': 2.0,
        'HighlightColor': VBase3(1, 1, 1) },
    '1303260680.08jloehrle': {
        'HpScale': 5,
        'MpScale': 3,
        'Level': 35,
        'GoldScale': 2,
        'ModelScale': 1.0,
        'DamageScale': 3.0,
        'HighlightColor': VBase3(1, 1, 1) },
    '1303331892.2jloehrle': {
        'HpScale': 5,
        'MpScale': 3,
        'Level': 35,
        'GoldScale': 2,
        'ModelScale': 1.0,
        'DamageScale': 3.0,
        'HighlightColor': VBase3(1, 1, 1) },
    '1219352693.09mtucker': {
        'HpScale': 10,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.5,
        'DamageScale': 1.75,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1219367627.94mtucker': {
        'HpScale': 10,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.5,
        'DamageScale': 1.75,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1219339266.79mtucker': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.10,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1219277508.79mtucker': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.5,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1219277509.79mtucker': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.5,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1244583168.0jloehrle0': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.5,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1244833920.0jloehrle': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.5,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1218760329.71mtucker': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.0,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1218760328.71mtucker': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.0,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1244657664.0jloehrle1': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 1.5,
        'DamageScale': 2.0,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '1244832512.0jloehrle': {
        'HpScale': 5,
        'MpScale': 3,
        'GoldScale': 2,
        'ModelScale': 2.0,
        'DamageScale': 1.5,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '.mtucker': {
        'HpScale': 2,
        'MpScale': 2,
        'Skills': [],
        'Level': 23,
        'GoldScale': 2,
        'ModelScale': 2,
        'DamageScale': 1,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '.mtucker': {
        'HpScale': 2,
        'MpScale': 2,
        'Skills': [],
        'Level': 23,
        'GoldScale': 2,
        'ModelScale': 2,
        'DamageScale': 1,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '.mtucker': {
        'HpScale': 2,
        'MpScale': 2,
        'Skills': [],
        'Level': 23,
        'GoldScale': 2,
        'ModelScale': 2,
        'DamageScale': 1,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '.mtucker': {
        'HpScale': 2,
        'MpScale': 2,
        'Skills': [],
        'Level': 23,
        'GoldScale': 2,
        'ModelScale': 2,
        'DamageScale': 1,
        'HighlightColor': VBase3(0, 1, 0.5) },
    '.mtucker': {
        'HpScale': 2,
        'MpScale': 2,
        'Skills': [],
        'Level': 23,
        'GoldScale': 2,
        'ModelScale': 2,
        'DamageScale': 1,
        'ArmorScale': 0.100,
        'HighlightColor': VBase3(0, 1, 0.5) } }
