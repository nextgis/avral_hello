FROM harbor.nextgis.net/toolbox-base/ubuntu2204:6

COPY . /opt/avral_hello
RUN pip3 install --no-cache-dir /opt/avral_hello
