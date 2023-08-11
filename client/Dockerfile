# Download full python 3 linux image
FROM python:3

# Create a work directory on the container
WORKDIR /tmp/python_server 

# Copy the directory on my machine into the docker container
COPY . .

RUN pip3 install requests

# Command to run when we first start the container (Starts our server)
CMD exec python3 -u client.py

# Exposes port 8468 in our container, we still need to publish our port when we
# Run: docker run -p 8468:8468
# EXPOSE 8468
