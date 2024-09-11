# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23303247"))
API_HASH = getenv("API_HASH", "23623f737dc15708708c65a7297e1510")
BOT_TOKEN = getenv("BOT_TOKEN", "6398304554:AAHJmnH73p0DUh7TAQlW0XTsZAO1BG19kNQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6335525003").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Radha:Radha@cluster0.6gat6fo.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1002166457568")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002187998395"))
