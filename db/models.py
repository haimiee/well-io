from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)

class Mood(models.Model):
    id = fields.IntField(pk=True)
    userID = fields.IntField()
    mood = fields.CharField(max_length=255) # sad/happy/mad/tired
    date = fields.DatetimeField(auto_now_add=True)

class Meal(models.Model):
    id = fields.IntField(pk=True)
    url = fields.CharField(max_length=1000)
    category = fields.CharField(max_length=255)  # breakfast/lunch/dinner/snack/dessert
    quick = fields.BooleanField(default=False)  # true for "easy" meals
    healthy = fields.BooleanField(default=False)  # true for "eat healthy" goal
    treat = fields.BooleanField(default=False)  # true for "treat yourself" goal
    score = fields.IntField(default=0)  # adjusted by feedback

class Goal(models.Model):
    id = fields.IntField(pk=True)
    userID = fields.IntField()
    goal = fields.CharField(max_length=255)  # e.g., "treat myself", "eat healthy"
    timestamp = fields.DatetimeField(auto_now_add=True)

class Feedback(models.Model):
    id = fields.IntField(pk=True)
    userID = fields.IntField()
    mealID = fields.IntField(null=True)
    activityID = fields.IntField(null=True)
    rating = fields.IntField() # -1, 0, or 1

class MealLog(models.Model):
    id = fields.IntField(pk=True)
    userID = fields.IntField()
    mealID = fields.IntField()
    timestamp = fields.DatetimeField(auto_now_add=True)







