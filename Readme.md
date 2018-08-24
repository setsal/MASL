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

## Database
Create DB file with django
 - ``$ python manage.py migrate``

Insert Data:
 1. Add text file in `pybin/text_transfer/text/`
 2. enter `pybin/text_transfer` and Run `transfer.py [textfile]`
 3. Use sqlite browser to check the data is correct

Reset & Clear All Data in DB ( recommend ):
 - Run `pybin/text_transfer/reset_table.py`

Reset Migration ( if it is necessary ):
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
