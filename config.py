import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6949246022:AAHCF2JY6ZLCDPItDC8Qx6O-hWAYt26hcYY")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27672739"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f48d0da94f2622364ab24eb0d911903c")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://khaanbarwaani:qL47JyUNrzSRp2Aj@cluster0.qgucx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
