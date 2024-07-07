# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21658697"))
API_HASH = getenv("API_HASH", "de14ead808f57b3825f74a8be57868c5")
BOT_TOKEN = getenv("BOT_TOKEN", "7347946943:AAF1GOMRtDKnyzyOPVHOO-y-nJvGY2adScI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5573656801").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://dharmendrasaini4435:sahilkhan@cluster0.pcbftgb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
