Build and run container

```
git clone https://gitlab.com/nextgis/toolbox_public/avral_hello.git --depth 1
cd avral_hello
docker build -t avral_hello:latest .
docker run --rm -t -i -v ${PWD}:/avral_hello avral_hello:latest  /bin/bash
```

Run in container

```
cd /avral_hello
pip install -e /avral_hello
```

Test

```
avral-exec hello "name" 5
avral-exec hello "name" ""
```

Deploy

```
docker build -t avral_hello:latest .
docker tag avral_hello:latest harbor.nextgis.net/toolbox-workers/hello:prod
docker image push harbor.nextgis.net/toolbox-workers/hello:prod
```

## Call of this insturument on server ##

### Testing: run directly\synchronously (without queue)
```python
from avral.tasks import execute
from avral.io.request import AvralRequest

inputs = {"name": "Alexander"}
request = AvralRequest("hello", inputs)
response = execute(request)
response.outputs
```

### Testing: run asynchronously (with queue)
Configure avral and Run worker before for queue with name <queue_name> 
see https://gitlab.com/nextgis_private/avral/wikis/Install,-configure-and-test#test-advanced
```python
from avral.tasks import execute
from avral.io.request import AvralRequest

queue_name = "<queue_name>"

inputs = {"name": "Alexander"}
request = AvralRequest("hello", inputs)
result = execute.apply_async((request,), queue=queue_name)
response = result.get()
response.outputs
```

### Testing (with avral_web)
see https://gitlab.com/nextgis_private/avral/wikis/Install,-configure-and-test#%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA-%D1%80%D0%B0%D0%B7%D0%B2%D0%B5%D1%80%D0%BD%D1%83%D1%82%D0%BE%D0%B9-%D0%B2-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B5-%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81-%D0%BA-avral-web
