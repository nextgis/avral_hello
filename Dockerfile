FROM harbor.nextgis.net/toolbox-workers/base:1.0.5-ubuntu2004

COPY . /opt/avral_helloworld
RUN pip3 install --no-cache-dir /opt/avral_helloworld
