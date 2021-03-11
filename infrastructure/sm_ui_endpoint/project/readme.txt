
================ Overview

The steps below identify
a) how to start the endpoint for use in running CM/SM tests
b) how to run unit-level tests on the endpoint code itself (frontend and backend)

================ Start the endpoint for use in testing CM/SM

To start the endpoint issue the following commands:
cd to the folder that has this readme (SQA_Testbench\infrastructure\sm_ui_endpoint\project)
./setup_win.ps1
python .\frontend_api_endpoint\project_endpoint\manage.py runserver 0.0.0.0:9100

=============== Running Unit-level Testing the endpoint itself

There are backend tests and frontend+backend tests.

To run backend tests:
cd to the folder that has this readme (SQA_Testbench\infrastructure\sm_ui_endpoint\project)
./setup_win.ps1
pytest -m sm_backend_tests --html=report_backend_.html
Optional:  --collect-only

To run frontend+backend tests:
Start the endpoint (refer to instructions above).  Note the endpoint runs in its own powershell.
From the current powershell:
cd to the folder that has this readme (SQA_Testbench\infrastructure\sm_ui_endpoint\project)
./setup_win.ps1
pytest -m sm_frontend_tests --html=report_frontend_.html
Optional:  --collect-only



xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxx other crap xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

On the server running SM:

Start a powershell as administrator

setup the environment
  .\setup_win.ps1


For AWS server running SM you must configure the associated security group and network access control list (network ACL).
This is done to allow http traffic inbound/outbound.
Refer to:
https://aws.amazon.com/premiumsupport/knowledge-center/connect-http-https-ec2/


Add the IP address of the server to the ALLOWED_HOSTS in sm_ui_api\project\api_endpoint\project_endpoint\project_endpoint\settings.py
For example if the host is 192.168.2.29 this would look like:
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1], '192.168.2.29']

Open firewall access to TCP port 9100.  On Windows:
  Navigate to Control Panel, System and Security and Windows Firewall.
  Select Advanced settings and highlight Inbound Rules in the left pane.
  Right click Inbound Rules and select New Rule.
  Add the port you need to open and click Next.
  Add the protocol (TCP) and the port number (9100) into the next window and click Next.
  Select Allow the connection in the next window and hit Next.
  Select the network type as you see fit and click Next.
  Name the rule something meaningful and click Finish.



list the tests
  pytest --co tests

run a test
  pytest .\tests\test_01_sm_ui_home_get_test_status.py
  Note when running tests it is assumed:
	single sign-in is turned on
	there is at least one test to approve
	there is at least one test to cancel

run all tests
  go_regress_cm_sm.ps1
 <or>
  pytest .\tests

start Visual Studio Code (IDE) development environment
  code -n .





