from nicegui import ui
from datetime import datetime
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

 
mood_log = [] # list that store dictionaries of user ID, mood, and timestamp
mood_log_visible = False

def toggle_mood_log_visible():
    global mood_log_visible
    mood_log_visible = not mood_log_visible
    show_mood_log.refresh()

def log_mood(user_id, mood):
    global mood_log
    # generate a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mood_log.append({"user_id": user_id, "mood": mood, "timestamp": timestamp}) # save the mood locally
    ui.notify(f"Mood '{mood}' logged successfully at {timestamp}!") # notify the user
    show_mood_log.refresh()

# building ui
ui.label("Log your mood")
user_id_input = ui.input(label="User ID", placeholder="Enter your name")
mood_dropdown = ui.select(["happy", "sad", "tired"], label="Select Mood")
ui.button("Log Mood", on_click=lambda: log_mood(user_id_input.value, mood_dropdown.value))

# displaying the logged moods
@ui.refreshable
def show_mood_log():
    global mood_log_visible
    global mood_log
    if mood_log_visible:
        ui.label("Mood Log:")
        for entry in mood_log:
            ui.label(f"{entry['timestamp']} - User {entry['user_id']} felt {entry['mood']}.")

ui.button("View Mood Log", on_click=toggle_mood_log_visible)

show_mood_log()

ui.run()
