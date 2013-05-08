from itertools import izip
from copy import deepcopy

def get_fstates(decay, db, final_db):
    if decay['branching'][0] < 1E-10:
        return

    print decay['history']

    final_db.insert({
        'scheme': decay['history'],
        'branching': decay['branching'],
        'fstate': decay['products'],
        'father': decay['father']
    })

    if len(decay['products']) == 1:
        return

    for p in decay['products']:
        if not p in db:
            continue
        for k in db[p]:
            work_copy = deepcopy(decay)

            work_copy['products'].remove(k['father'])
            work_copy['products'] += k['products']

            work_copy['history'] += '; {} --> {}'.format(
                k['father'], ' '.join(k['products']))

            work_copy['branching'][0] *= k['branching'][0]

            get_fstates(work_copy, db, final_db)
