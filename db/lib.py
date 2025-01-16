from tortoise import Tortoise

DATABASE_URL = "sqlite://db.sqlite3"  # use SQLite for local testing, can switch to PostgreSQL later

async def init_db():
    """
    Initialize the database and create schemas if they do not exist.
    """
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models": ["db.models"]}  # points to the models file
    )
    await Tortoise.generate_schemas()  # Create database tables from models


async def close_db():
    """
    Close the database connection.
    """
    await Tortoise.close_connections()
