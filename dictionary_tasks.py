def pattern():
    sequences = {"Short Sequence" : 3, "Medium Sequence" : 2, "Long Sequenece" : 1}
    return sequences

def display_keys(dict):
    for keys in dict:
        print(f"{keys}")


def display_values(dict):
    for value in dict.values():
        print(f"{value}")

def display_items(dict):
    for key, value in dict.items():
        print(f"{key}: {value}")
def run():
    print("Dictionary:")
    dict = pattern()

    print(dict)
    print()
    print("Keys: ")
    display_keys(dict)
    print()
    print("Values")
    display_values(dict)
    print()
    print("Pairs ")
    display_items(dict)


if __name__ == "__main__":
    run()
