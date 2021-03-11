
We will be testing using Selenium using Python.
If you are not familiar with Selenium you can follow instructions at udemy https://www.udemy.com/course/selenium-with-python/
This costs $12 but is very worth it.

We have a RMB Testbench Environment on git, instructions below.

+================== Populate the RMB Testbench Environment ============

Windows users:
Create folder "testbench"
start powershell
cd testbench
git clone  http://sqa-auto/github/testbench_cm.git
Username is your rapidmicro username,  your password is ‘password’.   -------------->  Bangalore use "bangalore" "password"
cd  .\testbench_cm\practice_2_udemy\project\

Run the "setup" script. This creates a virtualenv and adds to PATH and PYTHONPATH.  
<windows> .\setup_win.ps1
<linux>   source setup_linux.sh  (not fully tested but should work)

Optional: populate the contents from the Udemy tutorial.  This is not technically necessary but this is the entire code fromthe tutorial and is handy if you want to skip ahead or use as reference.
git clone https://github.com/testingworldnoida/SeleniumPython.git

Download and install an IDE (I recommend Visual Studio Code and my instructions below use that)
Start Visual Studio code.  To do this type "code -n ."

====== follow instructions from the Udemy tutorial above =================

You already completed many sections of the Udemy tutorial.  Here's what you need to review:

Section 1 (Overview)              OPTIONAL: if you need review on this
Section 2 (Pythonm,PIP,pycharm)   NO: the setup script already set up virtualenv.  No need for these unless you have problems.
Section 3 (Element Locators)      YES: if you are not familiar with Selenium
	Example facebook.com
	HTML tag, attribute, inner text

	You will need to install Chrome plugins: Selenium IDE, CSS/XPATH Checker. This is detailed in the tutorial but...
	Google Search:  selenium ide chrome plugin download
	Google Search:  selenium css xpath checker download
	with those two plugins you will have 2 new icons in the top-right of your Chrome browser

	Using Selenium IDE
		Syntax 1=locating by ID    id=pass id=u_0_16
		Syntax 2=locating by NAME  name=email
        	Syntax 3=locating by LINK  link=Forgot account?
		Syntax 4=locating by CLASS  class='input text'
	CSS element locator
 		Syntax 1=id   css=#email   css=input#email
		Syntax 2=classname  css.inputtext  css=input.inputtext
		Syntax 3=any attribute   [type='email']   css=input[id='email']
		Syntax 4=id+attribute   css=#pass[type='password']  css=input#pass[type='password']
		Syntax 5=class+attribute   .inputtext[type='email']  input.inputtext[type='email']
	XPATH
		Syntax 1=single attribute	//input[@value='Log In']
		Syntax 2=mult attribute w/or	//input[@name='firstname' or area-label='First name']
		Syntax 3=mult attribute w/and	
		Syntax 4=* on att name or tag
		Syntax 5=innertext		//div[text()='Create a new account']  //a[text()='Create a Page']
		Syntax 6 partial text		//div[contains(text(),'new account')]
		Syntax 7 partial attribute	//input[contains(@type,'pass')]
(frequent)	Syntax 8 via parent		//table[@role='presentation']/tbody/tr[2]/td[1]/input
		Syntax 9 via child		//iput[@type='email'/parent::td/parent::tr/parent:tbody/parent::table
		Syntax 10 via siblings		//input[@id='tab2']/following-sibling::label
		Syntax 11 multiple approaches


Section 24: Selenium w/ Python
	We have already installed RMB environment.  The setup.ps1 installs
		Selenium module (specified in the requirements.txt file)
		Selenium ChromDriver for Chrome 83  under /lib_webdriver_chrome
		updates to PATH and PYTHONPATH for above

	I prefer Visual Studio Code but you can use whatever IDE.
	PLEASE ENABLE A LINTER like flake8

	Example from Udemy: test_FirstTestcase.py

Section 27: PyTest unit testing Framework
	The requiremnts.txt file already loaded pytest

	The following summarizes how to enable PyTest, discover and run tests.  For reference
		https://code.visualstudio.com/docs/python/testing#_enable-a-test-framework
	To enable PyTest in Visual Studio Code: open the Command Pallette (Ctrl+Shift+P) -> Python Configure Tests -> PyTest  and select ". Root directory
	To trigger test discovery: (Ctrl+Shift+P) -> Python Discover Tests  -OR- click on "status bar" (blue tray at bottom)
	If discovery succeeds, the "status bar" (bottom in blue) shows Run Tests
	If discovery fails it will show "Test discovery failed" - to understand:  View -> Open View -> Python Test Log
	To see test list - click on the test tube beaker icon on the left

	There will be one test "test_TC_001_FirstTestCase.py
	To run the test click on the green arrow
	To see test summary status - click on the checkbox on the "status bar" (blue tray at bottom)











by CLASS  .





<windows) .\setup_win.ps1
<linux>   source setup_linux.sh


Section 4 (XPath in Detail)       YES
Section 5 (Basic Scripting)       YES
Section 6 (Condition Handling)    YES
all the rest YES





You will follow instructions from the tutorial above
You will need to install selenium IDE for chrome and/or Firefox
The  have a script to set up libraries (modules) so you can skip several sections - details below.


download and install Selenium IDE from  https://www.selenium.dev/selenium-ide/   This runs as a plugin in Chrome browser.



xxxxxxxxxxxxxxxxxxxxxxxx

Testbench assumes Chrome version 83 is the browser, other versions/browsers can be added.

code -n .  (this starts Visual Studio Code.  If you do not have this download it from Microsoft)
open test01.py
<F5> (run Python file)
browser comes up



