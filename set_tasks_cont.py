
def observations():
    observations = []
    for x in range(5):
        observations.append(input("Please enter an observation \n"))
    return observations
def remove_observations(obs_list):

    if input("Do you want to remove any observations [Y/N] \n") == "Y":
        obs_to_remove = input("Which observation to remove? \n")
        obs_list.remove(obs_to_remove)
    return obs_list
def run_task3():
    observations_list = observations()
    remove_observations(observations_list)
    print(sorted(observations_list))

if __name__ == "__main__":
    run_task3()