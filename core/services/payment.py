import requests
import base64


class Atmos:
    def __init__(self, consumer_key, consumer_secret, terminal_id, store_id):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.terminal_id = terminal_id
        self.store_id = store_id
    
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
        url = 'https://apigw.atmos.uz/token'
        res = requests.post(url, headers=headers, data=data)
        if 'access_token' in res.json():
            return res.json()['access_token']
        else:
            return None
    
    def create_transaction(self, amount, account):
        access_token = self.login()
        
        url = 'https://apigw.atmos.uz/merchant/pay/create'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'amount': amount,
            'account': account,
            'terminal_id': self.terminal_id,
            'store_id': self.store_id
        }

        res = requests.post(url, headers=headers, data=data)
        if res.json()['result']['code'] == 'OK':
            return res.json()
        else:
            return None
    
    def generate_url(self, transaction_id, redirect_url):
        url = f'https://test-checkout.pays.uz/invoice/get?storeId={self.store_id}&transactionId={transaction_id}&redirectLink={redirect_url}'

        res = requests.get(url)
        return res.json()

    