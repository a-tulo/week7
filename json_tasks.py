import json
def read(path):
    with open(path) as file:
        data = json.load(file)
        location = data["location"]
        population = data["population"]
        print(f"Place Name: {location}")
        print(f"Population Size: {population}")

        for bot in data["bots"]:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")



def save(path,)
def run():
    read("futurama.json")

def read_task2(path):
    with open(path) as file:
     data = json.load(file)
    print("Done!")
    return data

def run_task2():
    read("futurama.json")
if __name__ == "__main__":
  run()

