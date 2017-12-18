1. Testing (with python)

from avral.tasks import execute
from avral.io.request import AvralRequest

inputs = {"name": "Alexander"}
request = AvralRequest("hello", inputs)
result = execute.apply_async((request,), queue="tests")
responce = result.get()
responce.outputs


2. Testing (with avral_web, see avral_web README)

import requests

url = 'http://dev.nextgis.com/avral/json/execute'
data = {'operation':'hello', 'inputs': {"name": 'Bob'}}
result = requests.post(url, json=data)

task_id = result.json().get("task_id")
print "task_id: ", task_id
url = 'http://dev.nextgis.com/avral/json/check/%s' % task_id
result = requests.get(url)
print result.text