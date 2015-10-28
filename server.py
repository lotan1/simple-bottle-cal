import os
import pathlib
import calendar
import datetime
from bottle import route, run, static_file, template
from datetime import datetime

PORT = int(os.environ.get("PORT", 80))
BASE_PATH = pathlib.Path(__file__).parent
cal1 = calendar.HTMLCalendar(calendar.SUNDAY)
year1 = datetime.now().year
month1 = datetime.now().month

print (year1, month1)

def links(year, month):
    if month > 1 :
        monthP = month - 1
    else:
        monthP = 12,
    if month < 11:
        monthM = month + 1
    else:
        monthM = 1,
    return {'monthP': monthP,
            'monthM': monthM,
           }


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=str(BASE_PATH / 'static'))

@route('/')
def home():
    return cal1.formatmonth(year1, month1)

@route('/<year>/<month>')
def show_page(year,month):
    year1 = int(year)
    month1 = int(month)
    print(year1,month1)
    return template('calte2', calendar = cal1.formatmonth(year1,month1), monthP = monthP, monthM = monthM, year = year1)

@route('/<year>')
def show_page(year):
    year1 = int(year)
    return template('calte', calendar = cal1.formatyear(year1))

run(host='localhost', port=PORT)
