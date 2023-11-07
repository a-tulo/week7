def observed():
    observations = {'Car', 'Sky Scraper', 'Bike', 'House'}
    return observations

def observed_items():
    observations = []
    for x in range(7):
        observations.append(input("Please enter an observation \n"))
    return observations

def run_task1():
    print(observed())

def run_task2():
    print("Counting observations...")
    observations = observed_items()
    observations_set = set()

    for x in observations:
        temp_tuple = (x ,observations.count(x))
        observations_set.add(temp_tuple)

    for x in observations_set:
        print(f"{x[0]} observed {x[1]} times")



if __name__ == "__main__":
    run_task2()