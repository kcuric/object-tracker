from tracker.configuration import configuration

import requests
import json

def create_product_missing_report():
  data = {'productId': configuration.PRODUCT_ID}
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  response = requests.post(
    f'{configuration.SERVER_URL}{configuration.ENDPOINT}',
    data=json.dumps(data),
    headers=headers
  )  
  return response.text.replace("\"", "")

def mark_order_as_completed(id):
  data = {'filter': {'_id': id}, 'data': {'completed': True}}
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  response = requests.put(
    f'{configuration.SERVER_URL}{configuration.ENDPOINT}',
    data=json.dumps(data),
    headers=headers
  )  