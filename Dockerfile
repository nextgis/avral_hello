FROM harbor.nextgis.net/toolbox-base/ubuntu2204:2

COPY . /opt/avral_helloworld
RUN pip3 install --no-cache-dir /opt/avral_helloworld
