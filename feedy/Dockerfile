FROM python:3.7-slim

RUN apt-get update && apt-get -y install build-essential

RUN mkdir /home/webapp

WORKDIR /home/webapp/

copy requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . .

RUN ["chmod", "+x", "entrypoint.sh"]

COPY celeryconf/init/celeryd /etc/init.d/
COPY celeryconf/default/celeryd /etc/default/

RUN ["chmod", "+x", "/etc/init.d/celeryd"]
