import os
import pathlib
import calendar
from bottle import route, run, static_file
from datetime import datetime

PORT = int(os.environ.get("PORT", 50))
BASE_PATH = pathlib.Path(__file__).parent

cal1 = calendar.HTMLCalendar(calendar.SUNDAY)
year1 = datetime.now().year
month1 = datetime.now().month
print (year1, month1)

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
    return cal1.formatmonth(year1, month1)

@route('/<year>')
def show_page(year):
    year1 = int(year)
    print(year1)
    return cal1.formatyear(year1)




run(host='0.0.0.0', port=PORT)
