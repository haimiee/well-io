from nicegui import app
from tortoise import Tortoise

from db.models import User
from ui.ui import run_ui

async def init_database():
    await Tortoise.init(db_url="sqlite://db.sqlite", modules={"models": ["db.models"]})
    await Tortoise.generate_schemas()
    # await User.all().delete()

if __name__ in {"__main__", "__mp_main__"}:
    app.on_startup(init_database)
    run_ui()

