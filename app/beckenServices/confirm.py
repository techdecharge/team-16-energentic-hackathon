import requests
import json
import time
import uuid
from app.config import BAP_CLIENT_URL, DFP_DOMAIN, DFP_VERSION, BAP_ID, BPP_ID,BAP_NETWORK_URL, BPP_NETWORK_URL

url = f"{BAP_CLIENT_URL}/confirm"


def confirm_selection(provider_id, item_id):
    payload = json.dumps({
      "context": {
        "domain": DFP_DOMAIN,
        "action": "confirm",
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
        "order": {
          "provider": {
            "id": provider_id
          },
          "items": [
            {
              "id": item_id
            }
          ],
          "fulfillments": [
            {
              "id": "616",
              "customer": {
                "person": {
                  "name": "Lisa"
                },
                "contact": {
                  "phone": "876756454",
                  "email": "LisaS@mailinator.com"
                }
              }
            }
          ]
        }
      }
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
