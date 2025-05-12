from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnnct = mysql.connector.connect(user='', password='',
                                host='',
                                database='login')
cnnct.close()
