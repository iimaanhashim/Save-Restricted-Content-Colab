import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7578977444:AAGWYESi99c4it5woaL9-j2Y6-NI3GDjBkE")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "17461958"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0f083cb4779252f82b99f5c644274624")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://khaanbarwaani:qL47JyUNrzSRp2Aj@cluster0.qgucx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
