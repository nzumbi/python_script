import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, Iso, Site, Region ,State

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Category.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()



    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python



    for row in reader:
        print(row)

        try:
            c, created = Category.objects.get_or_create(name=row[7])
        except:
            c, created=None

        try:
             s, created = State.objects.get_or_create(states=row[8])
        except:
            s, created=None

        try:
            r, created = Region.objects.get_or_create(region=row[9])
        except:
            r, created=None

        try:
            i, created = Iso.objects.get_or_create(name=row[10])
        except:
            i, created=None

        #x = Category(name=row[7])
       # x.save()
        #x = Iso(name=row[10])
        #x.save()

        #x = Region(region=row[9],category=row[7],states=row[8],iso=row[10])
       # x.save()
       # x = State(states=row[8],category=row[7],region=r,iso=row[10])
       # x.save()







        try:
            y = int(row[3])
        except:
            y = None

        try:
            site = Site(name=row[0], description=row[1], year=y, justification=row[2], longitude=row[4], latitude=row[5], area_hectares=row[6])
        except:
            site=None

            site.save()