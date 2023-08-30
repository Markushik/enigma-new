from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Jinja, Const

from src.tgbot.states.user import MainMenu

main_menu = Dialog(
    Window(
        Jinja("Hello"),
        Button(
            text=Const("Tap!"), id="tap_id"
        ),
        state=MainMenu.MAIN_MENU
    )
)
