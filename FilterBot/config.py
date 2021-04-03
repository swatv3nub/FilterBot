import os

APP_ID = int(os.environ.get("APP_ID"))

API_HASH = os.environ.get("API_HASH")

BOT_TOKEN = os.environ.get("BOT_TOKEN")

DB_URI = os.environ.get("DB_URI")

USER_SESSION = os.environ.get("USER_SESSION")

# For Local Hosting, Make the above Vars as Comments and make the lower ones uncommented and correctly fill them.

#APP_ID = 19288

#API_HASH = "my.telegram.org"

#BOT_TOKEN = "@BotFather"

#DB_URI = "mongodb.com"

#USER_SESSION = "@PyrogramStringBot"
