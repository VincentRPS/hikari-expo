# hikari-expo
expo is a extension for hikari providing a meriad of useful features.

# Warning
expo is still under heavy development and is not meant for public use,
however if you do use it expect frequent breaking changes.

# Installing
If you want to install the stable version just do the following command:
```sh
pip install -U hikari-expo
```
If you want to install the dev version just do the following command:
```sh
pip install -U git+https://github.com/VincentRPS/hikari-expo
```
Little note, You will want to have [git](https://git-scm.com) to install the dev version.

To clone the repo just do the following set of commands:
```sh
git clone https://github.com/VincentRPS/hikari-expo
cd hikari-expo
```

# Issues
for any issue please report it to our issue tracker, [here](https://github.com/VincentRPS/hikari-expo/issues/new)

# Quick Example
Down below is a quick example of the extension.
```py
from expo import commands  # import the commands module.

bot = commands.Bot("my_bot_token")  # initiate the bot instance.

bot.run()  # Start the bot
```

# Useful links
the [hikari discord](https://discord.gg/3kDAzaM36b)

the [hikari docs](https://www.hikari-py.dev/hikari/index.html)

the [discord developers](https://discord.gg/discord-developers) server.
