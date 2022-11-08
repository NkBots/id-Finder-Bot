import os

class Config(object):

    # get bot token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5543668594:AAE8IAWuv6kTaeGAXBQf_rh-bJscJ8IwNFo")

    # The Telegram API things
    # Get these values from my.telegram.org
    API_ID = int(os.environ.get("API_ID", "10412514"))
    API_HASH = os.environ.get("API_HASH", "4d55a7064ad72adcfa8944f505453a8c")
    # Update Channel Username
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Nkbots")
