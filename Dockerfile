FROM python:3
MAINTAINER "Gerard Hickey <hickey@kinetic-compute.com>"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./taskshow.py" ]