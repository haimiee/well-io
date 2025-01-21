from tortoise import Tortoise

DATABASE_URL = "sqlite://db.sqlite3"  # can change this to PostgreSQL

# initialize database
async def init_db():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models": ["db.models"]},  # path to models
    )
    await Tortoise.generate_schemas()

