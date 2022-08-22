import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "8913469"))
API_HASH = getenv("API_HASH", "b3f7cb5deefe1cf33bebee944915061b")
BOT_TOKEN = getenv("BOT_TOKEN", "2124064704:AAG-_oWI2-08SAgg1GbrU45OayzAHepIdAk")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQB11qP7xaOX6mI3Zz9lfuhTPhZWbEBWz-NyiWhhiDIf2eLfTWi7EPyRwcXj0UBDFSKXeJmG0hy6q8Q2mod57kLG9Mwz_Z_zbqdqr_36QHhauSEtzOWpwUDTbq_w44x05-UYEj3EIrPogF_Tff-0aw7NWdZARk4sotHR3fn4ea9sDh8hsRyiF77bIDKcYZXaYhIlrQURKN2pJ3lTYLCZEmucZE7SogqT6KDDS-P8aSMNn7Q4ZzuwlzZIWt_kCJ35JiSvYhEgSNvl9mKN6g4hftCKuGw_vc3XEGTFFFxfTp4Mb9_WRTg4ql4QP7VXTopGRXxpIawBR4bRGnoeaZlxj3TUeArx6QA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES"? "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5486269467").split()))
