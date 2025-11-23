from plaid.api import plaid_api
from plaid.api_client import ApiClient
from plaid.configuration import Configuration
from plaid.model.item_remove_request import ItemRemoveRequest
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
SECRET = os.getenv("PLAID_SECRET")


# CONFIGURE THE CLIENT
config = Configuration(
    host="https://sandbox.plaid.com",
    api_key={
        "clientId": CLIENT_ID,
        "secret": SECRET,
    }
)

api_client = ApiClient(config)
client = plaid_api.PlaidApi(api_client)

# REQUEST TO REMOVE ITEM
request = ItemRemoveRequest(
    access_token="access-sandbox-92ed2019-5945-4cf8-907f-2e1cb6bec1e1"
)

response = client.item_remove(request)

print(response)
