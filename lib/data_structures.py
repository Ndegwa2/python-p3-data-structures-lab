spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    #Returns a list of names of spicy foods.
    return [food["name"] for food in spicy_foods]

def get_average_heat_level(spicy_foods):
    #Returns a list of dictionaries where the heat level is greater than 5.
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    #Prints each spicy food in the specified format.
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    #Returns a dictionary of the spicy food with the specified cuisine.
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if no matching cuisine is found

def print_spiciest_foods(spicy_foods):
    #Prints only the spicy foods with heat level greater than 5.
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def average_heat_level(spicy_foods):
    #Returns the average heat level of the spicy foods.
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    count = len(spicy_foods)
    return total_heat // count  # Use integer division for the average

def create_spicy_food(spicy_foods, new_spicy_food):
    #Adds a new spicy food to the list and returns the updated list.
    spicy_foods.append(new_spicy_food)
    return spicy_foods
