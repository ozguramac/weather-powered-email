WEATHER POWERED EMAIL

## Download and Installation

To begin development on this site:
* Setup SSH between your dev local and GitHub account
* Clone the repo: 
```
git clone git@github.com:ozguramac/weather-powered-email.git
```
* [Fork, Clone, or Download on GitHub](https://github.com/ozguramac/weather-powered-email)

### How do I get set up? ###

* Install docker/docker-compose
* Summary of set up: Recommend using Intellij IDEA to build/run.
* Configuration: docker-compose, python, django, postgres
* Add .env file to provide env values in docker-compose.yml: 
```
PORT=80
SECRET=*******************  #<---- GENERATE ONE
DBG=False  #<----- TURN THIS ON FOR DEV ENV
HOST=wxmail.derinworksllc.local  #<---- NEED THIS IN PROD
DB_NAME=postgres
DB_USER=postgres
DB_PSWD=***************  #<----- SET TO GOOD ONE in PROD
WEATHER_API_KEY=**************  #<--- FROM openweathermap.org/appid
SMTP_HOST=fakesmtp  #<--- REPLACE THIS WITH A REAL SMTP HOST
SMTP_PORT=25
SMTP_USER=fake
SMTP_PSWD=
SMTP_USE_TLS=False
```
* How to build: ```docker-compose build```
* How to run tests: TBD
* How to run: ```docker-compose up -d```
* Deployment instructions:
  - Setup deploy key (read-only SSH) between target VM and GitHub
  - ```git clone``` for the first time and ```git pull``` from VM
  - ```cd ./weather-powered-email```
  - Add a production-ready .env file with production values
  - ```docker-compose up -d```
  - Create first superuser:
    ```
    $ docker exec -it app sh
    /code # python3 manage.py createsuperuser
    Username (leave blank to use 'root'):
    .
    .
    .
    ```

### Manual End User Testing ###
Please refer to PORT from .env file if you want to run app on a
different port
* Launch your favorite browser and goto
  [here](http://wxmail.derinworksllc.local/) to subscribe
* Then goto [here](http://wxmail.derinworksllc.local/admin) to send
  emails

### Contribution guidelines ###

* Writing tests
* Code review
    - Create PR (pull request) to master branch
    - Merging PR to master requires code review and approval from teammate.
* Other guidelines
    - Create own branch for changes

### Who do I talk to? ###

* Repo owner or [admin](mailto:info@derinworksllc.com) 
* Other community or team contact

## Copyright and License

Copyright 2017 [Derin Works LLC](http://www.derinworksllc.com)