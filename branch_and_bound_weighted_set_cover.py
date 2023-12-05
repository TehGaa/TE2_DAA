# code is referenced from https://github.com/AndreaRubbi/Set-Cover-problem-solution-Python
def bypassbranch(subset, i):
    for j in range(i-1, -1, -1):
        if subset[j] == 0:
            subset[j] = 1
            return subset, j+1

    return subset, 0

def nextvertex(subset, i, m):
    if i < m:
        subset[i] = 0
        return subset, i+1
    else:
        for j in range(m-1, -1, -1):
            if subset[j] == 0:
                subset[j] = 1
                return subset, j+1
                
    return subset, 0

def BB(universe,sets,weights):
    subset = [1 for x in range(len(sets))]
    subset[0] = 0
    bestWeight = sum(weights) 
    i = 1

    while i > 0:

        if i < len(sets):
            weight, tSet = 0, set()
            for k in range(i):
                weight += subset[k]*weights[k]
                if subset[k] == 1: tSet.update(set(sets[k]))

            if weight > bestWeight:
                subset, i = bypassbranch(subset, i)
                continue
            for k in range(i, len(sets)): tSet.update(set(sets[k]))
            if tSet != universe:
                subset, i = bypassbranch(subset, i)
            else:
                subset, i = nextvertex(subset, i, len(sets))
                
        else:
            weight, fSet = 0, set()
            for k in range(i):
            	weight += subset[k]*weights[k]
            	if subset[k] == 1: fSet.update(set(sets[k]))

            if weight < bestWeight and fSet == universe:
            	bestWeight = weight
            	bestSubset = subset[:]
            subset, i = nextvertex(subset, i , len(sets))

    return bestWeight, bestSubset