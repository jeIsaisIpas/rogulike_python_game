# English UI translation generated automatically. Identifiers kept to preserve compatibility.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#V18 - ROGUELIKE CATACOMBES

import os 
import json 
import random 
from dataclasses import dataclass ,field 
from typing import List ,Dict ,Tuple ,Optional 

# ======================================================
# ANSI Colors
# ======================================================
COLOR_RESET ="\033[0m"
COLOR_RED ="\033[91m"
COLOR_GREEN ="\033[92m"
COLOR_YELLOW ="\033[93m"
COLOR_BLUE ="\033[94m"
COLOR_MAGENTA ="\033[95m"
COLOR_CYAN ="\033[96m"
COLOR_BOLD ="\033[1m"

def rgb (r :int ,g :int ,b :int )->str :
    """Return a 24-bit ANSI foreground color code (RGB)."""
    return f"[38;2;{r };{g };{b }m"

def rgb_bg (r :int ,g :int ,b :int )->str :
    """Return a 24-bit ANSI background color code (RGB)."""
    return f"[48;2;{r };{g };{b }m"

    # Redefinition of colors in RGB style for V18
COLOR_RED =rgb (255 ,80 ,80 )
COLOR_GREEN =rgb (80 ,255 ,80 )
COLOR_YELLOW =rgb (255 ,220 ,50 )
COLOR_BLUE =rgb (80 ,160 ,255 )
COLOR_MAGENTA =rgb (220 ,80 ,255 )
COLOR_CYAN =rgb (80 ,255 ,255 )
COLOR_BOLD ="[1m"


def clear_console ()->None :
    os .system ('cls'if os .name =='nt'else 'clear')


def wait_for_enter ()->None :
    input ("Press Enter to continue...")


    # ======================================================
    # Base data : player classes, weapons, relics, zones
    # ======================================================
PLAYER_CLASSES :Dict [str ,Dict ]={
"1":{"name":'Warrior',"hp":35 ,"attack":6 ,"defense":3 ,"mana":5 ,"power":"Combat techniques"},
"2":{"name":"Mage","hp":22 ,"attack":4 ,"defense":1 ,"mana":15 ,"power":"Elemental arcana"},
"3":{"name":"Rogue","hp":28 ,"attack":5 ,"defense":2 ,"mana":8 ,"power":"Stealth arts"},
"4":{"name":"Paladin","hp":40 ,"attack":5 ,"defense":4 ,"mana":8 ,"power":"Sacred light"},
"5":{"name":"Ranger","hp":30 ,"attack":6 ,"defense":2 ,"mana":7 ,"power":"Bow mastery"},
"6":{"name":"Necromancer","hp":24 ,"attack":5 ,"defense":1 ,"mana":18 ,"power":'Forbidden magic'},
"7":{"name":'Shadow Assassin',"hp":26 ,"attack":7 ,"defense":2 ,"mana":10 ,"power":"Shadow arts"},
"8":{"name":"Berserker","hp":38 ,"attack":8 ,"defense":2 ,"mana":4 ,"power":"Blood rage"},
"9":{"name":"Bard","hp":27 ,"attack":4 ,"defense":2 ,"mana":14 ,"power":"Inspiring songs"},
"10":{"name":"Monk","hp":32 ,"attack":5 ,"defense":3 ,"mana":9 ,"power":"Spiritual martial arts"},
"11":{"name":"Summoner","hp":23 ,"attack":3 ,"defense":1 ,"mana":20 ,"power":"Ancient summons"},
}


@dataclass 
class Weapon :
    name :str 
    atk_bonus :int =0 
    crit_bonus :float =0.0 
    description :str =""


WEAPONS :List [Weapon ]=[
Weapon ('Training Sword',atk_bonus =0 ,crit_bonus =0.0 ,
description ='An old sword with no special bonus.'),
Weapon ('Longsword',atk_bonus =2 ,crit_bonus =0.05 ,
description ='A sturdy sword that deals above-average damage.'),
Weapon ("Heavy Axe",atk_bonus =3 ,crit_bonus =0.0 ,
description ='A very powerful axe, ideal for big raw hits.'),
Weapon ("Twin Daggers",atk_bonus =1 ,crit_bonus =0.12 ,
description ='Two fast daggers: higher crits and a small chance to poison.'),
Weapon ("Runic Keyboard of 1000 Lines",atk_bonus =5 ,crit_bonus =0.25 ,
description ="Runic weapon: massive damage and devastating critical hits."),
Weapon ("Sacred Mace",atk_bonus =2 ,crit_bonus =0.02 ,
description ="A blessed mace, moderately powerful and very reliable."),
Weapon ("Ember Blade",atk_bonus =2 ,crit_bonus =0.08 ,
description ='A burning blade: increased damage and more frequent crits.'),
Weapon ("Shadow Bow",atk_bonus =1 ,crit_bonus =0.15 ,
description ='A light bow: low raw attack but huge critical chance.'),
]


@dataclass 
class Relic :
    name :str 
    atk_bonus :int =0 
    def_bonus :int =0 
    crit_bonus :float =0.0 
    lifesteal :float =0.0 
    description :str =""


RELICS :List [Relic ]=[
Relic ("Amulet of Fury",atk_bonus =2 ,crit_bonus =0.05 ,
description ="+2 ATK and +5% crit."),
Relic ("Stone Talisman",def_bonus =2 ,
description ="+2 DEF."),
Relic ("Vampiric Ring",lifesteal =0.3 ,
description ="Life steal: 30% of damage dealt."),
Relic ("Critical Eye",crit_bonus =0.2 ,
description ='+20% critical hit chance.'),
Relic ("Creator's Feather",atk_bonus =3 ,def_bonus =1 ,crit_bonus =0.15 ,lifesteal =0.15 ,
description ="Mythic relic: ATK+3, DEF+1, crit+15%, life steal."),
Relic ("Golem Charm",def_bonus =3 ,
description ="+3 DEF: your skin hardens like stone."),
Relic ("Vampire Seal",lifesteal =0.2 ,
description ="Life steal 20%: each hit heals you slightly."),
Relic ("Star Fragment",atk_bonus =1 ,crit_bonus =0.1 ,
description ="+1 ATK and +10% crit: your strikes hit like starlight shards."),
]


# ======================================================
# Cards (progression system V17)
# ======================================================
@dataclass 
class Card :
    name :str 
    description :str 
    rarete :str # "Common", "Rare", "Epic", "Legendary"
    classes_autorisees :Optional [List [str ]]=None # None => generique
    bonus_hp_max :int =0 
    bonus_attack :int =0 
    bonus_defense :int =0 
    bonus_mana_max :int =0 
    bonus_potions :int =0 
    bonus_critique :float =0.0 


CARDS_POOL :List [Card ]=[
# Generic commons
Card ("Endurance","+5 HP max","Common",bonus_hp_max =5 ),
Card ('Tensed Muscles',"+1 ATK","Common",bonus_attack =1 ),
Card ('Defensive Stance',"+1 DEF","Common",bonus_defense =1 ),
Card ("Meditation","+2 mana max","Common",bonus_mana_max =2 ),
Card ('Emergency Flask',"+1 potion","Common",bonus_potions =1 ),

# Generic rares
Card ('Warrior Blood',"+10 HP max","Rare",bonus_hp_max =10 ),
Card ('Sharpened Blade',"+2 ATK","Rare",bonus_attack =2 ),
Card ('Fitted Armor',"+2 DEF","Rare",bonus_defense =2 ),
Card ("Esprit focalise","+4 mana max","Rare",bonus_mana_max =4 ),
Card ('Mobile Pharmacy',"+2 potions","Rare",bonus_potions =2 ),

# Generic epics
Card ('Supernatural Toughness',"+15 HP max","Epic",bonus_hp_max =15 ),
Card ('Brute Force',"+3 ATK","Epic",bonus_attack =3 ),
Card ('Iron Wall',"+3 DEF","Epic",bonus_defense =3 ),
Card ('Mystic Reservoir',"+6 mana max","Epic",bonus_mana_max =6 ),
Card ('Potion Specialist',"+3 potions","Epic",bonus_potions =3 ),

# Generic legendaries
Card ('Immortal Colossus',"+25 HP max, +2 DEF","Legendary",bonus_hp_max =25 ,bonus_defense =2 ),
Card ('Blade of Destiny',"+5 ATK, +10% crit","Legendary",bonus_attack =5 ,bonus_critique =0.10 ),
Card ('Arcane Master',"+8 mana max, +2 ATK","Legendary",bonus_mana_max =8 ,bonus_attack =2 ),

# Class-specific cards (examples)
Card ('Warrior Discipline','+3 ATK (Warrior)',"Rare",
classes_autorisees =['Warrior'],bonus_attack =3 ),
Card ('Occult Studies',"+5 mana max (Necromancer)","Rare",
classes_autorisees =["Necromancer"],bonus_mana_max =5 ),
Card ('Stealth Instinct','+10% crit (Rogue / Shadow Assassin)',"Rare",
classes_autorisees =["Rogue",'Shadow Assassin'],bonus_critique =0.10 ),
]


# Enemies & zones
CATACOMBES_ENNEMIS =[
{"name":"Giant Rat","hp":12 ,"attack":3 ,"defense":1 ,"gold":(3 ,7 ),"xp":(5 ,8 )},
{"name":'Gobelin',"hp":18 ,"attack":4 ,"defense":1 ,"gold":(6 ,12 ),"xp":(8 ,12 )},
{"name":'Squelette',"hp":20 ,"attack":5 ,"defense":2 ,"gold":(10 ,18 ),"xp":(10 ,14 )},
]

FORET_ENNEMIS =[
{"name":"Dark Wolf","hp":22 ,"attack":6 ,"defense":2 ,"gold":(10 ,18 ),"xp":(12 ,18 )},
{"name":'Corrupted Dryad',"hp":26 ,"attack":5 ,"defense":3 ,"gold":(12 ,20 ),"xp":(14 ,20 )},
{"name":"Raging Ent","hp":30 ,"attack":7 ,"defense":3 ,"gold":(15 ,24 ),"xp":(16 ,22 )},
]

CITADELLE_ENNEMIS =[
{"name":"Runic Guard","hp":32 ,"attack":8 ,"defense":4 ,"gold":(18 ,26 ),"xp":(18 ,26 )},
{"name":"Crystal Mage","hp":28 ,"attack":9 ,"defense":3 ,"gold":(20 ,30 ),"xp":(20 ,28 )},
{"name":"Spectral Knight","hp":36 ,"attack":9 ,"defense":4 ,"gold":(24 ,34 ),"xp":(22 ,30 )},
]

CATACOMBES_BOSSES =[
{"name":'Lord of Bones',"hp":45 ,"attack":7 ,"defense":3 ,"gold":(30 ,45 ),"xp":(35 ,50 )},
{"name":"Deep Lich","hp":40 ,"attack":9 ,"defense":2 ,"gold":(30 ,45 ),"xp":(35 ,50 )},
]

FORET_BOSSES =[
{"name":'Putrid Forest Spirit',"hp":55 ,"attack":9 ,"defense":4 ,"gold":(40 ,60 ),"xp":(45 ,65 )},
{"name":"Spider Queen","hp":50 ,"attack":10 ,"defense":3 ,"gold":(40 ,60 ),"xp":(45 ,65 )},
]

CITADELLE_BOSSES =[
{"name":'Runic Lord',"hp":70 ,"attack":11 ,"defense":5 ,"gold":(60 ,80 ),"xp":(70 ,90 )},
{"name":"Void Champion","hp":65 ,"attack":12 ,"defense":4 ,"gold":(60 ,80 ),"xp":(70 ,90 )},
]

ZONES =[
{"name":"Catacombs","start":1 ,"fin":10 ,'ennemis':CATACOMBES_ENNEMIS ,'bosses':CATACOMBES_BOSSES },
{"name":'Cursed Forest',"start":11 ,"fin":20 ,'ennemis':FORET_ENNEMIS ,'bosses':FORET_BOSSES },
{"name":"Runic Citadel","start":21 ,"fin":30 ,'ennemis':CITADELLE_ENNEMIS ,'bosses':CITADELLE_BOSSES },
]

MAX_ETAGES =100 


# ======================================================
# Skill tree (skill tree) V17.2
# ======================================================
SKILL_TREE :Dict [str ,Dict ]={
# Base stat upgrades
"hp1":{
"name":"+5 HP base",
"description":'Increase base HP by 5 for all runs.',
"cout":5 ,
"type":"stat",
"cible":"hp_bonus",
"valeur":5 ,
"prerequis":[],
},
"atk1":{
"name":"+1 ATK base",
"description":"Increase base attack by 1.",
"cout":5 ,
"type":"stat",
"cible":"attack_bonus",
"valeur":1 ,
"prerequis":[],
},
"def1":{
"name":"+1 DEF base",
"description":"Increase base defense by 1.",
"cout":5 ,
"type":"stat",
"cible":"defense_bonus",
"valeur":1 ,
"prerequis":[],
},
"mana1":{
"name":"+2 mana base",
"description":"Increase base mana by 2.",
"cout":4 ,
"type":"stat",
"cible":"mana_bonus",
"valeur":2 ,
"prerequis":[],
},

# Starting resources
"potion1":{
"name":"+1 starting potion",
"description":"Start each run with one extra potion.",
"cout":6 ,
"type":"start_res",
"cible":"potions_start",
"valeur":1 ,
"prerequis":["hp1"],
},
"gold1":{
"name":"+5 starting gold",
"description":"Start each run with +5 gold.",
"cout":4 ,
"type":"start_res",
"cible":"gold_start",
"valeur":5 ,
"prerequis":["atk1"],
},

# Shop / mystery chances
"shop1":{
"name":'+1 level chance shop',
"description":"Increases the probability of finding a shop.",
"cout":6 ,
"type":'chance',
"cible":'bonus_chance_shop',
"valeur":1 ,
"prerequis":["gold1"],
},
"mystery1":{
"name":'+1 mystery event chance level',
"description":"Increases the probability of triggering a mystery event.",
"cout":6 ,
"type":'chance',
"cible":'bonus_chance_mystery',
"valeur":1 ,
"prerequis":["mana1"],
},

# Unlock existing classes
"class_paladin":{
"name":"Unlock Paladin",
"description":"Allows you to choose the class Paladin at the start of the run.",
"cout":8 ,
"type":"unlock_class",
"cible":"Paladin",
"valeur":1 ,
"prerequis":["hp1"],
},
'class_rodeur':{
"name":"Unlock Ranger",
"description":"Allows you to choose the class Ranger at the start of the run.",
"cout":8 ,
"type":"unlock_class",
"cible":"Ranger",
"valeur":1 ,
"prerequis":["atk1"],
},
'class_necromancien':{
"name":"Unlock Necromancer",
"description":"Allows you to choose the class Necromancer at the start of the run.",
"cout":9 ,
"type":"unlock_class",
"cible":"Necromancer",
"valeur":1 ,
"prerequis":["mana1"],
},
'class_assassin_shadow':{
"name":'Unlock Shadow Assassin',
"description":'Allows you to choose the class Shadow Assassin at the start of the run.',
"cout":10 ,
"type":"unlock_class",
"cible":'Shadow Assassin',
"valeur":1 ,
"prerequis":["atk1","def1"],
},

# New advanced classes
"class_berserker":{
"name":"Unlock Berserker",
"description":"Allows you to choose the class Berserker at the start of the run.",
"cout":9 ,
"type":"unlock_class",
"cible":"Berserker",
"valeur":1 ,
"prerequis":["atk1"],
},
'class_barde':{
"name":"Unlock Bard",
"description":"Allows you to choose the class Bard at the start of the run.",
"cout":8 ,
"type":"unlock_class",
"cible":"Bard",
"valeur":1 ,
"prerequis":["mana1"],
},
'class_moine':{
"name":"Unlock Monk",
"description":"Allows you to choose the class Monk at the start of the run.",
"cout":9 ,
"type":"unlock_class",
"cible":"Monk",
"valeur":1 ,
"prerequis":["def1"],
},
'class_invocateur':{
"name":"Unlock Summoner",
"description":"Allows you to choose the class Summoner at the start of the run.",
"cout":10 ,
"type":"unlock_class",
"cible":"Summoner",
"valeur":1 ,
"prerequis":["mana1","hp1"],
},
}


# ======================================================
# Meta-progression
# ======================================================
@dataclass 
class Meta :
    essence :int =0 
    hp_bonus :int =0 
    attack_bonus :int =0 
    defense_bonus :int =0 
    mana_bonus :int =0 
    or_start :int =0 
    potions_start :int =0 
    bonus_chance_shop :int =0 
    bonus_chance_mystere :int =0 
    achievements :Dict [str ,Dict ]=field (default_factory =dict )
    classes_unlocked :List [str ]=field (default_factory =lambda :['Warrior',"Mage","Rogue"])
    talents_unlocked :List [str ]=field (default_factory =list )
    filename :Optional [str ]=None 

    @classmethod 
    def choose_slot (cls )->"Meta":
        while True :
            clear_console ()
            print (COLOR_CYAN +"===== SAVE SLOT SELECTION ====="+COLOR_RESET )
            print ("1) Slot 1")
            print ("2) Slot 2")
            print ("3) Slot 3")
            choix =input (">>").strip ()
            if choix in ("1","2","3"):
                filename =f"meta_save_slot{choix }.json"
                return cls .load (filename )
            print ("Invalid choice.")
            wait_for_enter ()

    @classmethod 
    def load (cls ,filename :str )->"Meta":
        if not os .path .exists (filename ):
            meta =cls ()
            meta .filename =filename 
            return meta 
        try :
            with open (filename ,'r',encoding ='utf-8')as f :
                data =json .load (f )
        except Exception :
            meta =cls ()
            meta .filename =filename 
            return meta 
        meta =cls (
        essence =data .get ("essence",0 ),
        hp_bonus =data .get ("hp_bonus",0 ),
        attack_bonus =data .get ("attack_bonus",0 ),
        defense_bonus =data .get ("defense_bonus",0 ),
        mana_bonus =data .get ("mana_bonus",0 ),
        or_start =data .get ("gold_start",0 ),
        potions_start =data .get ("potions_start",0 ),
        bonus_chance_shop =data .get ('bonus_chance_shop',0 ),
        bonus_chance_mystere =data .get ('bonus_chance_mystery',0 ),
        achievements =data .get ("succes",{}),
        classes_unlocked =data .get ("classes_debloquees",['Warrior',"Mage","Rogue"]),
        talents_unlocked =data .get ("talents_debloques",[]),
        filename =filename ,
        )
        return meta 

    def save (self )->None :
        if not self .filename :
            return 
        data ={
        "essence":self .essence ,
        "hp_bonus":self .hp_bonus ,
        "attack_bonus":self .attack_bonus ,
        "defense_bonus":self .defense_bonus ,
        "mana_bonus":self .mana_bonus ,
        "gold_start":self .or_start ,
        "potions_start":self .potions_start ,
        'bonus_chance_shop':self .bonus_chance_shop ,
        'bonus_chance_mystery':self .bonus_chance_mystere ,
        "succes":self .achievements ,
        "classes_debloquees":self .classes_unlocked ,
        "talents_debloques":self .talents_unlocked ,
        }
        try :
            with open (self .filename ,'w',encoding ='utf-8')as f :
                json .dump (data ,f ,ensure_ascii =False ,indent =2 )
        except Exception :
            pass 

    def debloquer_achievements (self ,cle :str ,description :Optional [str ]=None )->bool :
        if cle in self .achievements :
            return False 
        if cle =="premier_boss":
            self .attack_bonus +=1 
            desc_defaut ="Premier boss vaincu (+1 ATK base)"
        elif cle =="tueur_de_monstres":
            self .hp_bonus +=5 
            desc_defaut ='A tue au moins 20 ennemis en run (+5 HP base)'
        elif cle =='explorateur':
            self .or_start +=5 
            desc_defaut ='A atteint au moins floor 10 (+5 gold at the start chaque run)'
        else :
            desc_defaut =cle 
        self .achievements [cle ]={"description":description or desc_defaut }
        self .save ()
        print (">>> SUCCES DEBLOQUE :"+self .achievements [cle ]["description"]+"<<<")
        return True 


        # ======================================================
        # Entities
        # ======================================================
@dataclass 
class Status :
    poison :int =0 
    burn :int =0 
    stun :int =0 


@dataclass 
class Entity :
    name :str 
    hp :int 
    hp_max :int 
    attack :int 
    defense :int 
    mana :int =0 
    mana_max :int =0 
    status :Status =field (default_factory =Status )

    def est_vivant (self )->bool :
        return self .hp >0 

    def barre_vie (self ,longueur :int =20 )->str :
        if self .hp_max <=0 :
            return "["+"-"*longueur +"]"
        ratio =max (0 ,min (1 ,self .hp /self .hp_max ))
        rempli =int (ratio *longueur )
        vide =longueur -rempli 
        return "["+"#"*rempli +"-"*vide +"]"

    def appliquer_status (self )->bool :
        mort =False 
        if self .status .poison >0 :
            deg =max (1 ,int (self .hp_max *0.07 ))
            self .hp -=deg 
            self .status .poison -=1 
            print (f"{self .name } suffers from poison and loses {deg } hp !")
            if self .hp <=0 :
                mort =True 
        if (not mort )and self .status .burn >0 :
            deg =max (1 ,int (self .hp_max *0.09 ))
            self .hp -=deg 
            self .status .burn -=1 
            print (f"{self .name } is burning and loses {deg } hp !")
            if self .hp <=0 :
                mort =True 
        return mort 

    def est_stun (self )->bool :
        if self .status .stun >0 :
            self .status .stun -=1 
            return True 
        return False 


@dataclass 
class Player (Entity ):
    player_class :str =""
    pouvoir :str =""
    level :int =1 
    xp :int =0 
    xp_next :int =20 
    potions :int =0 
    gold :int =0 
    floors_cleared :int =0 
    enemies_killed :int =0 
    boss_killed :int =0 
    or_gagne_total :int =0 
    weapon :Weapon =field (default_factory =lambda :WEAPONS [0 ])
    weapons :List [Weapon ]=field (default_factory =list )
    relic :Optional [Relic ]=None 
    invocation_squelette_tours :int =0 
    bonus_critique :float =0.0 

    def atq_effective (self )->int :
        atk =self .attack 
        if self .weapon :
            atk +=self .weapon .atk_bonus 
        if self .relic :
            atk +=self .relic .atk_bonus 
        return atk 

    def def_effective (self )->int :
        df =self .defense 
        if self .relic :
            df +=self .relic .def_bonus 
        return df 

    def crit_chance (self )->float :
        base =0.05 
        if self .weapon :
            base +=self .weapon .crit_bonus 
        if self .relic :
            base +=self .relic .crit_bonus 
        base +=self .bonus_critique 
        return min (0.8 ,base )

    def lifesteal (self )->float :
        return self .relic .lifesteal if self .relic else 0.0 


@dataclass 
class Enemy (Entity ):
    gold_range :Tuple [int ,int ]=(0 ,0 )
    xp_range :Tuple [int ,int ]=(0 ,0 )
    element_resistances :Dict [str ,float ]=field (default_factory =dict )
    element_weaknesses :Dict [str ,float ]=field (default_factory =dict )


    # ======================================================
    # Game class
    # ======================================================
class Game :
    def __init__ (self ):
        self .meta :Meta =Meta .choose_slot ()
        self .player :Optional [Player ]=None 

        # ------------------ Creation joueur ------------------
    def creer_player (self )->Player :
        clear_console ()
        print (COLOR_MAGENTA +"="*30 +COLOR_RESET )
        print (COLOR_BOLD +'ROGUELIKE CATACOMBES'+COLOR_RESET )
        print ("Edition Roguelike ASCII")
        print (COLOR_MAGENTA +"="*30 +COLOR_RESET )
        print ()
        name =input ("Entre name your heros :")or "Heros"
        print ()

        # Construire liste classes debloquees
        classes_disponibles :Dict [str ,Dict ]={}
        index =1 
        for _ ,infos in PLAYER_CLASSES .items ():
            if infos ["name"]in self .meta .classes_unlocked :
                classes_disponibles [str (index )]=infos 
                index +=1 

        if not classes_disponibles :
        # Securite : si jamais aucune classe n'est debloquee, on autorise trois base
            for _ ,infos in PLAYER_CLASSES .items ():
                if infos ["name"]in ('Warrior',"Mage","Rogue"):
                    key =str (len (classes_disponibles )+1 )
                    classes_disponibles [key ]=infos 

        print ("Choisis classe :")
        for key ,infos in classes_disponibles .items ():
            print (
            f" {key }) {infos ['name']} "
            f"hp:{infos ['hp']} ATQ:{infos ['attack']} "
            f"DEF:{infos ['defense']} Mana:{infos ['mana']}"
            )

        choix =None 
        while choix not in classes_disponibles :
            choix =input ("Your choice:").strip ()
        base =classes_disponibles [choix ]

        hp_base =base ['hp']+self .meta .hp_bonus 
        mana_base =base ['mana']+self .meta .mana_bonus 
        attack_base =base ['attack']+self .meta .attack_bonus 
        defense_base =base ['defense']+self .meta .defense_bonus 
        weapon_base =WEAPONS [0 ]

        player =Player (
        name =name ,
        player_class =base ['name'],
        hp =hp_base ,
        hp_max =hp_base ,
        attack =attack_base ,
        defense =defense_base ,
        mana =mana_base ,
        mana_max =mana_base ,
        status =Status (),
        pouvoir =base ['power'],
        level =1 ,
        xp =0 ,
        xp_next =20 ,
        potions =2 +self .meta .potions_start ,
        gold =self .meta .or_start ,
        floors_cleared =0 ,
        enemies_killed =0 ,
        boss_killed =0 ,
        or_gagne_total =0 ,
        weapon =weapon_base ,
        weapons =[weapon_base ],
        relic =None ,
        invocation_squelette_tours =0 ,
        bonus_critique =0.0 ,
        )

        clear_console ()
        print (f"Bienvenue, {player .name } the {player .player_class } !")
        print ("catacombes t'attendent...")
        wait_for_enter ()
        self .player =player 
        return player 

        # ------------------ Affichage ------------------
    def afficher_status (self ,entite :Entity ,est_player :bool =True )->None :
        s =entite .status 
        actifs =[]
        if s .poison >0 :
            actifs .append (f"Poison({s .poison })")
        if s .burn >0 :
            actifs .append (f"Burn({s .burn })")
        if s .stun >0 :
            actifs .append (f"Stun({s .stun })")
        if actifs :
            target ="Toi"if est_player else "Lui"
            print (f"Statuts {target } : "+",".join (actifs ))

    def afficher_etat_player (self )->None :
        j =self .player 
        if j is None :
            return 
        ratio_hp =j .hp /j .hp_max if j .hp_max >0 else 0 
        ratio_mana =j .mana /j .mana_max if j .mana_max >0 else 0 
        if ratio_hp >=0.6 :
            col_hp =COLOR_GREEN 
        elif ratio_hp >=0.3 :
            col_hp =COLOR_YELLOW 
        else :
            col_hp =COLOR_RED 
        if ratio_mana >=0.6 :
            col_mana =COLOR_CYAN 
        elif ratio_mana >=0.3 :
            col_mana =COLOR_BLUE 
        else :
            col_mana =COLOR_MAGENTA 
        print (COLOR_MAGENTA +"="*50 +COLOR_RESET )
        print (COLOR_CYAN +COLOR_BOLD +f"Hero: {j .name } the {j .player_class } // Level {j .level }"+COLOR_RESET )
        print (col_hp +"HP :"+COLOR_RESET ,col_hp +j .barre_vie ()+COLOR_RESET ,f"{j .hp }/{j .hp_max }")
        print (col_mana +"mana :"+COLOR_RESET ,col_mana +j .barre_vie ()+COLOR_RESET ,f"{j .mana }/{j .mana_max }")
        print (f"ATQ : {j .attack } DEF : {j .defense }")
        weapon_name =j .weapon .name if j .weapon else "Aucune"
        relic_name =j .relic .name if j .relic else "Aucune"
        print (f"Arme : {weapon_name }")
        print (f"Relique: {relic_name }")
        print (f"Potions : {j .potions } // Gold : {j .gold }")
        if j .player_class =="Necromancer"and j .invocation_squelette_tours >0 :
            print (f"Invocation : Squelette actif ({j .invocation_squelette_tours } tour(s) restant(s))")
        self .afficher_status (j ,est_player =True )
        print (COLOR_MAGENTA +"="*50 +COLOR_RESET )

        # ------------------ Combat ------------------
    @staticmethod 
    def calculer_degats (base_atq :int ,base_def :int )->int :
        base =base_atq -base_def 
        variance =random .randint (-1 ,2 )
        return max (1 ,base +variance )

    def appliquer_degats_player (self ,degats :int )->int :
        j =self .player 
        if j is None :
            return 0 
        effective_def =j .def_effective ()
        dodge_chance =min (0.25 ,0.02 *effective_def )
        if random .random ()<dodge_chance :
            print ("You deftly dodge the attack!")
            return 0 
        j .hp -=degats 
        return degats 

        # --------- Systeme elementaire ---------
    def appliquer_element (self ,degats :int ,enemy :Enemy ,element :Optional [str ])->int :
        if element is None :
            return degats 
        mult =1.0 
        if element in enemy .element_resistances :
            mult *=enemy .element_resistances [element ]
        if element in enemy .element_weaknesses :
            mult *=enemy .element_weaknesses [element ]
        deg =int (degats *mult )
        if mult >1.0 :
            print (COLOR_YELLOW +"C'est super efficace !"+COLOR_RESET )
        elif mult <1.0 :
            print (COLOR_BLUE +"The enemy resists this element..."+COLOR_RESET )
        return max (1 ,deg )

    def attack_player_sur_enemy (self ,enemy :Enemy ,base_atq :int ,element :str ="physique")->int :
        j =self .player 
        if j is None :
            return 0 
        degats =self .calculer_degats (base_atq ,enemy .defense )
        if random .random ()<j .crit_chance ():
            degats =int (degats *1.8 )
            print (COLOR_YELLOW +"COUP CRITIQUE !!"+COLOR_RESET )
        degats =self .appliquer_element (degats ,enemy ,element )
        ls =j .lifesteal ()
        if ls >0 :
            soin =int (degats *ls )
            if soin >0 :
                j .hp =min (j .hp_max ,j .hp +soin )
                print (f"Your relique draine {soin } HP from the enemy.")
        enemy .hp -=degats 
        if j .weapon and j .weapon .name =="Twin Daggers":
            if random .random ()<0.35 :
                enemy .status .poison +=2 
                print (COLOR_GREEN +"Your daggers inject poison into the enemy's veins!"+COLOR_RESET )
        return degats 

        # ------------------ Tours combat ------------------
    def tour_player (self ,enemy :Enemy )->str :
        j =self .player 
        if j is None :
            return 'mort'
        mort =j .appliquer_status ()
        if mort :
            print ("effets statut ont eu raison toi...")
            wait_for_enter ()
            return 'mort'
        if j .est_stun ():
            print ("You are stunned and cannot act!")
            wait_for_enter ()
            return "stun"
        while True :
            print ()
            print ("Your action :")
            print ("1) Attaquer")
            print ("2) Defendre")
            print (f" 3) Special power ({j .pouvoir })")
            print ("4) Use a potion")
            choix =input (">>").strip ()
            if choix =="1":
                atq_eff =j .atq_effective ()
                degats =self .attack_player_sur_enemy (enemy ,atq_eff ,element ="physique")
                if j .player_class =="Rogue"and random .random ()<0.25 :
                    enemy .status .poison +=3 
                    print ("You poison the enemy!")
                elif j .player_class =="Mage"and random .random ()<0.25 :
                    enemy .status .burn +=2 
                    print ("You set the enemy on fire!")
                clear_console ()
                print (f"You strike {enemy .name } and deal {degats } damage!")
                return "attack"
            if choix =="2":
                clear_console ()
                print ("You te prepares a encaisser prochain coup (DEF x2 ce tour).")
                return "defense"
            if choix =="3":
                res =self .choisir_pouvoir_et_utiliser (j ,enemy )
                if res is None :
                    continue 
                msg ,degats =res 
                clear_console ()
                print (msg )
                if degats >0 :
                    print (f"You infliges {degats } damage to {enemy .name } !")
                return "power"
            if choix =="4":
                if j .potions <=0 :
                    clear_console ()
                    print ("You have no potions left...")
                    continue 
                self .utiliser_potion ()
                return "potion"
            print ("Invalid choice.")
            wait_for_enter ()

            # Sous-menu pouvoirs par classe
    def choisir_pouvoir_et_utiliser (self ,j :Player ,enemy :Enemy ):
    # Necromancer : 2 sorts
        if j .player_class =="Necromancer":
            while True :
                clear_console ()
                print ('=== Sorts Necromancer ===')
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print ("1) Soul Drain (5 mana)")
                print ('2) Invocation squelette (10 mana)')
                print ("0) Annuler")
                choix =input (">>").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cost =5 
                    if j .mana <cost :
                        print ('Not enough mana for Soul Drain!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =1 )
                if choix =="2":
                    cost =10 
                    if j .mana <cost :
                        print ('Not enough mana for Invocation squelette!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =2 )
                print ("Invalid choice.")
                wait_for_enter ()

                # Warrior : 2 techniques
        if j .player_class =='Warrior':
            while True :
                clear_console ()
                print ('=== Techniques Warrior ===')
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print ("1) Coup puissant (3 mana)")
                print ("2) Fracas bouclier (4 mana)")
                print ("0) Annuler")
                choix =input (">>").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cost =3 
                    if j .mana <cost :
                        print ('Not enough mana for Coup puissant!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =1 )
                if choix =="2":
                    cost =4 
                    if j .mana <cost :
                        print ('Not enough mana for Fracas bouclier!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =2 )
                print ("Invalid choice.")
                wait_for_enter ()

                # Mage : 2 sorts
        if j .player_class =="Mage":
            while True :
                clear_console ()
                print ("=== Arcanes Mage ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print ("1) Boule feu (5 mana)")
                print ("2) Nova glace (6 mana)")
                print ("0) Annuler")
                choix =input (">>").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cost =5 
                    if j .mana <cost :
                        print ('Not enough mana for Boule feu!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =1 )
                if choix =="2":
                    cost =6 
                    if j .mana <cost :
                        print ('Not enough mana for Nova glace!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =2 )
                print ("Invalid choice.")
                wait_for_enter ()

                # Rogue : 2 arts furtifs
        if j .player_class =="Rogue":
            while True :
                clear_console ()
                print ("=== Stealth arts Rogue ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print ("1) attack furtive (3 mana)")
                print ("2) Pluie dagues (4 mana)")
                print ("0) Annuler")
                choix =input (">>").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cost =3 
                    if j .mana <cost :
                        print ('Not enough mana for attack furtive!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =1 )
                if choix =="2":
                    cost =4 
                    if j .mana <cost :
                        print ('Not enough mana for Pluie dagues!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =2 )
                print ("Invalid choice.")
                wait_for_enter ()

                # Paladin : 2 pouvoirs sacres
        if j .player_class =="Paladin":
            while True :
                clear_console ()
                print ('=== Pouvoirs Paladin ===')
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print ("1) Sacred light (4 mana)")
                print ("2) Benediction protectrice (5 mana)")
                print ("0) Annuler")
                choix =input (">>").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cost =4 
                    if j .mana <cost :
                        print ('Not enough mana for Sacred light!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =1 )
                if choix =="2":
                    cost =5 
                    if j .mana <cost :
                        print ('Not enough mana for Benediction protectrice!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =2 )
                print ("Invalid choice.")
                wait_for_enter ()

                # Ranger : 2 tirs
        if j .player_class =="Ranger":
            while True :
                clear_console ()
                print ("=== Techniques Ranger ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print ("1) Tir precis (3 mana)")
                print ("2) Tir multiple (4 mana)")
                print ("0) Annuler")
                choix =input (">>").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cost =3 
                    if j .mana <cost :
                        print ('Not enough mana for Tir precis!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =1 )
                if choix =="2":
                    cost =4 
                    if j .mana <cost :
                        print ('Not enough mana for Tir multiple!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =2 )
                print ("Invalid choice.")
                wait_for_enter ()

                # Shadow Assassin : 2 arts shadows
        if j .player_class =='Shadow Assassin':
            while True :
                clear_console ()
                print ('=== Shadow arts (Assassin) ===')
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print ('1) Lame spectrale (4 mana)')
                print ("2) Vanish into the Shadows (5 mana)")
                print ("0) Annuler")
                choix =input (">>").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cost =4 
                    if j .mana <cost :
                        print ('Not enough mana for Lame spectrale!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =1 )
                if choix =="2":
                    cost =5 
                    if j .mana <cost :
                        print ('Not enough mana for Vanish into the Shadows!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =2 )
                print ("Invalid choice.")
                wait_for_enter ()

                # Berserker : 2 attaques sauvages
        if j .player_class =="Berserker":
            while True :
                clear_console ()
                print ("=== Rages Berserker ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print ("1) Enraged Strike (3 mana)")
                print ("2) Rage incontrolable (0 mana)")
                print ("0) Annuler")
                choix =input (">>").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cost =3 
                    if j .mana <cost :
                        print ('Not enough mana for Enraged Strike!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =1 )
                if choix =="2":
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =2 )
                print ("Invalid choice.")
                wait_for_enter ()

                # Bard : 2 chants
        if j .player_class =="Bard":
            while True :
                clear_console ()
                print ("=== Chants Bard ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print ("1) Chant bravoure (4 mana)")
                print ("2) Soothing Ballad (5 mana)")
                print ("0) Annuler")
                choix =input (">>").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cost =4 
                    if j .mana <cost :
                        print ('Not enough mana for Chant bravoure!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =1 )
                if choix =="2":
                    cost =5 
                    if j .mana <cost :
                        print ('Not enough mana for Soothing Ballad!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =2 )
                print ("Invalid choice.")
                wait_for_enter ()

                # Monk : 2 techniques spirituelles
        if j .player_class =="Monk":
            while True :
                clear_console ()
                print ("=== Spiritual martial arts (Monk) ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print ("1) Paume vibrante (3 mana)")
                print ("2) Deep Meditation (4 mana)")
                print ("0) Annuler")
                choix =input (">>").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cost =3 
                    if j .mana <cost :
                        print ('Not enough mana for Paume vibrante!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =1 )
                if choix =="2":
                    cost =4 
                    if j .mana <cost :
                        print ('Not enough mana for Deep Meditation!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =2 )
                print ("Invalid choice.")
                wait_for_enter ()

                # Summoner : 2 incantations
        if j .player_class =="Summoner":
            while True :
                clear_console ()
                print ("=== Incantations l'Summoner ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print ("1) Salve astrale (6 mana)")
                print ("2) Rempart esprits (8 mana)")
                print ("0) Annuler")
                choix =input (">>").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cost =6 
                    if j .mana <cost :
                        print ('Not enough mana for Salve astrale!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =1 )
                if choix =="2":
                    cost =8 
                    if j .mana <cost :
                        print ('Not enough mana for Rempart esprits!')
                        wait_for_enter ()
                        continue 
                    j .mana -=cost 
                    return self .utiliser_pouvoir_special (j ,enemy ,ability_id =2 )
                print ("Invalid choice.")
                wait_for_enter ()

        return None 

    def utiliser_pouvoir_special (self ,j :Player ,enemy :Enemy ,ability_id :int =1 ):
    # Warrior
        if j .player_class =='Warrior':
            if ability_id ==1 :
                atq_eff =j .atq_effective ()+4 
                degats =self .attack_player_sur_enemy (enemy ,atq_eff ,element ="physique")
                if random .random ()<0.35 :
                    enemy .status .stun +=1 
                    print ("Your Power Strike stuns the enemy!")
                return "Coup puissant !!",degats 
            if ability_id ==2 :
                degats =self .calculer_degats (j .atq_effective (),enemy .defense )
                degats =self .appliquer_element (degats ,enemy ,"physique")
                enemy .hp -=degats 
                enemy .defense =max (0 ,enemy .defense -2 )
                return "Shield Bash! You reduce the enemy's defense.",degats 

                # Mage
        if j .player_class =="Mage":
            if ability_id ==1 :
                base =j .attack +random .randint (6 ,10 )
                degats =base 
                if random .random ()<j .crit_chance ():
                    degats =int (degats *1.8 )
                    msg ="Boule feu CRITIQUE !!"
                else :
                    msg ='You lances enorme boule feu !!'
                degats =self .appliquer_element (degats ,enemy ,"feu")
                enemy .hp -=degats 
                enemy .status .burn +=3 
                print ("The enemy is set ablaze by your magic!")
                ls =j .lifesteal ()
                if ls >0 :
                    soin =int (degats *ls )
                    if soin >0 :
                        j .hp =min (j .hp_max ,j .hp +soin )
                return msg ,degats 
            if ability_id ==2 :
                base =j .attack +random .randint (4 ,7 )
                degats =base 
                degats =self .appliquer_element (degats ,enemy ,"glace")
                enemy .hp -=degats 
                if random .random ()<0.4 :
                    enemy .status .stun +=1 
                    msg ="Ice Nova! The enemy is frozen in place!"
                else :
                    msg ="Ice Nova! The enemy is slowed by the cold."
                enemy .attack =max (1 ,enemy .attack -1 )
                return msg ,degats 

                # Rogue
        if j .player_class =="Rogue":
            if ability_id ==1 :
                atq_eff =j .atq_effective ()+2 
                degats =self .attack_player_sur_enemy (enemy ,atq_eff ,element ="physique")
                if random .random ()<0.4 :
                    enemy .status .poison +=2 
                    print ("Your Sneak Attack poisons the enemy!")
                if random .random ()<0.2 :
                    enemy .status .stun +=1 
                    print ("You surprise the enemy; it is stunned!")
                return "attack furtive ! You vises point faible.",degats 
            if ability_id ==2 :
                total =0 
                for _ in range (3 ):
                    d =self .calculer_degats (max (1 ,j .atq_effective ()-1 ),enemy .defense )
                    d =self .appliquer_element (d ,enemy ,"physique")
                    enemy .hp -=d 
                    total +=d 
                enemy .status .poison +=1 
                enemy .status .burn +=1 
                return "Pluie dagues ! You laceres your adversaire tous cotes.",total 

                # Paladin
        if j .player_class =="Paladin":
            if ability_id ==1 :
                soin =random .randint (10 ,16 )
                j .hp =min (j .hp_max ,j .hp +soin )
                degats =self .calculer_degats (j .atq_effective (),enemy .defense )
                degats =self .appliquer_element (degats ,enemy ,"sacre")
                enemy .hp -=degats 
                return f"Sacred Light! You heal for {soin } hp and deal {degats } damage.",degats 
            if ability_id ==2 :
                soin =random .randint (8 ,14 )
                j .hp =min (j .hp_max ,j .hp +soin )
                j .defense +=2 
                return 'Benediction protectrice ! You renforces your defense et heal your blessures.',0 

                # Ranger
        if j .player_class =="Ranger":
            if ability_id ==1 :
                base =j .atq_effective ()+random .randint (2 ,5 )
                degats =base 
                crit =j .crit_chance ()+0.15 
                if random .random ()<crit :
                    degats =int (degats *2.2 )
                    msg ="Tir precis CRITIQUE !!"
                else :
                    msg ='You decoches fleche mortelle.'
                degats =self .appliquer_element (degats ,enemy ,"physique")
                enemy .hp -=degats 
                return msg ,degats 
            if ability_id ==2 :
                d1 =self .calculer_degats (max (1 ,j .atq_effective ()-1 ),enemy .defense )
                d2 =self .calculer_degats (max (1 ,j .atq_effective ()-1 ),enemy .defense )
                d1 =self .appliquer_element (d1 ,enemy ,"physique")
                d2 =self .appliquer_element (d2 ,enemy ,"physique")
                total =d1 +d2 
                enemy .hp -=total 
                return "Tir multiple ! Deux fleches frappent leur cible.",total 

                # Necromancer
        if j .player_class =="Necromancer":
            if ability_id ==1 :
                base =j .attack +random .randint (4 ,8 )
                degats =base 
                degats =self .appliquer_element (degats ,enemy ,"shadow")
                enemy .hp -=degats 
                soin =int (degats *0.7 )
                j .hp =min (j .hp_max ,j .hp +soin )
                return f"Soul Drain ! You voles {soin } hp a {enemy .name }.",degats 
            if ability_id ==2 :
                if j .invocation_squelette_tours >0 :
                    return 'You as deja squelette invoque !',0 
                j .invocation_squelette_tours =3 
                return 'You invoques squelette catacombes combattre a your cotes !',0 

                # Shadow Assassin
        if j .player_class =='Shadow Assassin':
            if ability_id ==1 :
                base =j .atq_effective ()+random .randint (3 ,6 )
                degats =self .calculer_degats (base ,enemy .defense )
                if random .random ()<j .crit_chance ()+0.1 :
                    degats =int (degats *2.0 )
                    msg ='Lame spectrale CRITIQUE !'
                else :
                    msg ='You strike depuis tenebres your lame spectrale.'
                degats =self .appliquer_element (degats ,enemy ,"shadow")
                enemy .hp -=degats 
                return msg ,degats 
            if ability_id ==2 :
                j .bonus_critique +=0.15 
                j .defense +=1 
                return "You melt into the shadows; your next strikes will be deadlier.",0 

                # Berserker
        if j .player_class =="Berserker":
            if ability_id ==1 :
                base =j .atq_effective ()+random .randint (4 ,7 )
                degats =self .calculer_degats (base ,enemy .defense )
                degats =self .appliquer_element (degats ,enemy ,"physique")
                enemy .hp -=degats 
                recul =max (1 ,int (degats *0.15 ))
                j .hp =max (1 ,j .hp -recul )
                return f"Enraged Strike ! You infliges {degats } damage mais subis {recul } HP recoil.",degats 
            if ability_id ==2 :
                j .attack +=2 
                j .defense =max (0 ,j .defense -1 )
                j .hp =min (j .hp_max ,j .hp +5 )
                return 'Rage incontrolable ! ATK +2, DEF -1, you regagnes peu HP.',0 

                # Bard
        if j .player_class =="Bard":
            if ability_id ==1 :
                j .attack +=1 
                j .defense +=1 
                return 'Chant bravoure ! Your statistiques offensives et defensives augmentent legerement.',0 
            if ability_id ==2 :
                soin =random .randint (10 ,16 )
                j .hp =min (j .hp_max ,j .hp +soin )
                j .status .poison =0 
                j .status .burn =0 
                j .status .stun =0 
                return f"Soothing Ballad ! You recover {soin } hp et your status ailments disappear.",0 

                # Monk
        if j .player_class =="Monk":
            if ability_id ==1 :
                base =j .atq_effective ()+random .randint (2 ,4 )
                degats =self .calculer_degats (base ,enemy .defense )
                degats =self .appliquer_element (degats ,enemy ,"sacre")
                enemy .hp -=degats 
                if random .random ()<0.35 :
                    enemy .status .stun +=1 
                    return "Vibrating Palm! The enemy is hit and stunned.",degats 
                return "Paume vibrante ! You strike points vitaux your adversaire.",degats 
            if ability_id ==2 :
                soin =random .randint (8 ,12 )
                mana_gain =random .randint (5 ,8 )
                j .hp =min (j .hp_max ,j .hp +soin )
                j .mana =min (j .mana_max ,j .mana +mana_gain )
                j .status .poison =max (0 ,j .status .poison -1 )
                j .status .burn =max (0 ,j .status .burn -1 )
                return f"Deep Meditation ! You recover {soin } hp et {mana_gain } mana.",0 

                # Summoner
        if j .player_class =="Summoner":
            if ability_id ==1 :
            # Salve astrale : damage magiques multi-elements
                base =j .attack +random .randint (8 ,14 )
                degats =self .appliquer_element (base ,enemy ,"shadow")
                enemy .hp -=degats 
                return "Salve astrale ! pluie d'energie hits your enemy.",degats 
            if ability_id ==2 :
            # Rempart esprits : bouclier defensif
                j .defense +=2 
                j .hp =min (j .hp_max ,j .hp +6 )
                return "Rempart esprits ! Your defense augmente et esprits te soignent peu.",0 

                # fallback
        degats =self .attack_player_sur_enemy (enemy ,j .atq_effective (),element ="physique")
        return 'Pouvoir mysterieux...',degats 

    def utiliser_potion (self )->None :
        j =self .player 
        if j is None :
            return 
        while True :
            clear_console ()
            print (f"You as {j .potions } potion(s).")
            print ("Which potion would you like to use?")
            print ("1) Healing potion (beaucoup HP)")
            print ("2) potion mana (beaucoup mana)")
            print ("3) potion mixte ( peu HP et peu mana)")
            choix_p =input (">>").strip ()
            if choix_p =="1":
                soin =random .randint (14 ,20 )
                j .hp =min (j .hp_max ,j .hp +soin )
                j .potions -=1 
                clear_console ()
                print (f"You drink a healing potion et recover {soin } hp !")
                break 
            if choix_p =="2":
                mana_gain =random .randint (10 ,16 )
                j .mana =min (j .mana_max ,j .mana +mana_gain )
                j .potions -=1 
                clear_console ()
                print (f"You drink a mana potion et recover {mana_gain } mana !")
                break 
            if choix_p =="3":
                soin =random .randint (7 ,11 )
                mana_gain =random .randint (5 ,9 )
                j .hp =min (j .hp_max ,j .hp +soin )
                j .mana =min (j .mana_max ,j .mana +mana_gain )
                j .potions -=1 
                clear_console ()
                print (f"You drink a mixed potion et recover {soin } hp et {mana_gain } mana !")
                break 
            print ("Invalid potion choice.")
            wait_for_enter ()

    def squelette_attack (self ,enemy :Enemy )->None :
        j =self .player 
        if j is None :
            return 
        if j .invocation_squelette_tours <=0 :
            return 
        base_atq =max (1 ,j .attack -1 )
        degats =self .calculer_degats (base_atq ,enemy .defense )
        degats =self .appliquer_element (degats ,enemy ,"physique")
        enemy .hp -=degats 
        print (f"Your summoned skeleton hits {enemy .name } and deals {degats } damage!")
        j .invocation_squelette_tours -=1 
        if j .invocation_squelette_tours <=0 :
            print ("Your squelette se desagrege en poussiere d'os...")

    def enemy_competence_speciale (self ,enemy :Enemy )->None :
        j =self .player 
        if j is None :
            return 
            # Boss plus dangereux
        if "Seigneur"in enemy .name or "Champion"in enemy .name or "Reine"in enemy .name :
            print (COLOR_RED +f"{enemy .name } triggers an ULTIMATE SKILL !"+COLOR_RESET )
            degats_base =int (enemy .attack *1.8 )
            degats =self .appliquer_degats_player (degats_base )
            if degats >0 :
                print (f"You subis {degats } devastating damage !")
            if random .random ()<0.4 :
                j .status .stun +=1 
                print ("puissance coup t'etourdit !")
            return 
            # Enemies normaux : buff ou debuff
        choix =random .choice (["rage","curse"])
        if choix =="rage":
            print (f"{enemy .name } entre en rage ! Son attaque augmente.")
            enemy .attack +=2 
        else :
            print (f"{enemy .name } whispers a curse...")
            j .attack =max (1 ,j .attack -1 )
            print ("You te sens affaibli : ATK -1.")

            #------------------ attack enemy ------------------
    def tour_enemy (self ,enemy :Enemy ,action_player :str )->None :
        j =self .player 
        if j is None :
            return 
        mort =enemy .appliquer_status ()
        if mort :
            return 
        if enemy .est_stun ():
            print (f"{enemy .name } is stunned and cannot act !")
            return 
            # chance competence speciale
        if random .random ()<0.20 :
            self .enemy_competence_speciale (enemy )
            return 
        effective_def =j .def_effective ()
        if action_player =="defense":
            effective_def *=2 
        degats_base =self .calculer_degats (enemy .attack ,effective_def )
        degats =self .appliquer_degats_player (degats_base )
        if degats >0 :
            print (f"{enemy .name } attacks you and deals {degats } damage!")
        if random .random ()<0.15 :
            j .status .poison +=2 
            print ("The enemy's attack poisons you!")
        elif random .random ()<0.15 :
            j .status .burn +=2 
            print ("The enemy's attack burns you!")

            # ------------------ Cards ------------------
    def tirer_cartes (self ,n :int =3 )->List [Card ]:
        cartes :List [Card ]=[]
        j =self .player 
        for _ in range (n ):
            r =random .random ()
            if r <0.60 :
                rarete_visee ="Common"
            elif r <0.85 :
                rarete_visee ="Rare"
            elif r <0.97 :
                rarete_visee ="Epic"
            else :
                rarete_visee ="Legendary"
            cand =[c for c in CARDS_POOL if c .rarete ==rarete_visee ]
            if j is not None :
                cand =[c for c in cand if (c .classes_autorisees is None or j .player_class in c .classes_autorisees )]
            if not cand :
            # Fallback : cartes generiques cette rarete, ou tout pool
                cand =[c for c in CARDS_POOL if c .rarete ==rarete_visee and c .classes_autorisees is None ]or CARDS_POOL 
            cartes .append (random .choice (cand ))
        return cartes 

    def appliquer_carte (self ,carte :Card )->None :
        j =self .player 
        if j is None :
            return 
        j .hp_max +=carte .bonus_hp_max 
        j .attack +=carte .bonus_attack 
        j .defense +=carte .bonus_defense 
        j .mana_max +=carte .bonus_mana_max 
        j .potions +=carte .bonus_potions 
        j .bonus_critique +=carte .bonus_critique 
        if carte .bonus_hp_max >0 :
            j .hp +=carte .bonus_hp_max 
        j .hp =min (j .hp_max ,j .hp )
        j .mana =min (j .mana_max ,j .mana )
        #------------------ cartes recompenses ------------------
    def choix_cartes_apres_combat (self )->None :
        j =self .player 
        if j is None :
            return 
        cartes =self .tirer_cartes (3 )
        while True :
            clear_console ()
            print ("===== REWARD: CHOOSE A CARD =====")
            for i ,c in enumerate (cartes ,start =1 ):
                restriction =""
                if c .classes_autorisees is not None :
                    restriction ="(specifique)"
                print (f" {i }) [{c .rarete }] {c .name }{restriction } - {c .description }")
            print ("0) Ne prendre aucune carte (not recommande)")
            choix =input ("Choisis carte (0-3) :").strip ()
            if choix =="0":
                print ('You ignores ces pouvoirs... choice risque.')
                wait_for_enter ()
                return 
            try :
                idx =int (choix )-1 
            except ValueError :
                print ("Invalid choice.")
                wait_for_enter ()
                continue 
            if 0 <=idx <len (cartes ):
                carte =cartes [idx ]
                clear_console ()
                print (f"You choose the card [{carte .rarete }] {carte .name } !")
                self .appliquer_carte (carte )
                wait_for_enter ()
                return 
            print ("Invalid choice.")
            wait_for_enter ()

            # ------------------ Resolution combat ------------------
    def gagner_recompenses (self ,enemy :Enemy )->None :
        j =self .player 
        if j is None :
            return 
        gold_gagne =random .randint (*enemy .gold_range )
        xp_gagne =random .randint (*enemy .xp_range )
        if gold_gagne >0 :
            j .gold +=gold_gagne +1 
            j .or_gagne_total +=gold_gagne 
            print (f"You ramasses {gold_gagne } gold coins.")
        j .xp +=xp_gagne 
        # mana se regenere a fin combat
        j .mana =j .mana_max 
        print ("Your mana se regenere entierement apres combat.")
        # Choice d' carte progression
        self .choix_cartes_apres_combat ()

        #------------------ menu combat ------------------
    def combat (self ,enemy :Enemy )->bool :
        j =self .player 
        if j is None :
            return False 
        clear_console ()
        print ("-"*40 )
        print (COLOR_RED +f"A {enemy .name } appears !"+COLOR_RESET )
        print ("-"*40 )
        while j .est_vivant ()and enemy .est_vivant ():
            self .afficher_etat_player ()
            self .afficher_status (enemy ,est_player =False )
            print (f"Enemy : {enemy .name }")
            print ("HP enemy :",enemy .barre_vie (),f"{enemy .hp }/{enemy .hp_max }")
            action =self .tour_player (enemy )
            if action =='mort':
                return False 
            if not enemy .est_vivant ():
                print (f"You as vaincu {enemy .name } !")
                j .enemies_killed +=1 
                self .gagner_recompenses (enemy )
                wait_for_enter ()
                return True 
            if j .player_class =="Necromancer"and j .invocation_squelette_tours >0 and enemy .est_vivant ():
                self .squelette_attack (enemy )
                if not enemy .est_vivant ():
                    print (f"Your squelette finishes off {enemy .name } !")
                    j .enemies_killed +=1 
                    self .gagner_recompenses (enemy )
                    wait_for_enter ()
                    return True 
            self .tour_enemy (enemy ,action )
            if not j .est_vivant ():
                print ("You es tombe au combat...")
                wait_for_enter ()
                return False 
            wait_for_enter ()
            clear_console ()
        return j .est_vivant ()

        # ------------------ shop ------------------
    def boutique (self )->None :
        j =self .player 
        if j is None :
            return 
        while True :
            clear_console ()
            print (COLOR_YELLOW +"========== shop =========="+COLOR_RESET )
            print (f"Current gold : {j .gold } coins")
            print ("0) Quit shop")
            print ("1) Healing potion (+1) - 10 gold")
            print ("2) Augmenter l'attack (+1) - 25 gold")
            print ("3) Augmenter defense (+1) - 25 gold")
            print ("4) Augmenter HP max (+5) - 30 gold")
            choix =input (">>").strip ()
            if choix =="0":
                break 
            if choix =="1":
                if j .gold <10 :
                    print ("Not enough d'gold !")
                else :
                    j .gold -=10 
                    j .potions +=1 
                    print ("You buy a potion healing.")
                wait_for_enter ()
                continue 
            if choix =="2":
                if j .gold <25 :
                    print ("Not enough d'gold !")
                else :
                    j .gold -=25 
                    j .attack +=1 
                    print ("Your attack augmente 1 ! ( cette run)")
                wait_for_enter ()
                continue 
            if choix =="3":
                if j .gold <25 :
                    print ("Not enough d'gold !")
                else :
                    j .gold -=25 
                    j .defense +=1 
                    print ("Your defense augmente 1 ! ( cette run)")
                wait_for_enter ()
                continue 
            if choix =="4":
                if j .gold <30 :
                    print ("Not enough d'gold !")
                else :
                    j .gold -=30 
                    j .hp_max +=5 
                    j .hp =j .hp_max 
                    print ("Your HP max augmentent 5 ! ( cette run)")
                wait_for_enter ()
                continue 
            print ("Invalid choice. Use 0 to quit gold 1-4 to buy.")
            wait_for_enter ()

            # ------------------ Loot : weapons & relics ------------------
    def donner_weapon_random (self )->None :
        j =self .player 
        if j is None :
            return 
        nouvelle =random .choice (WEAPONS [1 :])
        print (COLOR_YELLOW +f"You find a new weapon: {nouvelle .name } !"+COLOR_RESET )
        if nouvelle .description :
            print ("Description :",nouvelle .description )
        weapon_actuelle =j .weapon 
        if weapon_actuelle :
            print ("Your arme actuelle :",weapon_actuelle .name )
            if weapon_actuelle .description :
                print ("Description actuelle :",weapon_actuelle .description )
        if not j .weapons :
            j .weapons =[weapon_actuelle ]if weapon_actuelle else []
        while True :
            print ("What do you want to do?")
            print ("1) Equiper immediatement nouvelle arme")
            print ("2) Garder l'arme actuelle mais ajouter nouvelle a l'inventaire")
            print ("3) Laisser l'arme et continue your chemin")
            choix =input (">>").strip ()
            if choix =="1":
                j .weapons .append (nouvelle )
                j .weapon =nouvelle 
                print (f"You equip {nouvelle .name } !")
                break 
            if choix =="2":
                j .weapons .append (nouvelle )
                print (f"You ranges {nouvelle .name } dans your inventaire.")
                break 
            if choix =="3":
                print ("You laisses l'arme derriere toi.")
                break 
            print ("Invalid choice, try again.")

    def donner_relic_random (self )->None :
        j =self .player 
        if j is None :
            return 
        nouvelle =random .choice (RELICS )
        actuelle =j .relic 
        if actuelle is None :
            j .relic =nouvelle 
            print (f"You feel an ancient power: you obtain the relic '{nouvelle .name }'.")
            if nouvelle .description :
                print ("Description :",nouvelle .description )
            return 
        print (f"You discover a new relic : {nouvelle .name }")
        print ("Description nouvelle :",nouvelle .description or "???")
        print ("Relique actuelle :",actuelle .name )
        print ("Description actuelle :",actuelle .description or "???")
        while True :
            print ("What do you want to do?")
            print ("1) Remplacer relique actuelle par nouvelle")
            print ("2) Garder relique actuelle et laisser nouvelle")
            choix =input (">>").strip ()
            if choix =="1":
                j .relic =nouvelle 
                print (f"You remplaces your relique par {nouvelle .name }.")
                break 
            if choix =="2":
                print ("You decides garder your relique actuelle.")
                break 
            print ("Invalid choice.")

            # ------------------ Inventaire d'weapons ------------------
    def menu_weapons (self )->None :
        j =self .player 
        if j is None :
            return 
        if not j .weapons :
            print ("You n'as aucune arme dans your inventaire.")
            wait_for_enter ()
            return 
        while True :
            clear_console ()
            print ("====== INVENTAIRE D'ARMES ======")
            print ("(Choisis arme a equiper)")
            for i ,weapon in enumerate (j .weapons ,start =1 ):
                marque ="[Equipee]"if j .weapon is weapon else ""
                print (f" {i }) {weapon .name }{marque }")
            print ("0) Quit l'inventaire")
            choix =input (">>").strip ()
            if choix =="0":
                break 
            try :
                idx =int (choix )-1 
            except ValueError :
                print ("Invalid choice.")
                wait_for_enter ()
                continue 
            if 0 <=idx <len (j .weapons ):
                j .weapon =j .weapons [idx ]
                print (f"You equip {j .weapons [idx ].name }.")
                wait_for_enter ()
                break 
            print ("Invalid choice.")
            wait_for_enter ()

            # ------------------ Evenements ------------------
    def evenement_tresor (self )->None :
        j =self .player 
        if j is None :
            return 
        clear_console ()
        print ("You trouves petit coffre abandonne...")
        contenu =random .choice (["gold","potion","arme","relique","rien"])
        if contenu =="gold":
            gain =random .randint (10 ,25 )
            j .gold +=gain 
            j .or_gagne_total +=gain 
            print (f"The chest contains {gain } gold coins !")
        elif contenu =="potion":
            j .potions +=1 
            print ("You trouves potion healing !")
        elif contenu =="arme":
            self .donner_weapon_random ()
        elif contenu =="relique":
            self .donner_relic_random ()
        else :
            print ("coffre est vide... dommage.")
        wait_for_enter ()

    def evenement_feu_de_camp (self )->None :
        j =self .player 
        if j is None :
            return 
        clear_console ()
        print ("You arrives pres d' feu camp mysterieux.")
        print ("You decides te reposer moment.")
        soin =int (j .hp_max *0.5 )
        mana_recup =int (j .mana_max *0.6 )
        j .hp =min (j .hp_max ,j .hp +soin )
        j .mana =min (j .mana_max ,j .mana +mana_recup )
        print (f"You recover {soin } hp et {mana_recup } mana.")
        wait_for_enter ()

    def evenement_mystere (self )->None :
        j =self .player 
        if j is None :
            return 
        clear_console ()
        print ("You sens etrange presence... event mystery se declenche !")
        wait_for_enter ()
        effet =random .choice (["bon","bon","mauvais","mixte","arme","relique"])
        if effet =="arme":
            self .donner_weapon_random ()
            return 
        if effet =="relique":
            self .donner_relic_random ()
            return 
        if effet =="bon":
            choix =random .choice (["hp","attack","gold"])
            if choix =="hp":
                bonus =8 
                j .hp_max +=bonus 
                j .hp +=bonus 
                print (f"A benevolent energy surrounds you. Your max HP increases by {bonus } !")
            elif choix =="attack":
                j .attack +=2 
                print ('You ressens nouvelle force dans your bras : ATK +2 !')
            else :
                gain =30 
                j .gold +=gain 
                j .or_gagne_total +=gain 
                print (f"You find a pile of spectral gold: +{gain } gold !")
            wait_for_enter ()
            return 
        if effet =="mauvais":
            malus =random .choice (["hp","attack"])
            if malus =="hp":
                perte =max (1 ,int (j .hp_max *0.15 ))
                j .hp_max -=perte 
                j .hp =max (1 ,j .hp -perte )
                print (f"A curse gnaws at your body: -{perte } hp max...")
            else :
                j .attack =max (1 ,j .attack -1 )
                print ('froid etrange affaiblit your muscles : ATK -1.')
            wait_for_enter ()
            return 
        print ('pacte etrange... You gagnes en puissance mais you perds aussi quelque chose.')
        j .attack +=2 
        perte =max (1 ,int (j .hp_max *0.1 ))
        j .hp_max -=perte 
        if j .hp >j .hp_max :
            j .hp =j .hp_max 
        print (f"ATQ +2 mais -{perte } hp max.")
        wait_for_enter ()

        # ------------------ Difficulte & zones ------------------
    @staticmethod 
    def facteur_difficulte (floor :int )->float :
        palier =max (0 ,(floor -1 )//10 )
        return 1.0 +palier *0.25 

    @staticmethod 
    def zone_pour_floor (floor :int )->Dict :
        for zone in ZONES :
            if zone ['start']<=floor <=zone ['fin']:
                return zone 
        return ZONES [-1 ]

    @staticmethod 
    def est_floor_boss (floor :int )->bool :
        return floor %10 ==0 

    def choisir_chemins (self ,floor :int )->List [str ]:
        chemins =["combat","combat"]
        proba_shop =0.25 +self .meta .bonus_chance_shop *0.05 
        proba_mystere =0.10 +self .meta .bonus_chance_mystere *0.04 
        if random .random ()<proba_shop :
            idx =random .randint (0 ,len (chemins )-1 )
            chemins [idx ]="shop"
        if random .random ()<proba_mystere :
            indices_dispo =[i for i ,c in enumerate (chemins )if c =="combat"]
            if indices_dispo :
                idx =random .choice (indices_dispo )
                chemins [idx ]="mystery"
        if "combat"not in chemins :
            idx =random .randint (0 ,len (chemins )-1 )
            chemins [idx ]="combat"
        return chemins 

    @staticmethod 
    def decrire_chemin (chemin_type :str )->str :
        if chemin_type =="combat":
            return COLOR_RED +"Combat"+COLOR_RESET 
        if chemin_type =="shop":
            return COLOR_YELLOW +"shop"+COLOR_RESET 
        if chemin_type =="mystery":
            return COLOR_BLUE +"? event mystery ?"+COLOR_RESET 
        return "Inconnu"

        # ------------------ Floors ------------------
    def roguelike_floor (self ,floor :int )->bool :
        j =self .player 
        if j is None :
            return False 
        zone =self .zone_pour_floor (floor )
        clear_console ()
        j .floors_cleared =max (j .floors_cleared ,floor )
        print ("#"*50 )
        print (COLOR_CYAN +f"FLOOR {floor } - Zone : {zone ['name']}"+COLOR_RESET )
        print ("#"*50 )
        diff =self .facteur_difficulte (floor )
        if self .est_floor_boss (floor ):
            boss_data =random .choice (zone ['bosses']).copy ()
            # Exemple simple resistances/faiblesses selon boss
            resist ={}
            weak ={}
            if "Os"in boss_data ['name']:
                resist ={"physique":0.8 ,"feu":0.5 }
                weak ={"glace":1.4 }
            elif 'Foret'in boss_data ['name']or "Ent"in boss_data ['name']:
                resist ={"glace":0.7 }
                weak ={"feu":1.5 }
            elif "Runique"in boss_data ['name']or "Cristal"in boss_data ['name']:
                resist ={"sacre":0.7 }
                weak ={"shadow":1.4 }
            enemy =Enemy (
            name =boss_data ['name'],
            hp =int (boss_data ['hp']*diff ),
            hp_max =int (boss_data ['hp']*diff ),
            attack =int (boss_data ['attack']*diff ),
            defense =max (1 ,int (boss_data ['defense']+(diff -1 )*4 )),
            mana =0 ,
            mana_max =0 ,
            status =Status (),
            gold_range =boss_data ['gold'],
            xp_range =boss_data ['xp'],
            element_resistances =resist ,
            element_weaknesses =weak ,
            )
            print (COLOR_RED +"puissant boss se dresse sur your chemin !"+COLOR_RESET )
            wait_for_enter ()
            victoire =self .combat (enemy )
            if victoire :
                j .boss_killed +=1 
                clear_console ()
                print (f"You as vaincu {enemy .name } !")
                if floor <MAX_ETAGES :
                    print ("You ressens monde qui change autour toi...")
                    print ("You t'enfonces plus loin dans danger.")
                    wait_for_enter ()
                return True 
            return False 

        chemins =self .choisir_chemins (floor )
        while True :
            clear_console ()
            print ("#"*50 )
            print (COLOR_CYAN +f"FLOOR {floor } - Zone : {zone ['name']}"+COLOR_RESET )
            print ("#"*50 )
            self .afficher_etat_player ()
            print ("Chemins disponibles :")
            for i ,ch in enumerate (chemins ,start =1 ):
                print (f" {i }) {self .decrire_chemin (ch )}")
            print ("(Astuce : 1 ou 2 choisir chemin, 'i' gerer your weapons, 'admin' menu secret.)")
            choix =input ("Vers quel chemin want-you aller ? (1/2) :").strip ()
            if choix .lower ()=="i":
                self .menu_weapons ()
                continue 
            if choix =="admin":
                self .menu_admin ()
                continue 
            if choix not in ("1","2"):
                print ("Invalid choice.")
                wait_for_enter ()
                continue 
            idx =int (choix )-1 
            chemin_type =chemins [idx ]
            if chemin_type =="combat":
                enemy_data =random .choice (zone ['ennemis']).copy ()
                resist ={}
                weak ={}
                if 'Squelette'in enemy_data ['name']:
                    resist ={"feu":0.5 ,"physique":0.9 }
                    weak ={"glace":1.3 }
                elif "Loup"in enemy_data ['name']:
                    resist ={"physique":0.9 }
                    weak ={"feu":1.2 }
                elif "Mage"in enemy_data ['name']:
                    resist ={"feu":0.8 ,"glace":0.8 }
                    weak ={"shadow":1.3 }
                enemy =Enemy (
                name =enemy_data ['name'],
                hp =int (enemy_data ['hp']*diff ),
                hp_max =int (enemy_data ['hp']*diff ),
                attack =int (enemy_data ['attack']*diff ),
                defense =max (1 ,int (enemy_data ['defense']+(diff -1 )*3 )),
                mana =0 ,
                mana_max =0 ,
                status =Status (),
                gold_range =enemy_data ['gold'],
                xp_range =enemy_data ['xp'],
                element_resistances =resist ,
                element_weaknesses =weak ,
                )
                return self .combat (enemy )
            if chemin_type =="shop":
                self .boutique ()
                return True 
            if chemin_type =="mystery":
                self .evenement_mystere ()
                return True 

                # ------------------ sanctuary mort (Skill tree) ------------------
    def calcul_essence_gagnee (self )->int :
        j =self .player 
        if j is None :
            return 1 
        essence =0 
        essence +=j .floors_cleared *2 
        essence +=j .enemies_killed *1 
        essence +=j .boss_killed *5 
        essence +=j .or_gagne_total //50 
        return max (1 ,essence )

    def appliquer_talent (self ,talent_id :str ,node :Dict )->None :
        t_type =node .get ("type")
        target =node .get ("cible")
        val =node .get ("valeur",0 )
        if t_type in ("stat","start_res",'chance')and target :
            actuel =getattr (self .meta ,target ,0 )
            setattr (self .meta ,target ,actuel +val )
            print (f"The talent '{node ['name']}' renforce {target } of {val }.")
        elif t_type =="unlock_class":
            player_class =node .get ("cible")
            if player_class and player_class not in self .meta .classes_unlocked :
                self .meta .classes_unlocked .append (player_class )
                print (f"Nouvelle classe debloquee : {player_class } !")

    def death_shop (self )->None :
    # sanctuary = arbre talents V17.2
        while True :
            clear_console ()
            print ('====== sanctuary MORT - ARBRE TALENTS ======')
            print (f"Essence d'ame disponible : {self .meta .essence }")
            print ()
            print ("Talents deja debloques :")
            if not self .meta .talents_unlocked :
                print ("Aucun moment.")
            else :
                for tid in self .meta .talents_unlocked :
                    node =SKILL_TREE .get (tid )
                    if node :
                        print (f"  - {node ['name']}")
            print ()
            # Construire liste talents achetables
            disponibles =[]
            for tid ,node in SKILL_TREE .items ():
                if tid in self .meta .talents_unlocked :
                    continue 
                prereq =node .get ("prerequis",[])
                if all (p in self .meta .talents_unlocked for p in prereq ):
                    disponibles .append ((tid ,node ))
            if not disponibles :
                print ("Aucun talent supplementaire n'est actuellement disponible.")
                print ("Tape 0 quitter.")
            else :
                print ("Talents disponibles :")
                for i ,(tid ,node )in enumerate (disponibles ,start =1 ):
                    print (f" {i }) {node ['name']} ({node ['cout']} essence) - {node ['description']}")
            print ("0) Quit sanctuary")
            choix =input (">>").strip ()
            if choix =="0":
                break 
            try :
                idx =int (choix )-1 
            except ValueError :
                print ("Invalid choice.")
                wait_for_enter ()
                continue 
            if idx <0 or idx >=len (disponibles ):
                print ("Invalid choice.")
                wait_for_enter ()
                continue 
            tid ,node =disponibles [idx ]
            cost =node .get ("cout",0 )
            if self .meta .essence <cost :
                print ("Not enough soul essence...")
                wait_for_enter ()
                continue 
            self .meta .essence -=cost 
            self .appliquer_talent (tid ,node )
            self .meta .talents_unlocked .append (tid )
            self .meta .save ()
            wait_for_enter ()

            # ------------------ Menu admin secret (ameliore) ------------------
    def menu_admin (self )->None :
        while True :
            clear_console ()
            print ("===== MENU ADMIN (DEBUG) =====")
            print ("ATTENTION : reserve aux tests. Utilise precaution.")
            print ()
            print ("[META-PROGRESSION]")
            print (f"  Essence actuelle : {self .meta .essence }")
            print (f"  Classes debloquees : {','.join (self .meta .classes_unlocked )}")
            print ()
            print ("1) +100 essence d'ame")
            print ("2) Unlock toutes classes")
            print ("3) Reset entierement meta-progression")
            print ()
            print ("[RUN ACTUELLE]")
            if self .player is not None :
                print (f"  Joueur : {self .player .name } ({self .player .player_class }) - hp {self .player .hp }/{self .player .hp_max }, Mana {self .player .mana }/{self .player .mana_max }")
                print ("4) Donner 999 gold au joueur")
                print ("5) Soigner entierement joueur (HP/mana)")
            else :
                print ("Aucun joueur actif (lance run unlock ces options).")
            print ()
            print ("[DIVERS]")
            print ("6) Afficher detail complet meta (debug)")
            print ("0) Quit menu admin")
            choix =input (">>").strip ()
            if choix =="0":
                break 
            if choix =="1":
                self .meta .essence +=100 
                self .meta .save ()
                print ("+100 essence ajoutee.")
                wait_for_enter ()
                continue 
            elif choix =="2":
                for infos in PLAYER_CLASSES .values ():
                    name_player_class =infos ["name"]
                    if name_player_class not in self .meta .classes_unlocked :
                        self .meta .classes_unlocked .append (name_player_class )
                self .meta .save ()
                print ("Toutes classes sont maintenant debloquees.")
                wait_for_enter ()
                continue 
            elif choix =="3":
                confirm =input ("Are you sure you want to reset EVERYTHING? (yes/no):").strip ().lower ()
                if confirm =="oui":
                    filename =self .meta .filename 
                    self .meta =Meta ()
                    self .meta .filename =filename 
                    self .meta .save ()
                    print ("Meta-progression reinitialisee.")
                else :
                    print ("Reinitialisation annulee.")
                wait_for_enter ()
                continue 
            elif choix =="4"and self .player is not None :
                self .player .gold +=999 
                print ("joueur recoit 999 gold.")
                wait_for_enter ()
                continue 
            elif choix =="5"and self .player is not None :
                self .player .hp =self .player .hp_max 
                self .player .mana =self .player .mana_max 
                print ("joueur est entierement heal.")
                wait_for_enter ()
                continue 
            elif choix =="6":
                clear_console ()
                print ("===== DETAIL META =====")
                print (f"Essence : {self .meta .essence }")
                print (f"hp bonus : {self .meta .hp_bonus }")
                print (f"ATQ bonus : {self .meta .attack_bonus }")
                print (f"DEF bonus : {self .meta .defense_bonus }")
                print (f"Mana bonus : {self .meta .mana_bonus }")
                print (f"Starting gold: {self .meta .or_start }")
                print (f"Starting potions: {self .meta .potions_start }")
                print (f"Bonus chance shop : {self .meta .bonus_chance_shop }")
                print (f"Bonus chance mystere : {self .meta .bonus_chance_mystere }")
                print (f"Talents debloques : {','.join (self .meta .talents_unlocked )if self .meta .talents_unlocked else 'aucun'}")
                wait_for_enter ()
                continue 
            print ("Invalid choice.")
            wait_for_enter ()

            # ------------------ run ------------------
    def une_run (self )->None :
        self .creer_player ()
        j =self .player 
        if j is None :
            return 
        floor =1 
        while j .est_vivant ()and floor <=MAX_ETAGES :
            achievements_floor =self .roguelike_floor (floor )
            if not achievements_floor :
                break 
            floor +=1 
            clear_console ()
        clear_console ()
        if j .est_vivant ()and floor >MAX_ETAGES :
            print ("INCROYABLE ! You as survecu a toutes zones donjon !")
            print ("catacombes se taisent... l'instant.")
        else :
            print ("Your run se termine ici... Mais mort n'est qu' nouveau depart.")
        essence_gagnee =self .calcul_essence_gagnee ()
        if j .boss_killed >=1 :
            self .meta .debloquer_achievements ('premier_boss')
        if j .enemies_killed >=20 :
            self .meta .debloquer_achievements ('tueur_de_monstres')
        if j .floors_cleared >=10 :
            self .meta .debloquer_achievements ('explorateur')
        print (f"Pendant cette run, you as parcouru {j .floors_cleared } etages,")
        print (f"vaincu {j .enemies_killed } ennemis et {j .boss_killed } boss.")
        print (f"You as gagne {essence_gagnee } essence d'ame.")
        self .meta .essence +=essence_gagnee 
        self .meta .save ()
        wait_for_enter ()

        # ------------------ Menu principal ------------------
    def afficher_achievements (self )->None :
        clear_console ()
        print ("===== SUCCES DEBLOQUES =====")
        if not self .meta .achievements :
            print ("Aucun succes debloque moment.")
        else :
            for cle ,data in self .meta .achievements .items ():
                print (f"- {data .get ('description',cle )}")
        wait_for_enter ()

    def display_features (self )->None :
        clear_console ()
        print ("===== FEATURE SUMMARY =====")
        print ('- Floor-based roguelike with 3 zones (Catacombs, Cursed Forest, Runic Citadel).')
        print ("- Turn-based combat system with status effects (poison, burn, stun).")
        print ("- Weapons and relics with bonuses, critical hits, and life steal.")
        print ("- Meta-progression: soul essence currency and a permanent talent tree.")
        print ('- Playable classes with special powers (Warrior, Mage, Rogue + advanced classes to unlock).')
        print ("- Card-based progression after each fight; some cards are class-specific.")
        print ('- Events: treasures, campfires, mystery encounters.')
        print ("- Secret admin menu for testing (type 'admin' in some menus).")
        wait_for_enter ()

    def main_menu (self )->None :
        while True :
            clear_console ()
            print (COLOR_MAGENTA +"="*30 +COLOR_RESET )
            print (COLOR_BOLD +'ROGUELIKE CATACOMBES'+COLOR_RESET )
            print (COLOR_MAGENTA +"="*30 +COLOR_RESET )
            print (f"soul essence : {self .meta .essence }")
            print ("1) new run")
            print ('2) open death sanctuary (skill tree)')
            print ("3) leave")
            print ("4) see the fonctionality")
            choix =input (">>").strip ()
            if choix =="admin":
                self .menu_admin ()
                continue 
            if choix =="1":
                self .une_run ()
                continue 
            if choix =="2":
                self .death_shop ()
                continue 
            if choix =="3":
                self .afficher_achievements ()
                clear_console ()
                print ("thanks for playing")
                break 
            if choix =="4":
                self.display_features()
                continue 
            print ("Invalid choice.")
            wait_for_enter ()


def main ():
    game =Game ()
    game .main_menu ()


if __name__ =="__main__":
    main ()
