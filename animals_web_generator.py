import json

def load_data(file_path):
    """ Loads JSON file. """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def create_animals_data_string(animal_data):
    """ Iterates through the data and prints:
        name,
        diet,
        first location from locations list,
        type
        :return animals_string
    """
    animals_string = ''
    for animal in animal_data:
        animal_name = animal.get('name')
        animal_diet = animal.get('characteristics', None).get('diet', None)
        animal_location = animal.get('locations', None)[0]
        animal_type = animal.get('characteristics', None).get('type', None)
        if animal_name:
            animals_string += f"\nName: {animal_name}\n"
        if animal_diet:
            animals_string += f"Diet: {animal_diet.capitalize()}\n"
        if animal_location:
            animals_string += f"Location: {animal_location}\n"
        if animal_type:
            animals_string += f"Type: {animal_type.capitalize()}\n"
    return animals_string


def read_animals_template_content():
    """ Gets the content from 'animals_template.html'."""
    with open("animals_template.html", "r") as html_file:
        return html_file.read()


def write_animals_template_content(animals_html):
    """ Writes the updated content to 'animals_template.html'."""
    with open("animals_template.html", "w") as html_file:
        html_file.write(animals_html)

def main():
    animals_data = load_data("animals_data.json")
    animals_data_string = create_animals_data_string(animals_data)
    animals_template_html = read_animals_template_content()
    animals_template_html = animals_template_html.replace("__REPLACE_ANIMALS_INFO__",
                                                          animals_data_string)
    write_animals_template_content(animals_template_html)







if __name__ == '__main__':
    main()
