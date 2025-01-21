from db.models import Meal
# CRUD operations for meals

valid_meal_categories = set(['Dessert', 'Breakfast', 'Lunch', 'Dinner', 'Snack'])

# read all meals by category
async def get_meals_by_category(category):
    meals = await Meal.filter(category=category).all()
    return meals

# create a new meal
async def create_meal(name, url, category, difficulty, healthiness):

    if category not in valid_meal_categories:
        raise ValueError("Invalid Meal Category")

    # TODO: additional validation for url, diff, healthiness values

    # users = await User.filter(id=userid).all()
    # if len(users) == 0:
    #     raise Exception("no user found for that id")
    # username = users[0].name


    # if url is None or len(url) == 0:
    #     raise Exception("some shit aint right with the url")
    meal = await Meal.create(
        name=name,
        url=url,
        category=category,
        difficulty=difficulty,
        healthiness=healthiness,
    )
    return meal

# update the difficulty of a meal
async def update_meal_difficulty(meal_id, new_difficulty):
    meal = await Meal.get(id=meal_id) # returns None if the meal doesn't exist
    if meal:
        meal.difficulty = new_difficulty
        await meal.save()
        return meal
    else:
        return None

# delete a meal by ID
async def delete_meal(meal_id):
    meal = await Meal.get(id=meal_id)
    await meal.delete()
    return {"message": f"Meal with ID {meal_id} deleted successfully."}
