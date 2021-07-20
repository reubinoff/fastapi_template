
# How to run
to run the project:

`./scripts/run_debug.sh`

# How to debug
the project has launch file for visual studio code. just select the `Server Debug` configuration

# Docker
docker is supported. you may build the image with the command:

`docker build -t fastapi_best .`

to run the container:

`docker run --rm --name test  -p 80:80 fastapi_best`

# Configuration
currently there is only 1 config file: `.env`
