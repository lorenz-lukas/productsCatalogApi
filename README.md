# Catalog Project

    Project using django, flask, RabbitMQ and React with microservices arquitecture

# Requirements

- [Docker](https://docs.docker.com/engine/install/ubuntu/)

- [Docker Compose](https://docs.docker.com/compose/install/)

    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

    sudo chmod +x /usr/local/bin/docker-compose

- Add Docker to user group (run without sudo):

    sudo usermod -aG docker ${USER}

    sudo reboot

*OBS*: If does not install mysqlclient, install libmysqlclient-dev and try again.

    sudo apt install libmysqlclient-dev 

*OBS2*: Check docker-compose length in bytes.

*OBS3*: Install MySQL Database Manager from Cweijan in VScode Extensions to connect and manager your database.

# Aply Database migrations

- docker-compose exec backend sh

- python catalog/manage.py makemigrations

- python catalog/manage.py migrate