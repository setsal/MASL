# MASL TOPIC

Cheers OAO/

![demo](https://raw.githubusercontent.com/setsal/MASL/master/frontend/dist/brand.jpg)


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

## Database
Create DB file with django
 - ``$ python manage.py migrate``

Insert Data:
 1. Facebook API
     - Run `pybin/fb_fetch/crawler_and_insert.py`
 2. News Data
     - Run `pybin/media_fetch/news_transfer.py`

Reset & Clear All Data in DB ( recommend ):
 - Run `reset_table.py` in `fb_fetch` or `media`

Reset Migration ( if it is necessary ):
  1. Remove target table in database
  2. run the ResetMigration.sh script

## Cautions:
 -  Some Package need Microsoft Visual Studio C++ 14.0 package, you must install it before using. ( e.g. WordCloud )
    1. Install Via Visual Studio
    2. Install Via binary .whl file


## Contributors
- setsal Lan
- MeteorV Hsu
- Andy Chu
- Momo Zhang
