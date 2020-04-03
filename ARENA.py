# -*- coding: utf-8 -*-
"""
Arena

ENGINE:
    

joao:
attack = 30%
sword = 1d10 
armor = 10
HP = 20

professor:
attack = 40%
axe = 1d12 
armor = 15
HP = 30

combate por turno
1 - iniciativa (cara ou coroa)
2 - ataque
    joao ataca professor
    30% - 15 = 15...
    ataque = aleatorio (100)
    se ataque <= (ataque_joao - armad_prof):
        dano = aleatorio(10)
        hp_prof = hp_prof - dano
"""




# generate random integer values
import time                #tempo da maquina
from random import seed    #semente
from random import randint 
# seed random number generator

# generate some integers
att_pers = 30
dam_pers = 10
arm_pers = 10
hp_pers = 20

att_prof = 40
dam_pers = 12
arm_prof = 15
hp_prof = 30

def aleatorio(num):
    seed(time.time())
    return randint(1,num)
ataque = aleatorio(100)
print(" joao ataca o professor e tira", ataque,"  no seu ataque ")        
if ataque <= (att_pers - arm_prof):
    dano = aleatorio(dam_pers)
    hp_prof = hp_prof - dano
    print(" acertando o ataque e gerando ", dano, " de dano ")
    print(" reduzindo o HP do professor para ", hp_prof)







