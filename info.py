import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '26823235'))
API_HASH = environ.get('API_HASH', '5a1f8f94d3a79d3c650edce7f667c380')
BOT_TOKEN = environ.get('BOT_TOKEN', '6665782219:AAFYnRKdnutjN4Rx4_EVYGP9AWgu0Hk7Sb8')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6659090038 6056290459').split()]
USERNAME = environ.get('USERNAME', 'https://t.me/Dhruvmradiya')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002075513033'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/Nobi_Movies_Request')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002084096213').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://czaks:czlinksowner@cluster0.siuxfhq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://czaks:comymoviez@cluster0.cdow7e1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "czaks")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Aks')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002075513033'))
QR_CODE = environ.get('QR_CODE', 'https://t.me/Nobi_Movies_Request/7')

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1001987729563'))
URL = environ.get('URL', 'https://nobiakssujal-2a770e5b4981.herokuapp.com/')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002075513033'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/turtorialvideo/2")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/turtorialvideo/2")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "836d10a0655083cc1a383c79cac81b44be597b82")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "Krishnalink.com")
SHORTENER_API2 = environ.get("SHORTENER_API2", "e9365c39c9a8a6a9f6cc530385d90bb92b7e7bd9")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "zxlink.in")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-1001513688942'))
AUTH_REQ_CHANNEL = int(environ.get('AUTH_REQ_CHANNEL', '-1001513688942'))
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001987729563'))

# hastags request features
request_channel = environ.get('REQUEST_CHANNEL', '-1001987729563')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

# bot settings
IGNORE_WORDS = (list(os.environ.get("IGNORE_WORDS").split(",")) if os.environ.get("IGNORE_WORDS") else [])
IGNORE_WORDS=["movies", "Movies", ",", "episode", "Episode", "episodes", "Episodes", "south indian", "south indian movie", "South Indian Movie", "south movie", "South Movie", "South Indian", "web-series", "punjabi", "marathi", "hindi me bhejo", "hindi", "gujrati", "combined", "!", "kro", "jaldi", "Audio", "audio", "movi", "language", "Language", "Hollywood", "All", "all", "bollywood", "Bollywood", "South", "south", "HD", "hd", "karo", "Karo", "fullepisode", "please", "plz", "Please", "Plz", "send", "link", "Link", "full", "Full", "dabbed", "dubbed", "gujarati", "gujrati", "Gujarati", "Gujrati", "season", "Season", "web", "series", "Web", "Series", "webseries", "WebSeries", "upload", "HD", "Hd", "bhejo", "ful", "Send", "Bhejo"]
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
