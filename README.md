# Refgetter CLI Client


## How to Use Client

#### Installation
The client can be installed through pip using the following command:
```
pip install refgetter
```

The only requirement for running is Python 3, so it is usually necessary to use `pip3`:
```
pip3 install refgetter
```

#### Usage
To use the client to fetch metadata about a reference you call the package with the argument `--seq_id`. Here is an example:

```refgetter --seq_id 3050107579885e1608e6fe50fae3f8d0```

***

## Developing
This repository was designed specifically with development ease as a priority. The only pre-requisite for developing is to have docker and docker-compose installed.

[Docker installation documentation](https://docs.docker.com/get-docker/)

[Docker-compose installation documentation](https://docs.docker.com/compose/install/)

Once you have Docker and Docker-compose installed, and you have cloned the directory to your local environment, go to the project root directory and run `docker-compose build` to build the project containers, then `docker-compose up -d` to start the containers running in the background.

To build a development version of the package, run `make build-dev` and the package will be built in a way that it can be run from the container, and as code changes the package will be updated without needing to continually rebuild the package. You can call the package in the container using `make refgetter SEQID={some seq id}`


There are several other commands in the Makefile that are definitely of use to anyone wishing to contribute to the repository:

*   `make black` will apply standardized formatting to the code in this repository according to [Black](https://black.readthedocs.io/en/stable/) formatting patterns
* `make lint` will perform lint checking on the code in this repository
* `make publish` will publish the package to the PyPi server hosting it. A username and password will be asked for and only users who have been granted access to push to the PyPi server will be able to do this successfully.
* `make refgetter SEQID={some_id}` will call the refgetter command with the `--seq_id` argument, in order to pass a sequence id you will need to store it in a variable `SEQID`.
* `make test` to run tests in the testing folder using Pytest
* `make build-wheel` will build a wheel distribution of the package
* `make bash` will open a bash shell in the docker container
* `make python` will open a python client in the docker container.


Once you have built a wheel distribution of the package, you can install your version of the package locally on your machine by running:
```
python3.8 -m pip install refget/src/dist/{filename}.whl
```



***

### Future Ideas for Improvement

* CI/CD integration
    * When the main branch is merged into production, release a production version of the package to PyPi.
    * When a commit is made to the main branch, release a development version of the package to PyPi
    * When a PR is opened, run tests, formatting checking, and lint checking before being able to merge to main.
* Incorporate other endpoints of the CRAM refget API besides metadata retrieval as options when using refgetter.
* (Possibly) Add support for older Python distributions
* (Possibly) Provide a more descriptive help message when clients provide the `--help` flag, if the current message is not sufficient
* Continuously improve as people use the tool and feedback comes in!