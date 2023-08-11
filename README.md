# Docker presentation
A quick intro to a basic docker setup.

## What is docker?
Docker is a container system, it allows you to put your services into an easy to distribute container
that usually has a filesystem and your service(s) available for use on it.

This allows us to make easily reproducible builds, no more "It works on my machine". Docker aims to take
the pain out of building software. It also allows us to manage service and system deployments.

## Getting started
Go to: [Docker](https://www.docker.com/) and download the version of docker best suited for your system. Follow their guide to getting setup.

## Without Docker
I've built a little python server that serves get requests on my local network, all it does is reply with a
"hello mate". Lets see what it looks like when I run it.

## My first image
At its core an image is just a set of commands that build off a base, this base is normally an operating system such as alpine or more full fledged such as windows. 

Now lets dockerise it by first turning it into an image with our very basic Dockerfile.

We're going to run the command:

`docker build -t simple_server .`

This will build our image with the dockerfile found in the current directory.


## My first container
A container is just a running image, our Dockerfile shows that our image should just be a basic linux filesystem with python3 available to us. Lets start our container now with the command:

`docker run -dp 8468:8468 simple_server`

This command tells docker to run our container with the flags `d` which means detached mode so it starts in the background and `p 8468:8468` which is the port to bind from our localhost to the container.


## Using a compose file
A compose file is how most people operate docker containers. In our compose file we can list several services
and where to find them, set their details such as networking and container names. The full spec can be found
here: [Docker-compose](https://github.com/compose-spec/compose-spec/blob/master/spec.md).  It's always worth taking a look at the spec for options you might need or miss.


## Debugging containers (Basics)
We can do a couple things to debug containers such as follow the containers logs and attach our shell to the container and mess around on it.

To follow logs we do:

`docker logs -ft CONTAINER_NAME`
The `-f` means: `--follow`
The `-t` means: `--timestamps`

This follows the logs of our container.

To actually get into a container we can use `docker exec -it "/bin/bash"` or in longform: `docker exec --interactive --tty "/bin/bash"` this opens a terminal session on the container for us to do whatever
we want on it.