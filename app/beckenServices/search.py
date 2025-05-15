import requests
import json
import time
import uuid
from app.config import BAP_CLIENT_URL, DFP_DOMAIN, DFP_VERSION, BAP_ID, BPP_ID,BAP_NETWORK_URL, BPP_NETWORK_URL

url = f"{BAP_CLIENT_URL}/search"

payload = json.dumps({
  "context": {
    "domain": DFP_DOMAIN,
    "action": "search",
    "location": {
      "country": {
        "code": "USA"
      },
      "city": {
        "code": "NANP:628"
      }
    },
    "version": DFP_VERSION,
    "bap_id": BAP_ID,
    "bap_uri": BAP_NETWORK_URL,
    "bpp_id": BPP_ID,
    "bpp_uri": BPP_NETWORK_URL,
    "transaction_id": str(uuid.uuid4()),
    "message_id": str(uuid.uuid4()),
    "timestamp": str(int(time.time()))
  },
  "message": {
    "intent": {
      "item": {
        "descriptor": {
          "name": "Program"
        }
      }
    }
  }
})
headers = {
  'Content-Type': 'application/json'
}


def send_search_request():
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
