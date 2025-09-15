import requests, base64

from django.conf import settings


class Atmos:
    def __init__(self, terminal_id = None):
        self.consumer_key = settings.CONSUMER_KEY
        self.consumer_secret = settings.CONSUMER_SECRET
        self.terminal_id = terminal_id
        self.store_id = settings.STORE_ID
        self.global_consumer_key = settings.GLOBAL_CONSUMER_KEY
        self.global_consumer_secret = settings.GLOBAL_CONSUMER_SECRET
        self.global_store_id = settings.GLOBAL_STORE_ID

    def login(self):
        credentials = f"{self.consumer_key}:{self.consumer_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = {
            "grant_type": "client_credentials"
        }
        url = 'https://partner.atmos.uz/token'
        res = requests.post(url, headers=headers, data=data)
        return res.json()['access_token']
    
    def create_transaction(self, amount, account):
        access_token = self.login()

        url = 'https://partner.atmos.uz/merchant/pay/create'
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        data = {
            'amount': int(amount) * 100,
            'account': str(account),
            'store_id': f'{self.store_id}'
        }

        res = requests.post(url, headers=headers, json=data)
        return res.json()
    
    def generate_url(self, transaction_id, redirect_url):
        url = f'http://test-checkout.pays.uz/invoice/get?storeId={self.store_id}&transactionId={transaction_id}&redirectLink={redirect_url}'
        return url


    # Visa/MasterCard
    def login_global_payment(self):
        credentials = f"{self.global_consumer_key}:{self.global_consumer_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = {
            "grant_type": "client_credentials"
        }
        url = 'https://apigw.atmos.uz/token'
        res = requests.post(url, headers=headers, data=data)
        return res.json()['access_token']
    
    def global_payment(self, request_id, account, amount):
        access = self.login_global_payment()
        url = 'https://apigw.atmos.uz/checkout/invoice/create'
        headers = {
            'Authorization': f'Bearer {access}',
            'Content-Type': 'application/json',
        }
        data = {
            "request_id": request_id,
            "store_id": self.global_store_id,
            "account": str(account),
            "amount": amount * 100,
            "success_url": "https://wisdom.uz",
        }

        res = requests.post(url=url, headers=headers, json=data)
        if res.status_code == 200:
            return res.json()
        else:
            return res.json()