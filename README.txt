1. Download and install: https://gitlab.com/nextgis_private/avral

2. Install this
	
		cd avral_helloworld
		python setup.py develop

3. Set avral environment
	3.1 Choose avral work directoty: ~/avral/workdir
	3.2 Ask admin for celeryconfig.py
	3.3 Put celeryconfig.py to work directoty.

4. Run worker
	4.1 cd ~/avral/workdir
	4.2 celery -A avral worker -l info -Q avral_helloworld --concurrency 1

5. Check (python)

from avral_helloworld.operations import HelloWorld
from avral.tasks import execute
from avral.io.request import AvralRequest
from avral.io.types import String

inputs = {
	"name": String("Bob")
}
request = AvralRequest(
	"hello",
	inputs
)
result = execute.apply_async(kwargs={"avral_request": request}, queue="avral_helloworld")
responce = result.get()
responce.outputs.get("hello").value
