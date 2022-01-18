# This example gives a simple starting bot.
from expo import commands

bot = commands.Bot(token="my_bot_token", command_prefix="!")

bot.run()
