Quickstart
==========
These here outline some of the basis for getting started with expo.

Installing
----------
Installing expo isn't that hard! so let's get started with it.

First you will want to install hikari via pip: ::

        # windows
        pip install hikari
        # linux & mac
        python3 -m pip install hikari

Then once your done with that, 
you can install hikari-expo: ::

        # windows
        pip install hikari-expo
        # linux & mac
        python3 -m pip install hikari-expo

and now you have hikari and expo installed!
this should be enough to now go to the next step.

Creating a bot
--------------
Creating a bot with expo is as easy as cake

First you would want to import `expo.commands`: ::

        from expo import commands
    
Then define your bot as existant: ::

        bot = commands.Bot(token="my_bot_token")

now just add this to start your bot: ::

        bot.run()

and thats it! you should now get the expo boot message.

if you run into any errors during this process 
please go to the :resource:`hikari discord server <discord>`