def convert_to_human(
        animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    if animal_age < first_year:
        return 0
    elif animal_age < first_year + second_year:
        return 1
    else:
        return 1 + (animal_age - first_year - second_year) // each_year


def get_human_age(
        cat_age: int, dog_age: int
) -> list:
    cat_to_human = convert_to_human(cat_age, 15, 9, 4)
    dog_to_human = convert_to_human(dog_age, 15, 9, 5)
    return [cat_to_human, dog_to_human]
