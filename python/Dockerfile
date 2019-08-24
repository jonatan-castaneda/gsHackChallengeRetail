FROM python:3.5

RUN apt-get update
RUN apt-get install --assume-yes apt-utils locales
RUN apt-get install --assume-yes apt-utils 
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      build-essential \
      xorg \
      libssl-dev \
      libxrender-dev \
      wget \
      gdebi \
      libxrender1 \
      xfonts-utils \
      xfonts-base \
      xfonts-75dpi
RUN sed -i 's/# es_ES.UTF-8 UTF-8/es_ES.UTF-8 UTF-8/' /etc/locale.gen
RUN locale-gen es_ES.UTF-8
ENV LANG es_ES.UTF-8
ENV LANGUAGE es_ES  
ENV LC_ALL es_ES.UTF-8 
WORKDIR /tmp     
RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN tar -xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
WORKDIR /tmp/wkhtmltox
RUN cp -r * /usr/
RUN pip3 install geopy beautifulsoup4 \
	flask==0.11.1 flask_restful==0.3.5 requests>2.4.2 \
	cherrypy paste Pillow
RUN	apt-get install --assume-yes musl-dev g++
RUN pip3 install timezonefinder
RUN pip3 install nltk timezonefinder dateparser requests-cache joblib
RUN pip3 install pyqrcode qrcode pillow
RUN pip3 install git+https://github.com/rubend824/imgkit
RUN pip3 install pybars3
RUN apt-get install  --assume-yes sqlite3 libsqlite3-dev
RUN pip3 install git+https://github.com/pysimplesoap/pysimplesoap
RUN pip3 install coverage
RUN pip3 install flask-cors
RUN pip3 install pymongo
RUN pip3 install scipy
RUN pip3 install numpy
RUN pip3 install --upgrade google-cloud-language
RUN pip3 install xmltodict
RUN pip3 install redis
RUN pip3 install pyjwt
RUN pip3 install celery
COPY ./fonts/* /usr/share/fonts/opentype/
RUN fc-cache -f -v
COPY ./ /code/gus
