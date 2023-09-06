from pathlib import Path

app_dir: Path = Path(__file__).parent.parent

# bot = Bot(config.bot_token, parse_mode=types.ParseMode.HTML)
#
# # Without storage
# dp = Dispatcher(bot)

# storage = RedisStorage.from_url(config.redis.url)
# dp = Dispatcher(bot, storage=storage)
