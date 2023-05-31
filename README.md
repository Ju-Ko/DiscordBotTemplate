# Python Discord Bot Template
This template bot is a really simple python bot for Discord using the rewrite of discord.py.
The bot uses extensions/cogs to keep similar commands in the same file.
The bot is configured for the usage of slash commands while still allowing the old text based commands.
To update the bot there is an update command for the owner that will pull content from a GitHub repository.
List of commands:
- get_update    to get the newest version from GitHub
- restart       to restart the bot while keeping the PID
- shutdwon      to shutdown the bot if neccessary, won't be able to restart until manual start
- sync          to sync all slash commands globally
- unsync        to unsync all slash commands globally

Everytime the bot is restarted all commands are synced to the test guild. This is not suggested, because the ratelimit is quite strict, but for easier development it is enabled.

## GitHub update
Your bot need a GitHub repository to be updated via the command.
Clone the repository in the directory of the bot on the server and you are ready to go!

## Contribution
Feel free to add code to this template as long as it is simple and beginer-friendly.

## Help
If you need help check out the discord.py server and ping JuKo#1045.
