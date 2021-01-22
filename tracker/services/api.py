from tracker.configuration import configuration

import requests

def create_object_missing_report():
  response = requests.post(
    f'{configuration.SERVER_URL}{configuration.ENDPOINT}',
    {'id': {configuration.OBJECT_ID}}
  )