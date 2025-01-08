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
    category = fields.CharField(max_length=255) # breakfast/lunch/dinner/snack/dessert
    difficulty = fields.IntField() # 1-5
    healthiness = fields.IntField() # 1-5
    score = fields.IntField()

class Feedback(models.Model):
    id = fields.IntField(pk=True)
    userID = fields.IntField()
    mealID = fields.IntField(null=True)
    activityID = fields.IntField(null=True)
    rating = fields.IntField() # -1, 0, or 1






