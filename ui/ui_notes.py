from typing import List, Dict
from nicegui import ui
from datetime import datetime
from db.models import *
# import random

# def random_date():
#     start, end = datetime.datetime(year=2020, month=1, day=1), datetime.datetime(year=2025, month=1, day=1)
#     """Generate a random datetime between `start` and `end`"""
#     return start + datetime.timedelta(
#         # Get a random amount of seconds between `start` and `end`
#         seconds=random.randint(0, int((end - start).total_seconds())),
#     )


# moods = ["sad", "happy", "mad", "tired"]

# data = [[ random_date(), moods[random.randint(0, len(moods) - 1)] ] for _ in range(30)]
# data.sort(key=lambda x: x[0])
# # data = [f"text{x}" for x in range(5)]
# # data = [f"mood is {moods[random.randint(0,len(moods)-1)]}" for x in range(5)]

# with ui.grid(columns=2):
#     for entry in data:
#         ui.label(entry[0])
#         ui.label(entry[1])
    

# # with ui.row():
# #     for j in range(4):
# #         with ui.column():
# #             for d in range(10):
# #                 with ui.card():
# #                     rand_mood = moods[random.randint(0,len(moods)-1)]
# #                     ui.label(f"mood is {rand_mood}")

# ui.run()

 
# mood_log = []  # list that stores dictionaries of user ID, mood, and timestamp
# mood_log_visible = False  # boolean flag to control the visibility of the mood log

# def toggle_mood_log_visible():
#     global mood_log_visible
#     mood_log_visible = not mood_log_visible  # flip the visibility flag
#     show_mood_log.refresh()  # refresh the mood log UI

# def log_mood(user_id, mood):
#     global mood_log
#     # generate a timestamp
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # generate timestamp
#     mood_log.append({"user_id": user_id, "mood": mood, "timestamp": timestamp}) # save the mood locally
#     ui.notify(f"Mood '{mood}' logged successfully at {timestamp}!") # notify the user
#     show_mood_log.refresh()

# # building ui
# ui.label("Log your mood")
# user_id_input = ui.input(label="User ID", placeholder="Enter your name")
# mood_dropdown = ui.select(["happy", "sad", "tired"], label="Select Mood")
# ui.button("Log Mood", on_click=lambda: log_mood(user_id_input.value, mood_dropdown.value))
# goal_dropdown = ui.select(["Eat healthy", "Treat myself", "Easy meal"], label="Select Goal")
# ui.button("Set Goal", on_click=lambda: log_mood(user_id_input.value, goal_dropdown.value))


# # displaying the logged moods
# @ui.refreshable
# def show_mood_log():
#     global mood_log_visible
#     global mood_log
#     if mood_log_visible:
#         ui.label("Mood Log:")
#         for entry in mood_log:
#             ui.label(f"{entry['timestamp']} - User {entry['user_id']} felt {entry['mood']}.")

# ui.button("View Mood Log", on_click=toggle_mood_log_visible)

# show_mood_log()

# ui.run()


### Sample data for music suggestions based on mood

# mood_data = {
#     "Happy": {
#         "playlist": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
#         "activity": "Dance to your favorite song!",
#         "quote": "Happiness is not by chance, but by choice."
#     },
#     "Sad": {
#         "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro",
#         "activity": "Journal your thoughts.",
#         "quote": "Tough times never last, but tough people do."
#     },
#     "Stressed": {
#         "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ",
#         "activity": "Try 5 minutes of meditation.",
#         "quote": "Breathe. It’s just a bad day, not a bad life."
#     },
#     "Calm": {
#         "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWV7EzJMK2FUI",
#         "activity": "Enjoy a walk outdoors.",
#         "quote": "Calmness is the cradle of power."
#     },
# }

# # main UI page
# @ui.page("/")
# def mood_page():
#     ui.label("How are you feeling today?").style("font-size: 24px; margin-bottom: 10px;")
    
#     # dropdown for mood selection
#     mood_dropdown = ui.select(["Happy", "Sad", "Stressed", "Calm"], label="Select your mood")
    
#     # button to fetch suggestions
#     def suggest():
#         mood = mood_dropdown.value
#         if mood:
#             suggestion = mood_data[mood]
#             # display the suggestions
#             ui.notify(f"Playlist: {suggestion['playlist']}")
#             ui.label(f"Activity: {suggestion['activity']}").style("margin-top: 10px;")
#             ui.label(f"Quote: {suggestion['quote']}").style("font-style: italic;")
#         else:
#             ui.notify("Please select a mood first!", color="red")
    
#     ui.button("Get Suggestions", on_click=suggest).style("margin-top: 20px;")

# # run the NiceGUI app
# ui.run()

# @ui.page('/')
# async def main_page():
#     async def add_meal(name, url, category, difficulty, healthiness):
#         await Meal.create(
#             name=name,
#             url=url,
#             category=category,
#             difficulty=difficulty,
#             healthiness=healthiness,
#         )
#         print(f"Meal '{name}' added to the database.")

#     async def suggest_meal(category):
#         # Query meals in the given category, ordered by healthiness
#         meal = await Meal.filter(category=category).order_by("-healthiness").first()
#         if meal:
#             return {
#                 "id": meal.id,
#                 "name": meal.name,
#                 "url": meal.url,
#                 "difficulty": meal.difficulty,
#                 "healthiness": meal.healthiness,
#             }
#         return None

#     async def log_feedback(user_id, meal_id, rating):
#         await Feedback.create(user_id=user_id, meal_id=meal_id, rating=rating)
#         print(f"Feedback logged for user {user_id}, meal {meal_id}, rating {rating}.")

# list_of_users: List[User] = []

# async def create_user(name, email):
#     if await User.filter(email=email).exists():
#         ui.notify(f"Failed to create user, email \"{email}\" ia already taken.", type="negative", close_button=True)
#     else:
#         new_user = await User.create(name=name, email=email)
#         ui.notify("User created!")

# @ui.page('/signup')
# async def signup_page():
#     ui.label("Sign Up")
#     user_name_input = ui.input(label="User Name", placeholder="Enter your name")
#     user_email_input = ui.input(label="User Email", placeholder="Enter your email")
#     ui.button("Sign Up", on_click=lambda: create_user(user_name_input.value, user_email_input.value))

# @ui.page('/debug')
# async def debug_page():
#     ui.label("Debug Page: Users List")

#     # Table to display users
#     table = ui.table(columns=["ID", "Name", "Email"], rows=[])

#     async def get_users_list():
#         """
#         Fetch the list of users from the backend API and populate the table.
#         """
#         nonlocal list

# ui.run()