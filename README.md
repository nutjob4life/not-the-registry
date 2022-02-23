# 😑 Not the Registry

This is not the PDS API nor its Registry service.


## 🏃‍♀️ Running

Several ways to do it.


### 🗾 Locally

Run:
```console
$ python3 -m venv venv
$ venv/bin/pip install --quiet --upgrade setuptools pip wheel build
$ venv/bin/pip install --requirement requirements.txt
$ venv/bin/python3 server.py
```
Then visit http://localhost:6543


### 🚢 Docker

Run:
```console
$ docker image build --tag not-the-registry:latest .
$ docker container run --rm --name not-the-registry --publish 6543:6543 --detach not-the-registry:latest
```
Then visit http://localhost:6543. Stop the container with `docker container stop not-the-registry`.


### 🕴 Jenkins

