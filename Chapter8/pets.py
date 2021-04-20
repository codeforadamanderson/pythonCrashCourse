def describe_pet(pet_name, animal_type='dragon'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='tribble', pet_name='furry')

describe_pet(animal_type='targ', pet_name='snarls')

describe_pet(pet_name='smokey')