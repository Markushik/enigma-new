import asyncio

import structlog
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram_dialog import setup_dialogs

from config import settings
from src.tgbot.dialogs.main_menu.dialog import main_menu
from src.tgbot.handlers import client

logger = structlog.get_logger()


async def _main() -> None:
    await logger.ainfo("Preparing to launching...")

    storage = RedisStorage.from_url(
        url="redis://127.0.0.1:6379",
        key_builder=DefaultKeyBuilder(
            with_bot_id=True, with_destiny=True
        )
    )
    bot = Bot(
        token=settings.TOKEN,
        parse_mode=ParseMode.HTML
    )
    disp = Dispatcher(
        storage=storage,
        events_isolation=storage.create_isolation()
    )

    disp.include_router(client.router)
    disp.include_router(
        main_menu
    )

    setup_dialogs(disp)

    await logger.ainfo("Launching Bot")

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await disp.start_polling(bot)
    finally:
        await disp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(_main())
    except KeyboardInterrupt:
        logger.info("Shutdown Bot")
