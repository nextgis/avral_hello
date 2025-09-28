FROM harbor.nextgis.net/toolbox-base/ubuntu2204:6

COPY . /opt/avral_hello
RUN pip install --no-cache-dir --editable /opt/avral_hello
