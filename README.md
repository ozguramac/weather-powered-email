Klaviyo Weather App
-------------------

[Spec](https://www.klaviyo.com/weather-app)

Prerequisites
-------------

- Install docker and docker-compose for your local OS env

Automated Testing
-----------------

TODO..

Setup & Run
-----------
Add a .env file to the project root with the environment values set e.g. as follows:
```
PORT=80
DB_NAME=postgres
DB_USER=???
DB_PSWD=???
WEATHER_API_KEY=???
SMTP_HOST=fakesmtp
SMTP_PORT=25
SMTP_USER=fake
SMTP_PSWD=
SMTP_USE_TLS=False
```

and bring up as follows:
```
$ docker-compose up -d
```

and do some first time setup:
```
$ docker exec -it app sh
/# cd code
/code # python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
.
.
/code # python3 manage.py createsuperuser
Username (leave blank to use 'root'):
.
.
.
```

Manual End User Testing
-----------------------

Launch your favorite browser and goto http://127.0.0.1/app (refer to PORT from .env file if different)
Go through steps to add email and select a location and hit Subscribe

Manual Admin Testing
--------------------

Go to http://127.0.0.1/admin/app/user/
Select all and select "Send Weather-Powered Emails to Users" admin action

Note that if testing via Fake SMTP, then following command will help with debugging:
```
$ docker logs fakesmtp
```

FAQ
---
Q. Can I change the port from 80 to something else?
A. Yes, edit the value for your PORT variable in your .env

Q. How can I access the database directly?
A. Uncomment ports portion of db container under docker-compose.yml

Q. How do I obtain a Open Weather Map API Key?
A. Follow instructions at [API | Open Weather Map](http://openweathermap.org/api)

Q. How can I see the emails being fake-sent through Fake SMTP?
A. Use following docker commands e.g.:
```
$ docker exec fakesmtp ls /var/mail
171117095647881.eml
$ docker exec fakesmtp cat /var/mail/171117095647881.eml
       Fri, 17 Nov 2017 21:56:47 +0000 (UTC)
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Enjoy a discount on us.
From: fake@fakesmtp
To: weatherapp+anc@klaviyo.com
Date: Fri, 17 Nov 2017 21:56:47 -0000
Message-ID: <20171117215647.40.4184@dcfe6c9251ec>

Current temperature in Anchorage,  Alaska is 72, Sunny.
```

Contact
-------
Please contact repo owner for any other questions or concerns.