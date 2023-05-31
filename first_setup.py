import json

with open("config.json", "rw") as file:
    data = json.load(file)

data["token"] = input("Please enter your bot token: ")
data["test-guild"] = int(input("Please enter your test guild id: "))
data["client-id"].append(int(input("Please enter your user id: ")))
data["bot-testing"] = input("Please enter your bot testing channel id (also used for startup messages): ")
data["prefix"]["std"] = input("Please enter your prefix: ")
print("That's it, have fun using the bot!")