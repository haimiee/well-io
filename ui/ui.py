from typing import List, Dict
from nicegui import ui, app
import asyncio

from api.meals import create_meal, get_meals_by_category, update_meal_difficulty, delete_meal
from db.models import *

def run_ui():

    def logout():
        app.storage.user['account'] = None
        ui.navigate.to("/")

    @ui.page("/")
    def main_page():
        if app.storage.user.get('account', None) is not None:
            user: User = app.storage.user['account']
            ui.label(f"Hi {user.name} {user.id} {user.email}! Welcome back to Wellio!").classes("text-lg font-bold")
        else:       
            ui.label("Welcome to Wellio!").classes("text-lg font-bold")
        ui.link("Sign Up", "/signup")
        ui.link("Meal CRUD UI", "/meals")
        ui.button("Log Out", on_click=logout)
    
        list_of_users: List[User] = []
        mood_log: List[Dict] = []
        mood_log_visible = False

    async def create_user(name, email):
        if await User.filter(email=email).exists():
            ui.notify(f"Failed to create user, email \"{email}\" ia already taken.", type="negative", close_button=True)
        else:
            new_user = await User.create(name=name, email=email)
            # ui.notify("User created!")
            app.storage.user['account'] = new_user
            ui.navigate.to("/")

    # user sign up page
    @ui.page('/signup')
    async def signup_page():
        ui.label("Sign Up")
        user_name_input = ui.input(label="User Name", placeholder="Enter your name")
        user_email_input = ui.input(label="User Email", placeholder="Enter your email")
        ui.button("Sign Up", on_click=lambda: create_user(user_name_input.value, user_email_input.value))

    # meal CRUD page
    @ui.page("/meals")
    def meal_page():
        ui.label("Meal CRUD Operations").classes("text-lg font-bold")
        
        # create meal section
        meal_name_input = ui.input(label="Meal Name", placeholder="Enter the meal name")
        meal_url_input = ui.input(label="Meal URL", placeholder="Enter the recipe URL")
        meal_category_input = ui.input(label="Category", placeholder="e.g., breakfast")
        meal_difficulty_input = ui.input(label="Difficulty", placeholder="1-5")
        meal_healthiness_input = ui.input(label="Healthiness", placeholder="1-5")

        results = ui.column() # displays the output dynamically
        
        async def create_meal_ui():
            name = meal_name_input.value
            url = meal_url_input.value
            category = meal_category_input.value
            difficulty = int(meal_difficulty_input.value)
            healthiness = int(meal_healthiness_input.value)
            await create_meal(name, url, category, difficulty, healthiness)
            ui.notify(f"Meal '{name}' created successfully!")
        
        ui.button("Create Meal", on_click=create_meal_ui)

        # display meals section
        async def get_meals_ui():
            try:
                category = meal_category_input.value
                meals = await get_meals_by_category(category)
                results.clear() # clear previous results
                if meals:
                    for meal in meals:
                        results.append(
                            f"ID: {meal.id}, Name: {meal.name}, Difficulty: {meal.difficulty, }"
                            f"Healthiness: {meal.healthiness}, Category: {meal.category}"
                        )
                else:
                    ui.notify("No meal found for this category", type="info")
            except Exception as e:
                ui.notify(f"Error: {str(e)}", type="negative")

        """
        No lambda or asyncio.run is necessary because NiceGUI automactically
        handles async functions for button callbacks.
        """
        # ui.button("View Meals", on_click=lambda: asyncio.run(get_meals_ui()))
        ui.button("Create Meal", on_click=create_meal_ui)

        # update meal section
        meal_id_input = ui.input(label="Meal ID", placeholder="Enter the meal ID")
        async def update_meal_ui():
            meal_id = int(meal_id_input.value)
            new_difficulty = int(meal_difficulty_input.value)
            await update_meal_difficulty(meal_id, new_difficulty)
            ui.notify(f"Updated Meal ID {meal_id}.")

        ui.button("Update Difficulty", on_click=lambda: asyncio.run(update_meal_ui()))

        # delete meal section
        async def delete_meal_ui():
            meal_id = int(meal_id_input.value)
            await delete_meal(meal_id)
            ui.notify(f"Deleted Meal ID {meal_id}.")

        ui.button("Delete Meal", on_click=lambda: asyncio.run(delete_meal_ui()))


    # # admin debug page
    @ui.page('/debug')
    async def debug_page():
        # users

        ui.label("Debug Page: Users List")
        users_list = []

        @ui.refreshable
        def userTable():
            # Table to display users
            nonlocal users_list

            data = []

            for user in users_list:
                data.append({'ID': user.id, 'Name': user.name, 'Email': user.email})

            ui.table(columns=[
                {'label':"ID", 'field': "ID"}, 
                {'label':"Name",'field':"Name"}, 
                {'label':"Email", 'field':"Email"}],
                row_key="ID", 
                rows=data)

        async def get_users_list():
            """
            Fetch the list of users from the backend API and populate the table.
            """
            nonlocal users_list

            users_list.clear()
            users_list.extend(await User.all())
            userTable.refresh()

        userTable()
        await get_users_list()
        ui.button("refresh users", on_click=get_users_list)
        
        # meals

        ui.label("Debug Page: Meals List")
        meals_list = []

        @ui.refreshable
        def mealsTable():
            # Table to display users
            nonlocal meals_list

            data = []

            for meal in meals_list:
                data.append({
                    'ID': meal.id, 
                    'Url': meal.url, 
                    'Name': meal.name,
                    'Category': meal.category,
                    'Difficulty': meal.difficulty,
                    'Healthiness': meal.healthiness,
                    'Score': meal.score,
                })

            ui.table(columns=[
                {'label':"ID", 'field': "ID"}, 
                {'label':"Url",'field':"Url"}, 
                {'label':"Name", 'field':"Name"},
                {'label':"Category", 'field':"Category"},
                {'label':"Difficulty", 'field':"Difficulty"},
                {'label':"Healthiness", 'field':"Healthiness"},
                {'label':"Score", 'field':"Score"},],
                row_key="ID", 
                rows=data)

        async def get_meals_list():
            """
            Fetch the list of users from the backend API and populate the table.
            """
            nonlocal meals_list

            if not await Meal.filter(name='tiramisu').exists():
                await create_meal('tiramisu', 'test.com', 'Dessert', 3, 1)

            meals_list.clear()
            meals_list.extend(await Meal.all())
            mealsTable.refresh()

        mealsTable()
        await get_meals_list()
        ui.button("refresh meals", on_click=get_meals_list)

        

# run app
ui.run(dark=True, storage_secret="super secret")
