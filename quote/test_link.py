import pyodbc
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import os

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iplan_django.settings')
    print("%" * 80)
    connection = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=117.50.82.37,1433;DATABASE=YZDQUOTE;UID=iplan;PWD=1234qwerasdfzxcv!')

    curs = connection.execute('select GETDATE()')
    print("%"*80)
    print(curs)