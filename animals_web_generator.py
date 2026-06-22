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

        # Write html string
        animals_string += '<li class="cards__item">'
        animals_string += '<div class="card__title">Wire Fox Terrier</div>'
        animals_string += '<p class="card__text">'
        if animal_name:
            animals_string += f"\n<strong>Name:</strong> {animal_name}<br/>\n"
        if animal_diet:
            animals_string += f"<strong>Diet:</strong> {animal_diet.capitalize()}<br/>\n"
        if animal_location:
            animals_string += f"<strong>Location:</strong> {animal_location}<br/>\n"
        if animal_type:
            animals_string += f"<strong>Type:</strong> {animal_type.capitalize()}<br/>\n"
        animals_string += '</p>'
        animals_string += '</li>'
    return animals_string


def read_animals_template_content():
    """ Gets the content from 'animals_template.html'."""
    with open("animals_template.html", "r") as html_file:
        return html_file.read()


def write_animals_content(animals_html):
    """ Writes the updated content to 'animals_template.html'."""
    with open("animals.html", "w") as html_file:
        html_file.write(animals_html)


def main():
    animals_data = load_data("animals_data.json")
    animals_data_string = create_animals_data_string(animals_data)
    animals_template_html = read_animals_template_content()
    animals_template_html = animals_template_html.replace("__REPLACE_ANIMALS_INFO__",
                                                          animals_data_string)
    write_animals_content(animals_template_html)







if __name__ == '__main__':
    main()
