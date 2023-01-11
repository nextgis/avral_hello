FROM registry.nextgis.com/toolbox-workers/base:0.0.3-ubuntu1804

COPY . /opt/avral_helloworld
RUN pip3 install --no-cache-dir /opt/avral_helloworld
