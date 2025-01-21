from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)

class Meal(models.Model):
    id = fields.IntField(pk=True)
    url = fields.CharField(max_length=1000)
    name = fields.CharField(max_length=255)
    category = fields.CharField(max_length=255)  # breakfast/lunch/dinner/snack/dessert
    difficulty = fields.IntField()  # 1-5
    healthiness = fields.IntField()  # 1-5
    score = fields.IntField(default=0)  # adjusted by feedback

class Feedback(models.Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    meal_id = fields.IntField()
    rating = fields.IntField()  # -1 for thumbs down, 1 for thumbs up

class Mood(models.Model):
    id = fields.IntField(pk=True)
    userID = fields.IntField()
    mood = fields.CharField(max_length=255) # sad/happy/mad/tired
    timestamp = fields.DatetimeField(auto_now_add=True)

class Goal(models.Model):
    id = fields.IntField(pk=True)
    userID = fields.IntField()
    goal = fields.CharField(max_length=255)  # e.g., "treat myself", "eat healthy"
    timestamp = fields.DatetimeField(auto_now_add=True)