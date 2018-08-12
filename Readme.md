# MASL TOPIC

Cheers OAO/

## Getting started

Install dependencies:

``` bash
$ git clone git@github.com:setsal/MASL.git
$ cd MASL
$ npm install
$ pip install -r requirements.txt
```

Run developement server:

``` bash
$ node server.js
$ python manage.py runserver
```

Create DB file with django

``$ python manage.py migrate``
``$ python trasnfer.py text/*txt``


Reset Migration:
 1. Remove target table in database
 2. run the ResetMigration.sh script


## Cautions:
 -  WordCloud Package need Microsoft Visual Studio C++ 14.0 package, you must install it before using.
    1. Install Via Visual Studio
    2. Install Via binary .whl file ( http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud )


## Contributors

- setsal Lan
- MeteorV Hsu
- Andy Chu
- Momo Zhang
