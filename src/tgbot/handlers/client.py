from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from src.tgbot.states.user import MainMenu

router = Router()


@router.message(CommandStart(), StateFilter('*'))
async def command_start(
        message: Message,
        dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(
        state=MainMenu.MAIN_MENU,
        mode=StartMode.RESET_STACK
    )
