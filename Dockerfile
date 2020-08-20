#Grab the latest alpine image
FROM alpine:latest

# Install python and pip
RUN apk add --no-cache --update python3 py3-pip bash
ADD ./webapp/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
RUN mkdir /opt/webapp
RUN mkdir /opt/webapp//logs
RUN mkdir /opt/webapp//data
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp
RUN chmod -R 777 /opt/webapp

# Expose is NOT supported by Heroku
# EXPOSE 5000 

# Run the image as a non-root user
RUN adduser -D myuser
USER myuser

# run stat first time (to get data)
RUN python3 /opt/webapp/folding-stats.py

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
