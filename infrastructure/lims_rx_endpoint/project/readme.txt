
===== Starting the server ========================

Every time:
./setup_win.ps1
python lims_server/manage.py runserver 0.0.0.0:9101

Confirm the server is running:
http://127.0.0.1:9101

First time:
python lims_server/manage.py createmigrations
python lims_server/manage.py migrate
python lims_server/manage.py createsuperuser   (create an admin account)







