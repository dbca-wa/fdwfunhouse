# FDW FunHouse

pip3 install -r requirements.txt
createdb fdwfunhouse
psql fdwfunhouse -c 'create extension postgres_fdw;'
./manage.py migrate # note the sql migration assumes superuser role for the creation of the usermapping
./manage.py createsuperuser
./manage.py runserver

You should be able to use the ForeignAuthUser and UserComment models/tables to do stuff that gets written back to django.contrib.auth.models.User using the postgres_fdw. This should work between dbs.
