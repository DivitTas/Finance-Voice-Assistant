from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from plaid.api import plaid_api
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from datetime import datetime, timedelta, date


import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")
PLAID_ENV = "sandbox"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
access_token = ACCESS_TOKEN

configuration = Configuration(
    host="https://sandbox.plaid.com",
    api_key={
        "clientId": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET
    }
)

api_client = ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)


@app.get("/")
def home():
    return {"status": "Plaid FastAPI backend running"}


@app.post("/create_link_token")
def create_link_token():
    try:
        user = LinkTokenCreateRequestUser(client_user_id="user123")

        request = LinkTokenCreateRequest(
    client_name="Divits Assistant",
    country_codes=[CountryCode("US")],
    language="en",
    user=user,
    products=[Products("transactions")]
)

        response = client.link_token_create(request)
        return response.to_dict()

    except Exception as e:
        print("\nPLAID ERROR:", e, "\n")
        return {"error": str(e)}


@app.post("/exchange_public_token")
def exchange_public_token(public_token: str):
    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=public_token
    )
    exchange_response = client.item_public_token_exchange(exchange_request)
    return {
        "access_token": exchange_response.access_token
    }


@app.post("/get_accounts")
def get_accounts(access_token: str):
    request = AccountsGetRequest(
        access_token=access_token
    )
    response = client.accounts_get(request)
    return response.to_dict()


from plaid.model.transactions_get_request import TransactionsGetRequest
from datetime import datetime, timedelta

@app.post("/get_transactions")
def get_transactions():
    start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    end_date = datetime.now().strftime("%Y-%m-%d")

    request = TransactionsGetRequest(
        access_token=ACCESS_TOKEN,
        start_date=start_date,
        end_date=end_date
    )

    response = client.transactions_get(request)
    return response.to_dict()



@app.post("/sandbox_public_token")
def sandbox_public_token():
    try:
        request = SandboxPublicTokenCreateRequest(
            institution_id="ins_109508", 
            initial_products=[Products("transactions")]  
        )
        response = client.sandbox_public_token_create(request)
        return response.to_dict()
    except Exception as e:
        return {"error": str(e)}
    

@app.post("/check_balance")
def check_balance(user_id: str):
    # Placeholder implementation
    #abstracted logic to get access token, using hardcoded pregenerated sandbox token just for demo
    #access_token = get_access_token_for_user(user_id)

    
    request = AccountsGetRequest(access_token=access_token)
    response = client.accounts_get(request)
    accounts = response.to_dict()["accounts"]


    savings_accounts = [  #Check balance returns only savings accounts
    {
        "name": acc["name"],
        "current": acc["balances"]["current"],
        "available": acc["balances"]["available"],
        "official_name": acc.get("official_name"),
        "account_id": acc["account_id"],
    }
    for acc in accounts 
    if acc["type"] == "depository" and acc.get("subtype") == "savings"
    ]

    return {"savings_accounts": savings_accounts}
    
def simplify_transactions(data):
    simplified = []
    txns = data.get("transactions", [])
    for txn in txns:
        simplified.append({
            "merchant": txn.get("merchant_name") or txn.get("name"),
            "amount": txn.get("amount"),
            "date": txn.get("date"),
        })
    simplified.sort(key=lambda x: x["date"], reverse=True)
    return simplified


@app.post("/get_accounts")
def get_accounts(access_token: str):
    request = AccountsGetRequest(
        access_token=access_token
    )
    response = client.accounts_get(request)
    return response.to_dict()


@app.post("/sandbox_public_token")
def sandbox_public_token():
    try:
        request = SandboxPublicTokenCreateRequest(
            institution_id="ins_109508", 
            initial_products=[Products("transactions")]  
        )
        response = client.sandbox_public_token_create(request)
        return response.to_dict()
    except Exception as e:
        return {"error": str(e)}
    

@app.post("/check_balance")
def check_balance(user_id: str):
    # Placeholder implementation
    #abstracted logic to get access token, using hardcoded pregenerated sandbox token just for demo
    #access_token = get_access_token_for_user(user_id)

    
    request = AccountsGetRequest(access_token=access_token)
    response = client.accounts_get(request)

    # extract balances
    accounts = response.to_dict()["accounts"]


    savings_accounts = [  #Check balance returns only savings accounts
    {
        "name": acc["name"],
        "current": acc["balances"]["current"],
        "available": acc["balances"]["available"],
        "official_name": acc.get("official_name"),
        "account_id": acc["account_id"],
    }
    for acc in accounts 
    if acc["type"] == "depository" and acc.get("subtype") == "savings"
    ]

    return {"savings_accounts": savings_accounts}
    
def simplify_transactions(data):
    simplified = []
    txns = data.get("transactions", [])
    for txn in txns:
        simplified.append({
            "merchant": txn.get("merchant_name") or txn.get("name"),
            "amount": txn.get("amount"),
            "date": txn.get("date"),
        })
    simplified.sort(key=lambda x: x["date"], reverse=True)
    return simplified

def fetch_transactions():
    start_date = date.today() - timedelta(days=30)
    end_date = date.today()

    print("\n--- FETCH TRANSACTIONS DEBUG ---")
    print("ACCESS TOKEN:", ACCESS_TOKEN)
    print("DATES:", start_date, end_date)

    request = TransactionsGetRequest(
        access_token=ACCESS_TOKEN,
        start_date=start_date,
        end_date=end_date
    )

    try:
        response = client.transactions_get(request)
        data = response.to_dict()
        print("PLAID SUCCESS:", data)
        return data
    except Exception as e:
        print("PLAID ERROR TYPE:", type(e))
        print("PLAID ERROR:", e)
        raise e
@app.post("/get_transactions")
def get_transactions_endpoint():
    return fetch_transactions()


@app.post("/get_recent_transactions")
def get_recent_transactions():
    raw = fetch_transactions()
    return simplify_transactions(raw)
