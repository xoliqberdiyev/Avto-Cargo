import requests, base64

from django.conf import settings


class Atmos:
    def __init__(self, terminal_id = None):
        self.consumer_key = settings.CONSUMER_KEY
        self.consumer_secret = settings.CONSUMER_SECRET
        self.terminal_id = terminal_id
        self.store_id = settings.STORE_ID
    
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
        }
        data = {
            'amount': amount,
            'account': str(account),
            'store_id': f'{self.store_id}'
        }

        res = requests.post(url, headers=headers, json=data)
        return res.json()
        # try:
        #     data = res.json()
        # except Exception as e:
        #     raise ValueError(f"Invalid JSON response: {res.text}") from e

        # if data.get('result', {}).get('code') == 'OK':
        #     return data
        # return None
    
    def generate_url(self, transaction_id, redirect_url):
        url = f'http://test-checkout.pays.uz/invoice/get?storeId={self.store_id}&transactionId={transaction_id}&redirectLink={redirect_url}'
        access_token = self.login()
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        print(url)
        res = requests.post(url, headers=headers)
        return res.json()

    