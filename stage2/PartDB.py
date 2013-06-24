from operator import mul
from copy import deepcopy
from datetime import datetime
from multiprocessing import Pool, cpu_count

from weight_split import get_jobs
from database import *
from NameConjugate import *





bosons = ['W','Z','gamma']
leptons = ['e','mu','tau','nu_e','nu_mu','nu_tau']
mesons = ['pi','K']
baryons = ['p', 'n', 'N','Omega', 'Delta', 'Lambda', 'Sigma', 'Xi', 'Chi']

neutrals = ['Z', 'gamma', 'pi', 'b_', 'rho', 'a_', 'eta', 'h_', 'omega', 'phi', 'f_', 'X(', 'chi', 'psi', 'Y']

particles.drop()
particles.create_index("keys", unique=True)

def AddToDB(prt,aprt):
    try:
        particles.insert({
                        'mass': prt[0],
                        'particle': prt[1],
                        'antiparticle': aprt[1],
                        'keys': [prt[1], aprt[1]]
                        })
        print 'added '+prt[1]+' and '+aprt[1]
    except pymongo.errors.DuplicateKeyError:
    	print 'Dublicate exceprion!'
        return

for x in open("../data/masses-fin.txt").readlines():
    prt = ['mass','name','isBaryon','isNeutral']
    aprt = ['mass','name','isBaryon','isNeutral']
    prt[0] = x.split(', ')[0][1:]
    prt[1] = x.split(', ')[2][:-2]
    for b in baryons:
    	if b in prt[1]:
    		prt[2] = 'baryon'
    prt[3] = 0
    for n in neutrals:
    	if n in prt[1]:
    		prt[3] = 1
    
    aprt = deepcopy(prt)
    if prt[2] == 'baryon':
        aprt[1] = BaryonNameConjugate(aprt[1])
    elif prt[3] != 1 or '+' in prt[1] or '-' in prt[1]:
        aprt[1] = NormalNameConjugate(aprt[1])

    AddToDB(prt,aprt)
