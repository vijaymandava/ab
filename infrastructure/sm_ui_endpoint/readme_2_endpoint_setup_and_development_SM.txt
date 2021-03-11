
===========================================================
================= SETTING UP THE ENDPOINT =================
===========================================================

Remote desktop to the AWS server running the SM.
cd c:\
git clone http://sqa-auto/github/testbench_cm.git

type python --version  If this returns a sensible version then skip to the next step.
If it fails you probably have an absolutely clean/fresh AWS instance.  This has no python and a very old update of Win7.
	This first-time update takes some time... expect 2 hours...
	It is necessary to install python...
	Download and install from https://www.python.org/downloads/
	But that requires an update to windows - use "windows update"...
	But that requires an update to Window Update (itself) do that !
	pop the stack 3 times and you're ready to start
	Set-ExecutionPolicy RemoteSigned 
	type 'python --version'   and you should see python 3.8.x


Run the setup file
cd testbench_cm\sm_ui_api\project
./setup_win.ps1

======= SM application ======= 


Menu -> General Settings
	LIMS Customer ID: E5196
	LIMS Activation Code:  NUAvuWGrgE/jd0++2+7DygNOAmRZy4ocKMmKu8yoPtc=

	Unchecked:
		Bridge Computer
		Signature Comment (Display, Require)
	Checked:
		all the rest

Technician -> Single Signin
	(logged in) this requires an account such as TestBench123 or you can use fieldservice

Technician -> Systems Settings -> Configure
	General:
		System Serial Number E05115196
		System Type = EM / Filtration
	Configure:
		Asset Tag E01014000
		Central Manager Client (checked)
			Base URL Only (unchecked)
			Base URL:  http://192.168.2.110:3002/    this is the CM IP
		Central Manager Server
			Enable Server (checked)
			Base URL: http://192.168.2.29:3002/    this is this SM's IP for net on which CM is attached
Development -> System Configuration -> 
	Vision -> Image Interval = 5 minutes
	Config -> Simulator (check 5 checkboxes)
	Config -> Monitor UPS using Ethernet (unchecked)
	Config -> Method Interval Minutes (checked)
	Config -> Allow Blank Username and Password (checked)

Menu -> Methods ->
		m5 (5 minutes)
		m10000 (10000 minutes)
	Action-Alerts
		a (defaults)
	Handling Rules
		h (defaults)
	Samples
		s5
		s10000


======= Before starting endpoint ==================

NOT NECESSARY::9100
      Edit the API endpoint settings.py to add SM IP:
      notepad .\api_endpoint\project_endpoint\project_endpoint\settings.py
      change the line with ALLOWED_HOSTS to be:
      ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.xxx.yyy']
      where xxx.yyy is ip
      The single-quotes are necessary.

======= Start the endpoint =========

python .\api_endpoint\project_endpoint\manage.py runserver <your_sm_host_ip>:9100

fire up a browser on the SM:
  <your_sm_host_ip>:9100  and you shoud see "sm_api" and "admin" as candidates
  <your_sm_host_ip>:9100\am_api\welcome  and you should see a welcome message.

fire up a browser on your Laptop (on AWS VPN)
    <your_sm_host_ip>:9100  and you shoud see "sm_api" and "admin" as candidates
    <your_sm_host_ip>:9100\sm_api\welcome  and you should see a welcome message.
    IF THIS DOES NOT WORK: confirm the EC2 instance has Security Group "SQA SM UI Automation Endpoint"
    Security Group is changed on AWS EC2 instances page.  Actions dropdown -> Networking -> Change Security Groups
    No need to re-start server or endpoint.

At this point the web server for the endpoint is running and will accept API commands.

Confirm similar access is available from a different host on the AWS netowrk such on your laptop running AWS VPN
  <your_sm_host_ip>:9100\am_api\welcome


======= Migrate database and create superuser ========

This is not technically necessary because we are not using the database or accounts, but for good measure:
python .\api_endpoint\project_endpoint\manage.py showmigrations
python .\api_endpoint\project_endpoint\manage.py migrate
python .\api_endpoint\project_endpoint\manage.py createsuperuser
you can then visit the /admin page if you want and login. There is not much there.


===== Confirm the api GETs =====================

You shoud use a browser do some GETs.  We know the frontend web API is working - this will confirm the SM application is running, you are running as Admin, and other stuff, the UI is at the home page (necessary as a starting point), etc.

http://<your_sm_host>:9100/sm_ui/home/get_test_list
http://<your_sm_host>:9100/sm_ui/approve/get_test_list
http://<your_sm_host>:9100/sm_ui/retrieve/get_test_list

===== Standalone tests =====================

There is a set of standalone tests to confirm internal functioning of the BFM.  This runs API commands (GET and POST) to the BFM.  It assumes a SM instance is running on that server (SM UI is accessible).  The tests are run from the command line using pytest.  Type the following command:
pytest
and you should see several tests run and pass, with the UI being manipulated by the tests.


===========================================================
======= INTERNALS AND DEVELOPMENT ENVIRONMENT  ============
===========================================================


====== Virtualenv =======================

setup_win.ps2, pip, requirements.txt

==== IDE ===========

Recommend Visual Studio Code but anything with a linter should work.
code -n .

====== Django web server ================

Django is a web server.  It provides the front-end of the API endpoint, so that tests running on another host can access the BFM. The web server makes URLs available to the test, and receives GET/POST API commands from the test.  The web server has backend code (pywinauto) that it uses to access the user interface elements.

References: 
https://www.djangoproject.com/


====== pywinauto ========================

SM is a Microsoft WFC (Windows Foundation Class) application.
Pywinauto is the library that gives access to elements in a WFC application, in our case the SM User Interface. 

References:
Home page: http://pywinauto.github.io/
Docs Intro: https://pywinauto.readthedocs.io/en/latest/
Getting Started Guide: https://pywinauto.readthedocs.io/en/latest/getting_started.html
StackOverflow tag: https://stackoverflow.com/questions/tagged/pywinauto


======== GUI Object Inspection / Spy tools ==========

These are tools to find the "name" of WFC UI objects.  During development it is necessary to find the name of the UI objects.  The name is then coded into the web server backend.

Per https://pywinauto.readthedocs.io/en/latest/_sources/getting_started.txt
just git clone https://github.com/blackrosezy/gui-inspect-tool and they are there.


