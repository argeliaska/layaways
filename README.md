# layaways API
API Rest for comic's layaways 

## Prerequisites

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Install pre-commit hooks

## Running on a local environment with Docker

### Environment
For running the API in a right way it needs some variables, there is a default file named `env.example` which you can use as a example. If you want the `.env` file with all the variables used in this project please contact me by sending a email to argeliaska@gmail.com.


### Running services
If you have already set up your local environment and have a **.env** file with the development variables set, this command builds the image `layaways-api:1.0.1` and starts the services `layaways-api` and `layaways-api-db`:

```shell
$ docker-compose up -d
```
Load the URL http://localhost:8000/ into your browser.
