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

def BB(universe,sets,costs):
    subset = [1 for x in range(len(sets))]
    subset[0] = 0
    bestCost = sum(costs) 
    i = 1

    while i > 0:

        if i < len(sets):
            cost, tSet = 0, set()
            for k in range(i):
                cost += subset[k]*costs[k]
                if subset[k] == 1: tSet.update(set(sets[k]))

            if cost > bestCost:
                subset, i = bypassbranch(subset, i)
                continue
            for k in range(i, len(sets)): tSet.update(set(sets[k]))
            if tSet != universe:
                subset, i = bypassbranch(subset, i)
            else:
                subset, i = nextvertex(subset, i, len(sets))
                
        else:
            cost, fSet = 0, set()
            for k in range(i):
            	cost += subset[k]*costs[k]
            	if subset[k] == 1: fSet.update(set(sets[k]))

            if cost < bestCost and fSet == universe:
            	bestCost = cost
            	bestSubset = subset[:]
            subset, i = nextvertex(subset, i , len(sets))

    return bestCost, bestSubset