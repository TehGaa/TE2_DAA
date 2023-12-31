import random

random.seed(2)

def subset_generator(universe):
    subsets = []
    size = 49
    while len(subsets) < size:
        subset = set(random.sample(sorted(universe), 
                               random.randint(1, len(universe))))
        while subset in subsets:
            subset = set(random.sample(sorted(universe), 
                               random.randint(1, len(universe))))
        subsets.append(subset)
    elem_not_in_universe = universe - set().union(*subsets)
    if len(elem_not_in_universe) != 0:
        subsets.append(elem_not_in_universe)
    else:
        subsets.append(universe)
    return subsets

if __name__ == "__main__":
    datasets = [20, 200, 2000]
    for i in datasets:
        folder_name = ""
        if i == 20:
            folder_name = f"dataset_kecil"
        elif i == 200:
            folder_name = f"dataset_sedang"
        else:
            folder_name = f"dataset_besar"
        with open(f'{folder_name}/subset_{i}.txt', 'w') as file:
            subset = subset_generator(set([j for j in range(1, i+1)]))
            for k in subset:
                file.write(" ".join([str(s) for s in list(k)]) + "\n")
        