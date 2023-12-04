import time
from greedy_weighted_set_cover import set_cover
from branch_and_bound_weighted_set_cover import BB

def running_time_greedy_weighted_set_cover(universes, subsets, costs, datasets):
    print("-------------GREEDY RESULT AND RUNNING TIME--------------")
    for i in range(len(datasets)):
        print(f"-----------------DATASET {datasets[i]}----------------")
        begin = time.time()
        result = set_cover(universes[i], subsets[i], costs[i])
        end = time.time()
        cover, cost = result[0], result[1]
        print("subset:", cover)
        print("cost:", cost)
        print(f"running time: {end-begin:.8f} seconds")
        print()

def running_time_branch_and_bound_weighted_set_cover(universes, subsets, costs, datasets):
    print("-------------B&B RESULT AND RUNNING TIME--------------")
    for i in range(len(datasets)):
        print(f"-----------------DATASET {datasets[i]}----------------")
        begin = time.time()
        result = BB(universes[i], subsets[i], costs[i])
        end = time.time()
        cost, temp_cover = result[0], result[1]
        cover = []
        for x in range(len(temp_cover)):
            if temp_cover[x] == 1:
                cover.append(subsets[i][x])
        print("subset:", cover)
        print("cost:", cost)
        print(f"running time: {end-begin:.8f} seconds")
        print()

    pass

def generate_input(datasets):
    universes = [0, 0, 0]
    subsets = [[], [], []]
    costs = [0, 0, 0]

    # generate universes
    for i in range(len(datasets)):
        folder_name = ""
        if i == 0:
            folder_name = f"dataset_kecil"
        elif i == 1:
            folder_name = f"dataset_sedang"
        else:
            folder_name = f"dataset_besar"
        with open(f"{folder_name}/universe_{datasets[i]}.txt", 'r') as file:
            for line in file:
                line = line.strip().strip("\n")
                if line == "":
                    break
                universes[i] = set([int(j) for j in line.split(" ")])

    # generate subsets
    for i in range(len(datasets)):
        folder_name = ""
        if i == 0:
            folder_name = f"dataset_kecil"
        elif i == 1:
            folder_name = f"dataset_sedang"
        else:
            folder_name = f"dataset_besar"
        with open(f"{folder_name}/subset_{datasets[i]}.txt", 'r') as file:
            for line in file:
                line = line.strip().strip("\n")
                if line == "":
                    break
                subsets[i].append(set([int(j) for j in line.split(" ")]))
    
    # generate costs
    for i in range(len(datasets)):
        folder_name = ""
        if i == 0:
            folder_name = f"dataset_kecil"
        elif i == 1:
            folder_name = f"dataset_sedang"
        else:
            folder_name = f"dataset_besar"
        with open(f"{folder_name}/cost_{datasets[i]}.txt", 'r') as file:
            for line in file:
                line = line.strip().strip("\n")
                if line == "":
                    break
                costs[i] = [int (j) for j in line.split(" ")]

    return universes, subsets, costs

if __name__ == "__main__":
    datasets = [20, 200, 2000]
    universes, subsets, costs = generate_input(datasets)
    running_time_greedy_weighted_set_cover(universes, subsets, costs, datasets)
    running_time_branch_and_bound_weighted_set_cover(universes, subsets, costs, datasets)
