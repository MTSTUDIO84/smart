import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps.
API_ID = int(getenv("API_ID", "28294093"))
API_HASH = getenv("API_HASH", "f24d982c45ab2f69a6cb8c0fee9630bd")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7569306898:AAHYH63zVYJtl_qIw31Lvs87wXu69c3127I")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","ll_KSD_ll")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "Kittu_music_robot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "Kittu")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , "itz_m3_kittu")
EVALOP = list(map(int, getenv("EVALOP", "8142003954  8142003954").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Riya9797:Riyamusiczxbot@cluster0.eyy5z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 170000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002302799359))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 8142003954))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

YTPROXY_URL = getenv("YTPROXY_URL", 'https://tgapi.xbitcode.com') ## E.G https://yt.okflix.
YT_API_KEY = "xbit_0000968756403419024924"
COOKIES_URL=getenv("COOKIES_URL" , "https://gist.githubusercontent.com/sparrow9616/f29fc6588086a3c72d92dd9c03773350/raw/4229f3f4aab4a6693fc0794d136d30f54d67ae85/gistfile1.txt")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ifgovtjoftibcdjpvd8nfiokbfobffob0vrb8bd/pallavi1",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Riya_Network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/KittuSupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get @tmm_string_bot session from @tmm_STRING_BOT
STRING1 = getenv("STRING_SESSION", "BQGvu80AFK9sNjc9-kC9oAfpGJ9gif149I8z9RfqwreO8vUb0IsIQKJnxuNzEg6bwwNj5Nq5XpDMZYBnUxS1_IuggrTno-aZ_Hl2hzxCMu9BWe8mtGn3RLwvhWYap_FUGwTjsYkEvPd7f0YhnjXyBmDj5_PT-XtJQIym9k_kj_abjrtFOQRP1OxVjlAL9xJOLF7Z-uXFQxh7tg_3ItKU17g7scnP7fIz0SpDjGEkbNRR3-oHQRyEwoXArjqS-el1Yf5CMo_MAGKkik7BL2gRY2ODXrOP3Sqk1DhtaJF_7iKgmJIfoKjeaw-I7PE-ZLg9po5PhMs60lM5N1CjfCh3C_Q9uGftSAAAAAHKXA1NAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
AMBOT = [
    "💞",
    "🔎",
    "🔍",
    "🧪",
    "💣",
     "⚡️",
     "🔥",
     "🕺",
     "🎩",
     "🌈",
     "👀",
     "🥂",
     "🍾",
    "🥃",
    "🥤",
    "🍽",
    "🍭",
    "🥀",
    "🦋",
    "🚓",
    "🙏🏻",
    "🚀",
    "💎",
    "🔮",
    "🪄",
    "💌",
    "👻",
    "💤",
    "🧨",
    "🦋"
]
AMOP = ["ʜᴇʟʟᴏ {0}, 🥀\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┗━━━━━━━━━━━━━━━━━⧫"]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/g3ae56.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/xt2rme.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/78ac6fc48e240895e5ec8.jpg"
STATS_IMG_URL = "https://graph.org/file/6abe3a913bf645b5b89ce.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/443076090048170968b90.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/0c40d1fc5f17c524a6c16.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/bc0844a1139b5214ba78f.jpg"


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
