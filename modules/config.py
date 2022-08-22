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
STRING_SESSION = getenv("STRING_SESSION", "1BVtsOJgBu8AtVc5cpSb0dO8WQGVgrkqVYuhGUePJE8I90weQoWDLName-OawgGlO3dRHCWjsk8SiC8r8yJSbTRPIi9Lt4w92hhOPHX3PYI-FMJ60LUJutRzolyTo-6mD9c0H50lZHtUEo_ib2oh-dkvPutBXStlq488eRWk4kNGaOQKAuI96dRVWJgBy53XHiQ-KKl3gfly_ZMRA0fM15zBGIr1E_ann8bdMd53cVDZI8lqgehyTliUp3LMgcZo7G0zISsVd89c0Yo7UEmmtKrNB4HejoqSegd-RTPl1u0f2cxrTp17UCGsMYWs8ZiKPNeKhy2j5rmsXW7vrqenzALwzzoHnXok=")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES"? "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5486269467 2013983209").split()))
