import os
from dotenv import load_dotenv

load_dotenv()

APPLICATION_HOST = os.getenv('APPLICATION_HOST')
APPLICATION_PORT = int(os.getenv('APPLICATION_PORT'))
BECKEN_BASE_URL = os.getenv('BECKEN_BASE_URL')
BAP_ID = os.getenv('BAP_ID')
BAP_NETWORK_URL = os.getenv('BAP_NETWORK_URL')
BAP_CLIENT_URL = os.getenv('BAP_CLIENT_URL')
BPP_ID = os.getenv('BPP_ID')
BPP_NETWORK_URL = os.getenv('BPP_NETWORK_URL')
BPP_CLIENT_URL = os.getenv('BPP_CLIENT_URL')
DFP_DOMAIN = os.getenv('DFP_DOMAIN')
DFP_VERSION = os.getenv('DFP_VERSION')
WORLD_ENGINE_URL = os.getenv('WORLD_ENGINE_URL')