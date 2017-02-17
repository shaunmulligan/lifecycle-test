FROM resin/raspberrypi3-python:2.7-slim

WORKDIR /usr/src/app

# Copy all our project into /usr/src/app/ folder in the container.
COPY . .
# So in our container we should now have:
# /usr/src/app/
#           |── Dockerfile
#           └── project
#               └── main.py
CMD ["python","-u","project/main.py"]
