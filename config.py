
import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBEtz_Lx37h_utho4SrArASwUUOtuqEP7dYmO5JQvApu5fm_rQXDFAHavHikjOVU4SGM_NDl6mN6qzPnVdA4jCAMClVoYH6aR-6HBJtk9SOEpyyuTwBCuyM38Xe_k3xefJikuI9CL5ErhauUI4O0n8zBlrmxboj25kb-_rgFAZdMBNJYPuIZN7L5lxXmakohC09htThTebVnVHWeOCjj4eB1vNYO8cBQlxSZYhXDlbvflfEh8msg-FxmVyBf5mltQAUsCnT9SlFFRwQ-FmfkSdW5GCwNc2AUbq3oEYp_k2-CbsiyRrt3p2FBeRCRyaPu8zJvCB78zYzPx87GBEYNqVrdCqCJAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1909102195:AAEbJIvqPKShOjvJat9EFMuPm3Dc8DGfg34")
BOT_NAME = getenv("BOT_NAME", "SHERSID")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DaisyXupdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", "7159660"))
API_HASH = getenv("API_HASH", "e1d5bfd2975078a56213605ce0d7f550")
BOT_USERNAME = getenv("BOT_USERNAME", "SHER_MUSICBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Sher_Vc")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DaisySupport_Official")
PROJECT_NAME = getenv("PROJECT_NAME", "DaisyXMusic v4")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamOfDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
