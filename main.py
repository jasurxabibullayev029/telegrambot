import asyncio
import logging
import os
import sys
from pathlib import Path

# Ensure project root directory is in sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from database import db
from handlers import setup_routers
from middlewares import BlockedUserMiddleware, RequiredChannelsMiddleware
from middlewares.inject_bot import InjectBotMiddleware

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


async def on_startup(bot: Bot):
    await db.init()
    me = await bot.get_me()
    channels = await db.get_required_channels()
    logger.info("Bot started: @%s (Prezent7AI)", me.username)
    logger.info("Majburiy kanallar: %d ta", len(channels))
    for ch in channels:
        logger.info("  - %s (%s)", ch.get("channel_title"), ch.get("channel_id"))


async def main():
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN not set! Create .env file from .env.example")
        sys.exit(1)

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage())

    inject_bot = InjectBotMiddleware(bot)
    dp.message.outer_middleware(inject_bot)
    dp.callback_query.outer_middleware(inject_bot)
    dp.message.outer_middleware(BlockedUserMiddleware())
    dp.callback_query.outer_middleware(BlockedUserMiddleware())
    dp.message.outer_middleware(RequiredChannelsMiddleware())
    dp.callback_query.outer_middleware(RequiredChannelsMiddleware())

    dp.include_router(setup_routers())

    dp.startup.register(on_startup)

    logger.info("Starting Prezent7AI bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
