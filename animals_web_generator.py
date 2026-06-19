import json

def load_data(file_path):
    """ Loads JSON file. """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def prints_animals(animal_data):
    """ Iterates through the data and prints:
        name,
        diet,
        first location from locations list,
        type
    """
    for animal in animal_data:
        animal_name = animal.get('name')
        animal_diet = animal.get('characteristics', None).get('diet', None)
        animal_location = animal.get('locations', None)[0]
        animal_type = animal.get('characteristics', None).get('type', None)
        if animal_name:
            print(f"\nName: {animal_name}")
        if animal_diet:
            print(f"Diet: {animal_diet}")
        if animal_location:
            print(f"Location: {animal_location}")
        if animal_type:
            print(f"Type: {animal_type}")




def main():
    animals_data = load_data("animals_data.json")
    prints_animals(animals_data)




if __name__ == '__main__':
    main()
