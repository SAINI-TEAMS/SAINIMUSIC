import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("12380656"))
API_HASH = getenv("d927c13beaaf5110f25c505b7c071273")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7468224439:AAEGXiQeoK_iRjHwFFIu1In574UDV1sLGvs")
BOT_USERNAME = getenv("BOT_USERNAME" , "@SAINI_MUSICBOT")
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://Suraj43:Suraj43@suraj.0bg0zuc.mongodb.net/?retryWrites=true&w=majority",)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 699999999999990))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002032619938", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("6790503262", ))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SURAJ-SAINI-DEV/SAINIMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/quizbys")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+HsKdS8nBrTs1Mzc1")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQAOIQqGis1V4DWQjNCrDiuwjZhtdhPGzhcH_VrnHwu2byShQJH-2NBi-UU8tOhHUH_uZSkuMnq8BpbDVAc1InZwCtuL8hyky2XiH4l7IMtdLFk8MZI1tPaywYlfbZ5VkQTls7QL-PhNXZ0tVK1FyhH6AZF0F7ogQP7369x_81pvpvCfzLoPKCN7cLRyKMhiBIR7fCWrBWd8ZOlWpr1q98VZ0LV9H6UD8eInn_ZPVMyiMNn2mb2vXZEeSdkGX_V1Imxzf5c-8onEAoV0dmXvn7qb06AetPYg5-a_tHGu3rvE8te78HyZ4C-CJiaYgJBxQKAe0ul-rcQXPB4DXvIh57bZAAAAAXitP3AA",)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/ecfd3fd44af1fb2c361b4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/c100d2409d76468ecf291.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
