# Base our container on a Slim Python + Debian (Jessie) Image
FROM resin/raspberrypi3-python:3.6-slim

# Set our working directory
WORKDIR /usr/src/app

# Copy all our project into /usr/src/app/ folder in the container.
COPY . .

CMD ["bash","project/startup.sh"]
